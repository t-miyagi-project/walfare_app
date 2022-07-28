from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    #ユーザー作成
    path('create/', views.UserCreateView.as_view(), name="create"),
    path('profile/', views.UserProfileView.as_view(), name="profile"),
    path('change/', views.UserChangeView.as_view(), name="change"),
]