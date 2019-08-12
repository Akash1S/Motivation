from django.http import HttpResponse
from django.shortcuts import render
import re
# Project starting date is 31st of May.
from testapp.models import User_Model


def home(request):
    return render(request, 'home.html', {'type': 'Home_Page'})


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_check = User_Model.objects.filter(Email=email)
        if user_check:
            user_check = User_Model.objects.get(Email=email, Password=password)
            if not user_check:
                return render(request, 'user.html', {'n_password': 'Password is  not matching with the given email ID'})
            request.session['user_data'] = email
            return render(request, 'home.html', {'user': user_check, 'type': 'Confirmed'})
        return render(request, 'user.html', {'type': "Failed", 'n_email': 'Email id is not found'})
    return render(request, 'user.html', {'type': 'Login_Page'})


def registration(request):
    if request.method == "POST":
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        father_name = request.POST.get('father_name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        state = request.POST.get('state')
        qualification = request.POST.get('qualification')
        if (re.findall("^[9|8|7|6]", mobile)) == "9" or '8' or '7' or "6":
            if len(mobile) >= 10:
                validation = User_Model.objects.filter(Mobile=int(mobile))
                if not validation:
                    validation = User_Model.objects.filter(Email=email)
                    if not validation:
                        User_Model(First_Name=f_name, Last_Name=l_name, Mobile=mobile, Email=email,
                                   State=state, Qualification=qualification, Father_Name=father_name,
                                   Password=password).save()
                        return render(request, 'home.html', {'type': 'Confirmed', 'name': f_name})
                    msg = 'This Email is Already Register With Other User Enter A New Email'
                    return render(request, 'user.html', {'E_msg': msg, 'type': 'Registration_Page'})
                msg = 'This Mobile is Already Register With Other User Enter A New Number'
                return render(request, 'user.html', {'M_msg': msg, 'type': 'Registration_Page'})
            msg = 'This is Not a valid Number Please Enter A Valid Number'
            return render(request, 'user.html', {'M_msg': msg, 'type': 'Registration_Page'})
        msg = 'This is Not a valid Number Please Enter A Valid Number'
        return render(request, 'user.html', {'M_msg': msg, 'type': 'Registration_Page'})
    return render(request, 'user.html', {'type': 'Registration_Page'})


def about_The_Director(request):
    pass
