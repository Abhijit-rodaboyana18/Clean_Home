from django.contrib import messages

from django.shortcuts import render
from.models import Partners
from.forms import Partner_form
from django.views.generic.base import TemplateView, View
# from django.contrib import messsages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    return render(request,'home.html')




class Partners_view(View):

    def get(self,request):
        fm = Partner_form()
        return render(request,'partnerapp/partners.html',{'form':fm})

    def post(self,request):
        if request.method == 'POST':
            fm = Partner_form(request.POST)
            print(fm)
            if fm.is_valid():
                nm = fm.cleaned_data['name']
                ad = fm.cleaned_data['aadhaar']
                em = fm.cleaned_data['email']
                mb = fm.cleaned_data['mobile']
                pro = fm.cleaned_data['profession']
                ex = fm.cleaned_data['experience']
                sl = fm.cleaned_data['salary']
                dt = Partners(name=nm,aadhaar=ad,email=em,mobile=mb,profession=pro,experience=ex,salary=sl)
                dt.save()
                messages.success(request, "Data inserted successfully")
                content = f'{request.user} Clean home'
                to = em
                send_mail(
                    "cleaning",
                    content,
                    settings.EMAIL_HOST_USER,
                    [to]
                )


                return render(request, 'partnerapp/home.html')





