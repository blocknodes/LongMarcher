from django.forms import modelform_factory
from django import forms
from .models import Order
from django.shortcuts import render, redirect 
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

# Create your views here.


def index(request):
    orders = Order.objects.all()
    paginator = Paginator(orders, 2)
    page_num = request.GET.get('page')
    page_objs = paginator.get_page(page_num)
    context = {'orders': page_objs}
    return render(request, 'orderManager/index.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'orderManager/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def createOrder(request):
    OrderForm = modelform_factory(Order, exclude=('create_by',), widgets={'deliver_at':forms.SelectDateWidget()})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            print('form save')
            order = form.save(commit=False)
            order.create_by = request.user
            order.save()
        return redirect('home')

    form = OrderForm()
    print(form)
    context = {'form': form}
    return render(request, 'orderManager/order_form.html', context)


