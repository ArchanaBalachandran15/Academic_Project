from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Event, Booking, Category
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404



def home(request):
    # events = Event.objects.all()
    # categories = Category.objects.all()
    #  return render(request, 'events/home.html', {'events': events, 'categories': categories})
    return render(request, 'events/home.html')


def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def book_event(request, event_id):
    event = Event.objects.get(id=event_id)
    Booking.objects.create(user=request.user, event=event)
    messages.success(request, 'Booking successful!')
    return redirect('my_bookings')

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'events/booking_list.html', {'bookings': bookings})

def contact(request):
    if request.method == 'POST':
        # Save contact details
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        from .models import Contact
        Contact.objects.create(name=name, email=email, message=message)
        messages.success(request, 'Message sent successfully!')
    return render(request, 'events/contact.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'events/register.html', {'form': form})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})
