
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def home(request):
    context = {}
    return render(request, 'home.html', context)
    

def detail(request):
    context = {}
    return render(request, 'detail.html', context)


def them(request):
    context = {}
    return render(request, 'them.html', context)


def sua(request):
    context = {}
    return render(request,'sua.html' , context)


def xoa(request):
    return render(request, 'xoa.html', {'xoa': xoa})


def dangnhap(request):
    context = {}
    return render(request, 'dangnhap.html', context)


def dangxuat(request):
    logout(request)
    return redirect('home')
