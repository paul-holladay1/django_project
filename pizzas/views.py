from django.shortcuts import render,redirect
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('pizza_name')

    context = {'all_pizzas':pizzas}                 #key is variable name used in html file. Value is variable name usin in view

    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)

    toppings = Topping.objects.filter(pizza=p)

    reviews = Review.objects.filter(pizza=p)

    context = {'pizza':p, 'toppings':toppings, 'reviews':reviews} 

    return render(request, 'pizzas/pizza.html', context)

def new_review(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = ReviewForm()
    else:
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.pizza = pizza
            new_review.save()
            return redirect('pizzas:pizza',pizza_id=pizza_id)
    
    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/new_review.html', context)

    
