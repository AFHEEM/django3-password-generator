from django.shortcuts import render
import random


def home(request):
    """
    Home page - this function is called when no URL is provided
    :return:
    """
    return render(request, 'generator/home.html')


def password(request):
    """
    Gets password generated from Home form
    :param request:
    :return:
    """
    characters = list('abcdefghijklmnopqrstuvwxyz')
    thepassword = ''
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get('numbers'):
        characters.extend(list("1234567890"))
    if request.GET.get('special'):
        characters.extend(list("!@#%$^%*^((#)*)(&()"))

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    """
    Shows About page
    :param request:
    :return:
    """
    about_me = "IAM THE GAME !!!"
    return render(request, 'generator/about.html', {'about': about_me})
