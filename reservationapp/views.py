from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from concertapp.models import Performance, Schedule, Seat
from reservationapp.models import Reservation
from django.conf import settings
import requests
# Create your views here.

@login_required
def reserve(request, pk):
    if request.method == "GET":
        performance = Performance.objects.get(id=pk)
        schedule = Schedule.objects.filter(performance=performance)
        seats = Seat.objects.filter(concert_hall=schedule[0].concert_hall)
        context = {
            'performance':performance,
            'schedule':schedule,
            'seats':seats,
        }
        return render(request, 'reservationapp/reserve.html', context)

    if request.method == "POST":
        URL = "https://kapi.kakao.com/v1/payment/ready"
        ADMIN_KEY = settings.ADMIN_KEY
        headers = {
            # "KakaoAK " + "Kakao Developers에서 생성한 앱의 어드민 키"
            "Authorization": f"KakaoAK {ADMIN_KEY}",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }
        params = {
            # 테스트용 코드
            "cid": "TC0ONETIME",
            # 주문번호
            "partner_order_id": "1001",
            # 유저 아이디 
            "partner_user_id": "admin",
            # 구매 물품 이름
            "item_name": "IU[POEM]",
            # 구매 물품 수량
            "quantity": "1",
            # 구매 물품 가격
            "total_amount": "100",
            # 구매 물품 비과세
            "tax_free_amount": "0",         
            "approval_url": "http://127.0.0.1:8000/",
            "cancel_url": "http://127.0.0.1:8000/reservation/reserve/3",
            "fail_url": "http://127.0.0.1:8000/reservation/reserve/3",
        }
        res = requests.post(URL, headers=headers, params=params)
        request.session['tid'] = res.json()['tid']
        next_url = res.json()['next_redirect_pc_url']   
        return redirect(next_url)