from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='Index'),
    path('Register/',views.Register,name='Register'),
    path('Registration/',views.Registration,name='Registration'),
    path('Login/',views.Login,name='Login'),
    path('Home/',views.Home,name='Home'),
    path('Logout/',views.Logout,name='Logout'),
    path('findAccount/',views.findAccount,name='findAccount'),
    path('sendDetails/',views.sendDetails,name='sendDetails'),
    path('addAccount/',views.addAccount,name='addAccount'),
    path('deleteAccount/',views.deleteAccount,name='deleteAccount'),
    path('updateAccount/',views.updateAccount,name='updateAccount'),
    path('updateIt/',views.updateIt,name='updateIt'),
    path('getBankAccountDetails/',views.getBankAccountDetails,name='getBankAccountDetails'),
    path('addBankAccount/',views.addBankAccount,name='addBankAccount'),
    path('deleteBankAccount/<int:aid>/',views.deleteBankAccount,name='deleteBankAccount'),
]
