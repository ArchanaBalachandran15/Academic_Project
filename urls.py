from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('book/<int:event_id>/', views.book_event, name='book_event'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register_user, name='register'),
    path('login/', LoginView.as_view(template_name='events/login.html', next_page='home'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('events/', views.event_list, name='event_list'),

]
