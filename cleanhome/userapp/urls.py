from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.signup_view.as_view(), name='signup_page'),
    path('login/',views.login_view.as_view(), name='login_page'),
    path('bookings/',views.bookings_view.as_view(), name='bookings_page'),
    path('confirm_booking/',views.confirm_booking_view, name='confirm_bookings_page'),
    path('delete_booking/<int:id>/',views.delete_booking_view, name='delete_booking'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('home/',views.home,name='home'),
    path('partner/',views.partners,name='partners'),
    path('booking_summary/<int:id>/', views.booking_summary, name='booking_summary_page'),
    path('show_booking/', views.show_booking_view, name='show_bookings_page'),
    path('logout/', views.user_logout, name='logout'),

]