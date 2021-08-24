from datetime import datetime, timedelta

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from .forms import Signup_Form, Login_Form, Bookings_Form
from .models import Signup, Bookings


def home(request):
    request = request
    template_name = 'userapp/home.html'
    return render(request, template_name)


class signup_view(View):
    def post(self,request):
        if request.method=='POST':
            fm = Signup_Form(request.POST)
            if fm.is_valid():
                name = fm.cleaned_data['name']
                mobile = fm.cleaned_data['mobile']
                email = fm.cleaned_data['email']
                # request.session['name'] = name
                # request.session['mobile'] = mobile
                # request.session.set_expiry(600)
                #response = render(request, 'userapp/login.html')
                # response.set_cookie('movie_name', movie_name, expires=datetime.utcnow()+timedelta(days=2))
                #response.set_signed_cookie('product', prod, salt='product',expires=datetime.utcnow() + timedelta(days=2))
                obj = Signup(name=name, mobile=mobile, email=email)
                obj.save()
                return HttpResponseRedirect('/login')

    def get(self, request):
        fm = Signup_Form()
        return render(request,'userapp/signup.html',{'form':fm})


class login_view(View):
    def post(self,request):
        if request.method=='POST':
            fm = Login_Form(request.POST)
            if fm.is_valid():
                mobile = fm.cleaned_data['mobile']
                try:
                    check_mobile = Signup.objects.get(mobile=mobile)
                    # fm2 = Bookings_Form()
                    # return render(request, 'userapp/bookings.html', {'form': fm2,'check_mobile':check_mobile})
                    return HttpResponseRedirect('/bookings')
                except:
                    msg = '* Entered Mobile number is not registered'

                    #return HttpResponse("Entered Mobile number is not registered")

                    return render(request, 'userapp/Login.html',{'form':fm,'msg':msg})

    def get(self, request):
        fm = Login_Form()
        return render(request,'userapp/login.html',{'form':fm})



class bookings_view(View):
    def post(self,request):
        if request.method=='POST':
            fm = Bookings_Form(request.POST)
            if fm.is_valid():
                user = fm.cleaned_data['user']
                type_of_home = fm.cleaned_data['type_of_home']
                persons = fm.cleaned_data['persons']
                address = fm.cleaned_data['address']
                zip_code = fm.cleaned_data['zip_code']
                request.session['name'] = user
                # request.session['mobile'] = mobile
                request.session.set_expiry(600)
                response = render(request, 'userapp/bookings.html')
                response.set_cookie('type_of_home', type_of_home, expires=datetime.utcnow()+timedelta(days=2))
                # response.set_signed_cookie('type_of_home', type_of_home, salt='type_of_home',expires=datetime.utcnow() + timedelta(days=2))
                obj = Bookings(user=user,type_of_home=type_of_home, persons=persons, address=address,zip_code=zip_code)
                obj.save()
                return HttpResponseRedirect('/confirm_booking')

    def get(self, request):
        fm = Bookings_Form()
        return render(request,'userapp/bookings.html',{'form':fm})

def confirm_booking_view(request):
    dt = Bookings.objects.all()
    return render(request, 'userapp/confirm_booking.html', {'form': dt})

def delete_booking_view(request,id):
    if request.method == 'GET':
        ord = Bookings.objects.get(pk=id)
        context = {'ord': ord}
        template = 'userapp/delete_booking.html'
        return render(request, template, context)

    elif request.method == 'POST':
        ord = Bookings.objects.get(pk=id)
        ord.delete()
        return HttpResponseRedirect('/confirm_booking')


def show_booking_view(request):
    dt = Bookings.objects.all()
    print(dt)
    return render(request, 'userapp/show_booking.html', {'form': dt})



def booking_summary(request,id):
    ord = Bookings.objects.get(pk=id)
    if ord.type_of_home == '1BHK':
        price = 800.00
        CGST = round(price / 9, 2)
        SGST = round(price / 9, 2)
        Total = price + CGST + SGST
        Total = round(Total, 2)

    elif ord.type_of_home == '2BHK':
        price = 1200.00
        CGST = round(price / 9, 2)
        SGST = round(price / 9, 2)
        Total = price + CGST + SGST
        Total = round(Total, 2)
    elif ord.type_of_home == 'Above 3BHK':
        price = 2000.00
        CGST = round(price / 9, 2)
        SGST = round(price / 9, 2)
        Total = price + CGST + SGST
        Total = round(Total, 2)
    elif ord.type_of_home == 'Garden':
        price = '10 per Sq/ft'
        CGST = 'NA'
        SGST = 'NA'
        Total = '10 per Sq/ft + GST(18%)'
    elif ord.type_of_home == 'Villa/Bunglow':
        price = '15 per Sq/ft'
        CGST = 'NA'
        SGST = 'NA'
        Total = '15 per Sq/ft + GST(18%)'
    elif ord.type_of_home == 'Office':
        price = '20 per Sq/ft'
        CGST = 'NA'
        SGST = 'NA'
        Total = '20 per Sq/ft + GST(18%)'
    return render(request, 'userapp/show_booking.html', {'fm': ord,'price':price,'CGST':CGST,'SGST':SGST,'Total':Total,})



def user_logout(request):
    #logout(request)
    return HttpResponseRedirect('/login')


def about(request):
    return render(request,'userapp/about.html')

def contact(request):
    return render(request,'userapp/contact.html')

def services(request):
    return render(request,'userapp/services.html')

def home(request):
    return render(request,'userapp/home.html')


def partners(request):
    return render(request,'partnerapp/partners.html')