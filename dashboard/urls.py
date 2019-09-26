from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('attendance/', views.tracking, name='attendance'),
    path('lreqform/', views.leave, name='leaveform'),
    path('lrequest/', views.RQST, name='rqust'),
    path('report/', views.report, name='report'),
    url('^(?P<question_id>\d+)/approve/$', views.Approve, name='approve'),
    url('^(?P<question_id>\d+)/reject/$', views.Reject, name='reject'),
    path('reset/', views.Reset, name='reset'),
    path('report/jtest/', views.jsn, name='jsn'),
    path('create/', views.signup, name='create_user'),
    path('update/', views.update, name='update_user'),
    path('edit_remove/', views.edit_remove, name='edit_remove'),
    url('^(?P<user_id>\d+)/edit/$', views.pupdate, name='pupdate'),
]
