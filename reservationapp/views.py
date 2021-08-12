from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from concertapp.models import Performance, Schedule, Seat
from reservationapp.models import Reservation
from django.conf import settings
import requests
# Create your views here.

@login_required
def reserve(request, pk):
    performance = Performance.objects.get(id=pk)
    schedule = Schedule.objects.filter(performance=performance)
    if request.method == "GET":    
        context = {
            'performance':performance,
            'schedule':schedule,
        }
        return render(request, 'reservationapp/reserve.html', context)

    if request.method == "POST":
        URL = "https://kapi.kakao.com/v1/payment/ready"
        ADMIN_KEY = settings.ADMIN_KEY
        domain = request.META['HTTP_ORIGIN']
        partner_order_id = "1001"
        partner_user_id = request.user.username
        quantity = request.POST.get('count')
        date = request.POST.get('date')
        area = request.POST.get('area')
        total_amount = request.POST.get('totalAmount')
        item = Reservation.objects.filter(schedule=schedule.get(start_dt=date),seat__area=area,user=None)[0]
        item_name = f"{item.seat}"
        headers = {
            "Authorization": f"KakaoAK {ADMIN_KEY}",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }
        params = {
            # 테스트용 코드
            "cid": "TC0ONETIME",
            # 주문번호
            "partner_order_id": "1001",
            # 유저 아이디 
            "partner_user_id": partner_user_id,
            # 구매 물품 이름
            "item_name": item_name,
            # 구매 물품 수량
            "quantity": quantity,
            # 구매 물품 가격
            "total_amount": total_amount,
            # 구매 물품 비과세
            "tax_free_amount": "0",         
            "approval_url": f"{domain}/reservation/reserve/payment_approval",
            "cancel_url": f"{domain}/reservation/reserve/3",
            "fail_url": f"{domain}/reservation/reserve/3",
        }
        res = requests.post(URL, headers=headers, params=params)
        request.session['tid'] = res.json()['tid']
        request.session['reserve_pk'] = item.pk
        next_url = res.json()['next_redirect_pc_url']   
        return redirect(next_url)


def payment_approval(request):
    URL = "https://kapi.kakao.com/v1/payment/approve"
    ADMIN_KEY = settings.ADMIN_KEY
    partner_user_id = request.user.username
    reserve_pk = request.session['reserve_pk']
    reservation = Reservation.objects.get(pk=reserve_pk)
    reservation.user = request.user
    reservation.save()

    headers = {
            "Authorization": f"KakaoAK {ADMIN_KEY}",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }
    params = {
            "cid": "TC0ONETIME",
            "tid": request.session['tid'],
            "partner_order_id": "1001",
            "partner_user_id": partner_user_id,
            # Query String으로부터 받은 pg token
            "pg_token": request.GET.get('pg_token')
        }
    res = requests.post(URL, headers=headers, params=params)
    amount = res.json()['amount']['total']
    res = res.json()
    context = {
        'res': res,
        'amount': amount,
        'reservation': reservation
    }
    return render(request, 'reservationapp/payment_approval.html')