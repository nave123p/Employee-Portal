from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('login/', authview.LoginView.as_view(redirect_authenticated_user=True), name='login'), 
    path('logout/', authview.LogoutView.as_view(), name='logout'),
    path('', authview.LoginView.as_view(redirect_authenticated_user=True), name='login'),
]