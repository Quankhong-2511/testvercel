from django.urls import path, include
from . import views


urlpatterns = [
    
    path('dangnhap/', views.dangnhap, name='dangnhap'),
    path('dangxuat/', views.dangxuat, name='dangxuat'),
    
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    
    path('them/', views.them, name='them'),
    path('xoa/', views.xoa, name='xoa'),
    path('sua/', views.sua, name='sua'),

]
