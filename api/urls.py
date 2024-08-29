from django.urls import path
from crud import views

urlpatterns = [
    path('get-transaction/', views.get_transaction)
]
