from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required 

from .models import Record

from django.contrib import messages

# Create your views here.

#Home Page
def home(request):
    
    return render(request, 'index.html')


#Register
def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully!")

            return redirect('login')
    context = {'form':form}

    return render(request, 'register.html', context=context)


#user login
def login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            #get method here is used to get the username and password entered by the user
            username = request.POST.get('username')
            password = request.POST.get('password')

            #authenticate if username and password entered by user are correct and exist in database
            user = authenticate(request, username=username, password=password)

            if user is not None: #Simply if user exists(lol)
                
                auth.login(request, user)

                return redirect('dashboard')

    context = {'form':form}

    return render(request, 'login.html', context=context)


#Dashboard

@login_required(login_url='login') #Allows only logged in users to access their dashboard
def dashboard(request):

    my_record = Record.objects.all()

    context = {'record':my_record}

    return render(request, "dashboard.html", context=context)



#Create or Add Record
@login_required(login_url='login')
def create_record(request):

    form = CreateRecordForm()

    if request.method == 'POST':

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form':form}

    return render(request, 'create-record.html', context=context)



#Update Record
@login_required(login_url='login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(request.POST, instance=record)

    if request.method == 'POST':

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect('dashboard')

    context = {'form':form}

    return render(request, 'update-record.html', context=context)


#View a single record
@login_required(login_url='login')
def view_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'view-record.html', context=context)



#Delerte a single record
@login_required(login_url='login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect('dashboard')

#User Logout
def logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("login")


