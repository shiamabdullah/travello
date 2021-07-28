from travello.models import Destination
from django.shortcuts import render
from .models import Destination

def index(request):
    des1= Destination()
    des1.name='tangail'
    des1.des='amr sohor'
    des1.price='9000'
    des1.img='destination_1.jpg'
    des1.offer= False

    des2= Destination()
    des2.name='dhaka'
    des2.des='amr sohor'
    des2.price='19000'    
    des2.img='destination_2.jpg'
    des2.offer= True

    dests=[des1, des2]

    return render(request, "index.html",{'dests':dests})