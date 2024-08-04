from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  peoples=[
    
      
    {"name":'sachin',"age":18},
    {"name":'lovish',"age":19},
    {"name":'anubhav',"age":20},
    {"name":'kaustubh',"age":21}
    
     ]



  return render(request,"index.html",context={'peoples':peoples})


def contact(request):
  vegetables=[
    {"name":"cucumber","rate":20,"weight":1},
    {"name":"tomato","rate":30,"weight":1},
    {"name":"potato","rate":40,"weight":1},
    {"name":"bhindi","rate":50,"weight":1},
    {"name":"loki","rate":60,"weight":1},
    {"name":"tuar dal","rate":70,"weight":1},
    {"name":"onion","rate":80,"weight":1},
    {"name":"lemon","rate":90,"weight":1},
    {"name":"green chili","rate":100,"weight":1}
    ]
  return render(request,"contact.html",context={'vegetables':vegetables})
  

  
