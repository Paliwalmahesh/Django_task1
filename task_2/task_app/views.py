from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile



def register(request):
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        ph_no = request.POST['P_number']
        email = request.POST['email']
        gender = request.POST['gender']
        password = request.POST['password']
        try:
            user = User.objects.get(username=email)
            return HttpResponse('<h2>User exists</h2>')
        except User.DoesNotExists:
            user = User.objects.create_user(username=email, password=password)
            user.save()
            return redirect('search')
    else:
       return render(request, 'task_app/register.html')

def search_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            profile = UserProfile.objects.get(email=email)
            return render(request, 'task_app/info.html', {'profile': profile, 'message': 'Found user!'})
        except UserProfile.DoesNotExist:
            return render(request, 'task_app/info.html', {'message': 'Sorry no user with the entered email found'})

    else:
        return render(request, 'task_app/search.html')


# Create your views here.
