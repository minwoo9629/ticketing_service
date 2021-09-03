from django import conf
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from concertapp.models import Performance, Schedule, PerformanceSeat
from reservationapp.models import Ticket, Reservation
from django.conf import settings
from uuid import uuid4
import requests
from django.views.generic import DetailView, ListView
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
        # url 연결을 위한 domain 값
        domain = request.META['HTTP_ORIGIN']
        # 수량
        quantity = request.POST.get('count')
        # 공연 일자
        date = request.POST.get('date')
        # 좌석 구역
        area = request.POST.get('area')
        # 예매 개수
        total_amount = request.POST.get('totalAmount')
        # 예약 번호 생성
        partner_order_id = uuid4().hex
        partner_user_id = request.user.username
        schedule = schedule.get(start_dt=date)
        item = PerformanceSeat.objects.filter(schedule=schedule,seat__area=area,reserved=False)[0]
        item_name = f"{item.seat}"

        if int(quantity) >=2 :
            item_name += " 외 {}건".format(int(quantity)-1)

        headers = {
            "Authorization": f"KakaoAK {ADMIN_KEY}",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }
        params = {
            # 테스트용 코드
            "cid": "TC0ONETIME",
            # 주문번호
            "partner_order_id": partner_order_id,
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
        request.session['partner_order_id'] = partner_order_id
        request.session['area'] = area
        request.session['schedule_pk'] = schedule.pk
        next_url = res.json()['next_redirect_pc_url']   
        return redirect(next_url)


def payment_approval(request):
    URL = "https://kapi.kakao.com/v1/payment/approve"
    ADMIN_KEY = settings.ADMIN_KEY
    partner_user_id = request.user.username
    partner_order_id = request.session['partner_order_id']
    area = request.session['area']
    schedule_pk = request.session['schedule_pk']

    headers = {
            "Authorization": f"KakaoAK {ADMIN_KEY}",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }
    params = {
            "cid": "TC0ONETIME",
            "tid": request.session['tid'],
            "partner_order_id": partner_order_id,
            "partner_user_id": partner_user_id,
            # Query String으로부터 받은 pg token
            "pg_token": request.GET.get('pg_token')
        }
    res = requests.post(URL, headers=headers, params=params)
    amount = res.json()['amount']['total']
    quantity = res.json()['quantity']
    res = res.json()

    # 예약 정보 저장
    reservation = Reservation(id=partner_order_id,user=request.user)
    reservation.save()
    schedule = Schedule.objects.get(pk=schedule_pk)
    seats = PerformanceSeat.objects.filter(schedule=schedule,seat__area=area,reserved=False)[:int(quantity)]
    # 티켓 생성
    tickets = []
    for idx in range(int(quantity)):
        seat = seats[idx]
        tickets.append(Ticket(user=request.user, schedule=schedule, seat=seat.seat, reserve=reservation))
        seat.reserved = True
        seat.save()

    Ticket.objects.bulk_create(tickets)

    context = {
        'res': res,
        'amount': amount,
    }
    return render(request, 'reservationapp/payment_approval.html', context)


class TiketListView(ListView):
    model = Reservation
    template_name = 'reservationapp/ticket_list.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        reservations = Reservation.objects.filter(user=self.request.user)
        return reservations