from django.urls import path
from . import views

urlpatterns = [
	path('cart/', views.carts),
	path('store/',views.store),
	path('checkout/',views.checkout)

]