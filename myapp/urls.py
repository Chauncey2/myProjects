from django.urls import path
from . import views

app_name='myapp'
urlpatterns=[
    path(r'',views.index,name='index'),
    path(r'detail/',views.detail,name='detail_page'),
    # 测试页面
    path(r'test/',views.test,name='test'),
]