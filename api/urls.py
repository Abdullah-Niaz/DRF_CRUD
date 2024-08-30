from django.urls import path
from crud import views

urlpatterns = [
    path('get-transaction/', views.get_transaction),  # class-based view
    path('transaction/', views.TransactionAPI.as_view()),  # Class-based view
]
