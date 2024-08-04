from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def receipes(request):

  if request.method=="POST":
     data=request.POST
     receipe_image=request.FILES.get('receipe_image')
     receipe_name=data.get('receipe_name')
     receipe_description=data.get('receipe_description')
     print(receipe_name)
     print(receipe_description)
     print(receipe_image)
     
     Receipe.objects.create(receipe_name=receipe_name, receipe_description=receipe_description,  receipe_image=receipe_image)
     return redirect('/receipes')
   
  queryset=Receipe.objects.all()
  context={'receipes':queryset}
  return render(request,'receipes.html',context)


def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        if receipe_image:
            queryset.receipe_image = receipe_image
        queryset.save()
        return redirect('/receipes/')

    context = {'receipe': queryset}
    return render(request,'update_receipe.html', context)



   


def delete_receipe(request,id):
   queryset=Receipe.objects.get(id=id)
   queryset.delete()
   return redirect('/receipes/')
     


def Login_page(request):
    if request.method == "POST":
      username = request.POST.get('user_name')
      password = request.POST.get('password')
      if not  User.objects.filter(username=username).exists():
         messages.error(request,'Invalid username')
         return redirect('/login/')
      user=authenticate(username=username,password=password)
      if user is None:
         messages.error(request,'Invalid password')
         return redirect('/login/')
      else:
         login(request,user)
         return redirect('/receipes/')


    return render(request,'login.html')



def Register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('user_name')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username is already taken")
            return redirect('register')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Registered Successfully")
        return redirect('register')

    return render(request, 'register.html')

      


   