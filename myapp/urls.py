from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('gallery/',views.gallery,name='gallery'),
    path('logout/',views.logout,name='logout'),
    path('doctor_profile/',views.doctor_profile,name='doctor_profile'),
    path('change_password/',views.change_password,name='change_password'),
    path('doctor_home/',views.doctor_home,name='doctor_home'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('new_password/',views.new_password,name='new_password'),
    path('verifyotp/',views.verifyotp,name='verifyotp'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('doctors/',views.doctors,name='doctors'),
    path('doctor_detail/<int:pk>/',views.doctor_detail,name='doctor_detail'),
    path('book appointment/<int:pk>/',views.book_appointment,name='book_appointment'),
    path('myappointment/',views.myappointment,name='myappointment'),
    path('patient_cancel_appointment/<int:pk>',views.patient_cancel_appointment,name='patient_cancel_appointment'),
    path('health_profile/',views.health_profile,name='health_profile'),
    path('doctor_appointment/',views.doctor_appointment,name='doctor_appointment'),
    path('doctor_approve_appointment/<int:pk>',views.doctor_approve_appointment,name='doctor_approve_appointment'),
    path('doctor_complete_appointment/<int:pk>',views.doctor_complete_appointment,name='doctor_complete_appointment'),
    path('doctor_cancel_appointment/<int:pk>',views.doctor_cancel_appointment,name='doctor_cancel_appointment'),
    
]  


