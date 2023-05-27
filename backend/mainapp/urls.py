from django.urls import path,include ,re_path
from . import views

urlpatterns = [
    path('login',views.LoginView.as_view()),
    path('signin',views.SignInView.as_view()),
    path('createpost',views.CreatPostView.as_view()),
]
