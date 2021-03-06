from django.urls import path
from . import views

app_name='country'

urlpatterns=[
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'), 
    path('result/', views.result, name='result')
]


'''
urlpatterns=[
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('ajaxreq/', views.ajaxRes, name='ajaxRes')
]

'''


