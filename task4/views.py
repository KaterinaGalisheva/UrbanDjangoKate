from django.shortcuts import render

# Create your views here.
def index_cart(request):
    return render(request, 'fourth_task/cart.html')

def index_primary(request):
    return render(request, 'fourth_task/primary.html')

def index_store(request):
    isecream = ['вишневое', 'персиковое', 'шоколадное', 'крем-брюле']
    context = {'isecream' : isecream}
    return render(request, 'fourth_task/store.html', context)



