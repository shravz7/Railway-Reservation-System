from django.shortcuts import render
from MyApp.models import Reservation
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
 
def reservation(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        medicalpractitioner = request.POST.get('medicalpractitioner')
        seniorcitizen = request.POST.get('seniorcitizen')
        trainno = request.POST.get('trainno')
        trainname = request.POST.get('trainname')
        classname = request.POST.get('classname')
        noofseat = request.POST.get('noofseat')
        stationfrom = request.POST.get('stationfrom')
        stationto = request.POST.get('stationto')
        reservation=Reservation(name=name, age=age, gender=gender, medicalpractitioner=medicalpractitioner, seniorcitizen=seniorcitizen,trainno=trainno, trainname=trainname, classname=classname, noofseat=noofseat, stationfrom=stationfrom, stationto=stationto)
        reservation.save()
        messages.success(request, 'Registration Successfull ')
    return render(request, 'reservation.html')

# def cancellation(request):
#     return render(request, 'cancellation.html')
