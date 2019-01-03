from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import render
import json
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import dong_data

# 인덱스 화면을 띄우는 함수
def index(request):
    print("---------index()-------------")

    return render(request, 'country/index.html')

def detail(request):
    print("---------detail()-------------")
    try:
        form = request.POST['selectedCity']
        print('입력된 값 : ', form)
        cityList = form.split(',')
        print('변환된 값 : ', cityList)

    except(KeyError):
        return render(request, 'country/detail.html',{'error_message' : '값 오류입니다.'} )


    dong = dong_data.objects.all()
    
    dong = dong.filter(city__in= cityList )
    context = {'dong':dong}
    return render(request, 'country/detail.html', context)



def result(request):
    print("---------result()-------------")

    return render(request, 'country/result.html')

# 인덱스 화면에서 값 입력 받고 시별로 정렬 한 후 디테일로 넘기는 함수(세션 유지)


# 디테일 화면에서 값 입력 받고 결과창으로 넘기는 함수


# 로직 함수 결과 받아서 결과 창에서 지도로 시각화해 보여주는 함수
