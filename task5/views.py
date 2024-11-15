from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm


# Create your views here.
def sign_up_by_html(request):
    users = ['Анастасия', 'Екатерина', 'Никита', 'Дмитрий', 'Кирилл', 'Мария', 'Павел']
    info = {}
    context = {'info':info}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'fiveth_task/registration.html', context)
        if int(age) < 18:
            info['error'] = 'Вы несовершеннолетний'
            return render(request, 'fiveth_task/registration.html', context)
        if username in users:
            info['error'] = 'Такой пользователь уже существует'
            return render(request, 'fiveth_task/registration.html', context)
        else:
            return HttpResponse("Регистрация прошла успешно!")
            
    return render(request, 'fiveth_task/registration.html')


      
def sign_up_by_django(request):
    users = ['Анастасия', 'Екатерина', 'Никита', 'Дмитрий', 'Кирилл', 'Мария', 'Павел']
    info = {}
    context = {'info':info}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = request.POST.get('age')

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'fiveth_task/registration.html', context)
            if int(age) < 18:
                info['error'] = 'Вы несовершеннолетний'
                return render(request, 'fiveth_task/registration.html', context)
            if username in users:
                info['error'] = 'Такой пользователь уже существует'
                return render(request, 'fiveth_task/registration.html', context)
            else:
                return HttpResponse("Регистрация прошла успешно!")
    else:
        form = RegistrationForm()     
    return render(request, 'fiveth_task/registration.html', {'form':form})




  
        
    
  
      

