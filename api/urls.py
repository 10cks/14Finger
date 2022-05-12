from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('user', views.UserRegisterView.as_view(), name='register'),
    path('user/login', views.UserLogin.as_view(), name='login'),
    path('user/logout', views.UserLogout.as_view(), name='logout'),
    path('user/rank', views.UserRankView.as_view(), name='user_rank'),
    path('factory', views.FactoryMultiHandle.as_view(), name='factory'),
    path('app', views.AppMultiHandle.as_view(), name='app'),
    path('finger', views.FingerMultiHandle.as_view(), name='finger_multi'),
    path('finger/single', views.FingerSingleHandle.as_view(), name='finger_single'),
    path('finger/single/query', views.FingerSingleQuery.as_view(), name='finger_single_query'),
    path('finger/batch/query', views.FingerBatchQuery.as_view(), name='finger_batch_query'),
    path('finger/batch/action', views.FingerBatchAction.as_view(), name='finger_batch_action'),
    path('admin/finger', views.FingerMultiAdminHandle.as_view(), name='finger_multi_admin'),
    path('admin/finger/single', views.FingerSingleAdminHandle.as_view(), name='finger_single_admin'),
]