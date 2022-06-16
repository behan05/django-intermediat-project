from .form import update
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from core.models import NewUserTB
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.paginator import Paginator


def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        phone = request.POST.get('num')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        if pwd == cpwd:       
            db = NewUserTB(fname=fname,lname=lname,uname=uname,email=email,phone=phone,password=pwd,cnf_password=cpwd)
            db.save()
        else:
            return HttpResponseRedirect('/')    
        subject = f'Hello {fname} {lname} This is a Greeting Message From BehanSingh.com'
        message = render_to_string('email_template.html')
        message_content = strip_tags(message)
        from_mail = settings.EMAIL_HOST_USER
        recipient = [email]
        email = EmailMultiAlternatives(subject,message_content,from_mail,recipient)
        email.attach_alternative(message,'text/html')
        email.send()
        return HttpResponse(f'Thank You mr./mrs {fname}')
    
    return render(request, 'signup.html')


def showdb(request):
    db = NewUserTB.objects.all().order_by('id')
    pagination = Paginator(db,8)
    page_num = request.GET.get('page')
    main = pagination.get_page(page_num)
    return render(request,'show_data.html',{'data':main})

def delete(request,u_id):
    if request:
        all_db = NewUserTB.objects.get(pk=u_id)
        all_db.delete()
        return HttpResponseRedirect('/') 
        
def edit(request,u_id):
    if request.method == 'POST':
        all_db = NewUserTB.objects.get(pk=u_id) 
        fm = update(request.POST,instance=all_db)
        if fm.is_valid:
           fm.save()
        return HttpResponseRedirect('/') 
    else:
        if request.method == 'GET':
            db = NewUserTB.objects.get(pk=u_id) 
            form = update(instance=db)
        return render(request,'update.html',{'form':form})      
            
            
            
         
          