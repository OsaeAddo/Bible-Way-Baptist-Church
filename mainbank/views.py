from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import CustomerUserForm, CustomerForm
from .models import BankAccount, Customer



def home(request):
    return render(request, 'mainbank/home.html')


def customer_signup_view(request):
    form = CustomerUserForm
    customerForm = CustomerForm
    context = {
        'form':form,
        'customerForm': customerForm
    }
    if request.method == 'POST':
        form = CustomerUserForm(request.POST)
        customerForm = CustomerForm(request.POST)
        if form.is_valid and customerForm.is_valid:
            form = form.save()
            form.set_password(form.password)
            form.save()

            customerForm = customerForm.save(commit=False)
            customerForm.user = form
            customerForm.save()
        return redirect('login')

    return render(request, 'mainbank/signup.html', context)



@login_required(login_url="login")
def customer_dashboard(request):
    customer = Customer.objects.get(user_id=request.user.id)
    bankaccount = BankAccount.objects.all()
    context = {
        'customer': customer,
    }
    return render(request, 'mainbank/dashboard.html', context)


@login_required(login_url="login")
def customer_account(request):
    customer = Customer.objects.get(user_id=request.user.id)
    bankaccount = BankAccount.objects.all()
    context = {
        'customer': customer,
    }
    return render(request, 'mainbank/customer_account.html', context)



@login_required(login_url="login")
def customer_goldcard(request):
    customer = Customer.objects.get(user_id=request.user.id)
    context = {
        'customer': customer,
    }
    return render(request, 'mainbank/gold_card.html', context)


@login_required(login_url="login")
def customer_notifications(request):
    customer = Customer.objects.get(user_id=request.user.id)
    context = {
        'customer': customer,
    }
    return render(request, 'mainbank/notifications.html', context)

@login_required(login_url="login")
def customer_deposit_check(request):
    customer = Customer.objects.get(user_id=request.user.id)
    context = {
        'customer': customer,
    }
    return render(request, 'mainbank/deposit_check.html', context)


@login_required(login_url="login")
def payment(request):
    customer = Customer.objects.get(user_id=request.user.id)
    context = {
        'customer': customer,
    }
    return render(request, 'mainbank/payment.html', context)


@login_required(login_url="login")
def messages(request):
    customer = Customer.objects.get(user_id=request.user.id)
    context = {
        'customer': customer,
    }
    return render(request, 'mainbank/messages.html', context)


@login_required(login_url="login")
def transactions(request):
    customer = Customer.objects.get(user_id=request.user.id)
    context = {
        'customer': customer,
    }
    return render(request, 'mainbank/transactions.html', context)


@login_required(login_url="login")
def history(request):
    customer = Customer.objects.get(user_id=request.user.id)
    context = {
        'customer': customer,
    }
    return render(request, 'mainbank/history.html', context)

@login_required(login_url="login")
def settings(request):
    customer = Customer.objects.get(user_id=request.user.id)
    context = {
        'customer': customer,
    }
    return render(request, 'mainbank/settings.html', context)


@login_required(login_url="login")
def transfer(request):
    customer = Customer.objects.get(user_id=request.user.id)
    context = {
        'customer': customer,
    }
    return render(request, 'mainbank/transfer.html', context)


@login_required(login_url="login")
def transfer_pending(request):
    customer = Customer.objects.get(user_id=request.user.id)
    context = {
        'customer': customer,
    }
    return render(request, 'mainbank/transfer_pending.html', context)
