from django.shortcuts import render

def index(request):
    return render (request,'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def booking(request):
    return render(request, 'core/booking.html')

def contact(request):
    return render(request, 'core/contact.html')

def services(request):
    return render(request, 'core/service.html')

def rooms(request):
    return render(request, 'core/room.html')