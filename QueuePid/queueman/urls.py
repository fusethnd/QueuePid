from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.qhome,name='qhome'),
    path('wallet/',views.wallet,name='qwallet'),
    path('history/',views.history,name='qhistory'),
    path('profile/',views.profile,name='qprofile'),
    path('profile/edit',views.edit_profile,name='qedit')
]