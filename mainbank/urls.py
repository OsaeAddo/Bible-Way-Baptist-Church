from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', LoginView.as_view(template_name="mainbank/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="mainbank/home.html"), name="logout"),
    path("signup/", views.customer_signup_view, name="signup"),
    path("dashboard/", views.customer_dashboard, name="dashboard"),
    # Dashboard views
    path("dashboard/account", views.customer_account, name="account"),
    path("dashboard/goldcard", views.customer_goldcard, name="goldcard"),
    path("dashboard/notifications", views.customer_notifications, name="notifications"),
    path("dashboard/deposit-check", views.customer_deposit_check, name="deposit-check"),
    path("dashboard/payment", views.payment, name="payment"),
    path("dashboard/messages", views.messages, name="messages"),
    path("dashboard/transactions", views.transactions, name="transactions"),
    path("dashboard/history", views.history, name="history"),
    path("dashboard/settings", views.settings, name="settings"),
    path("dashboard/transfer", views.transfer, name="transfer"),
    path("dashboard/transfer-pending/", views.transfer_pending, name="transfer-pending"),
]
