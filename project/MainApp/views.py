from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.decorators import login_required
from MainApp.models import Attendance

# Create your views here.
@login_required(login_url = "login")
def home(request):
    user = User.objects.get(id = request.user.id)
    if request.method == "POST":
        time = request.POST.get("time")
        location = request.POST.get("location")
        attendance = Attendance.objects.create(user = user , time = time , location = location)
        return JsonResponse({"status": "success", "message": "Data received"})
    return render(request, "home.html", {"user": user.username})

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username = username, email = email, password = password)
        login(request , user)
        return redirect("/")
    return render(request, "signup.html")

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request , user)
            return redirect("/")
    return render(request, "login.html")

def attendances(request):
    attendance = Attendance.objects.all().order_by("-time_created")
    return render(request , "attendaces.html", {"attendance": attendance})