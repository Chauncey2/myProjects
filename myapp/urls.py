from django.urls import path
from . import views

app_name='myapp'
urlpatterns=[
    path(r'',views.index,name='index'),

    path(r'normal/',views.nomepage,name='normal'),
    path(r'hidden/',views.hidden_sidebar,name='hidden'),
    path(r'fixed_sidebar/',views.fixed_sidebar,name='fixed_sidebar'),
    path(r'fixed_header/',views.fixed_header,name='fixed_header'),
    path(r'detail/',views.detail,name='detail_page'),
    # 测试页面
    path(r'test/',views.test,name='test'),
]