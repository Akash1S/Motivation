from django.http import HttpResponse
from django.shortcuts import render
from service.models import *
# All Service will come under this Application No need to Show services in
# any other app, This is Understandability purpose only..


def d_details(request):
    # return HttpResponse("All set")
    return render(request, 'services/director_details.html')


def seminar(request):
    return render(request, 'services/seminar.html')


def course_name(request):
    all_course = Course_Details.objects.all()
    return render(request,'services/course.html', {'all_course':all_course})


def gallery(request):
    return render(request, 'services/gallery.html')


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        Query_base(Name=name, Email=email, Mobile=mobile, Message=message).save()
        msg = '''Thank You For Selecting Us  We Will Come to You Soon'''
        return render(request, 'services/contact_us.html', {'msg': msg, 'type': 'queried'})
    return render(request, 'services/contact_us.html')