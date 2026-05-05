
from django.urls import path
from .import views

urlpatterns = [
    path('signin',views.sign_in,name="signin"),
    path('signup/', views.sign_up,name="signup"),
    path('signout/',views.sign_out,name="signout"),
    path('',views.home,name="home"),
    path('calc/',views.calc),
    path('calc/add',views.add),
    path('calc/sub',views.sub),
    path('calc/mult',views.mult),
    path('calc/div',views.div),
    path('appointment',views.appoin, name="appointment")
]