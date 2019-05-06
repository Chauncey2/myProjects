from django.urls import path
from . import views

app_name='myapp'
urlpatterns=[
    path('',views.index,name='index'),
    path('normal/',views.nomepage,name='normal'),
    path('hidden/',views.hidden_sidebar,name='hidden'),
    path('fixed_sidebar/',views.fixed_sidebar,name='fixed_sidebar'),
    path('fixed_header/',views.fixed_header,name='fixed_header'),
]