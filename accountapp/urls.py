from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"

# 들어오고자 하는 경로: "127.0.0.1:8000/account/hello_world" <=> accountapp:hello_world

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create')
]