from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.
# def home(request):
#     pizzas_str = ""
#     pizzas = Pizza.objects.all()
#     pizzas_names = list(pizza.nom for pizza in pizzas)
#     pizzas_price = list(pizza.prix for pizza in pizzas)
#     for i in range(len(pizzas)):
#         pizzas_str += pizzas_names[i] + " - " + str(pizzas_price[i]) + "€, "
#     print(pizzas_str)
#     return HttpResponse("My pizzas")

def index(request):
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, "menu/index.html", {"pizzas":pizzas})
