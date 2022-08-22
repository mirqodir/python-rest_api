from django.urls import path
from .views import UserView,UserDetail, ClientView, ClientDetail,AuthUserRegistrationView

urlpatterns  = [
	path('users/',UserView.as_view()), 
	path('user/<int:pk>/',UserDetail.as_view()),

	path('clients/',ClientView.as_view()), 
	path('client/<int:pk>/',ClientDetail.as_view()),
	path('register/',AuthUserRegistrationView.as_view()),
	]