import datetime
import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from .models import User, Book_ground, Admin,Event


def index(request):
    return render(request,'scm/index.html')
def about(request):
    return render(request,'scm/about.html')
def user_reg(request):
    return render(request,'scm/user_reg.html')
def user_test(request):
    if request.method=='POST':
        name=request.POST.get('uname')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        password=request.POST.get('password')
        contact=request.POST.get('contact')
        record=User(name=name,email=email,gender=gender,password=password,contact=contact)
        record.save()
        return render(request,'scm/user_login.html')

def user_login(request):
    if 'u_name' in request.session:
        param={'name':request.session['u_name']}
        return render(request,'scm/user_home.html',param)

    return render(request,'scm/user_login.html')

def user_check(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        try:
            user=User.objects.get(name=uname)
            if user.password==password:
                request.session['u_name']=uname
                return userhome(request)
            else:
                param={"msg":"Password Does not match"}
                return render(request,'scm/user_login.html',param)

        except Exception as e:
            param={"msg":"This unsername is not exist..."}
            return render(request,'scm/user_login.html',param)

def userhome(request):
    if 'u_name' in request.session:

        uname=request.session.get('u_name')
        param={"name":uname}
        return render(request,'scm/user_home.html',param)
    else:
        param={"status":"you need to Login"}
        return render(request,'scm/user_login',param)

def ground_booking(request):
    if 'u_name' in request.session:
        param={'date':datetime.date.today}
        return render(request,'scm/ground_booking.html',param)

    else:
        param={"status":"You need to Login.....!!!!"}
        return render(request,"scm/user_reg",param)
def data_groundbooking(request):
    if request.method == 'POST':
        date=request.POST.get('date')
        time=request.POST.get('time')
        try:
            book=Book_ground.objects.get(date=date)
            param={'status':"Please Select Another Date....."}
            return render(request,"scm/ground_booking.html",param)
        except Exception as e:
            user=User.objects.get(name=request.session.get('u_name'))
            book=Book_ground(uid=user.uid,name=user.name,date=date,time=time,mobile=user.contact)
            book.save()
            param={'status':"Booking Successfull....."}
            return render(request,'scm/user_home.html',param)
    else:
        param={'msg':"something Wrong.....!!!"}
        return render(request,"scm/ground_booking.html",param)

def admin_login_page(request):
    if 'a_name' in request.session:
        param={'name':request.session.get('a_name')}
        return render(request,'scm/admin_home.html',param)
    return render(request,'scm/admin_login.html')

def admin_check(request):
    if request.method == 'POST':
        aname = request.POST.get('aname')
        password = request.POST.get('password')
        try:
            add = Admin.objects.get(name=aname)
            if add.password == password:
                request.session['a_name'] = aname
                return adminhome(request)
            else:
                param = {"msg": "Password Does not match"}
                return render(request, 'scm/admin_login.html', param)

        except Exception as e:
            param = {"msg": "This unsername is not exist..."}
            return render(request, 'scm/admin_login.html', param)


def adminhome(request):
    if 'a_name' in request.session:

        aname = request.session.get('a_name')
        param = {"name": aname}
        return render(request, 'scm/admin_home.html', param)
    else:
        param = {"status": "you need to Login"}
        return render(request, 'scm/admin_login', param)

def admin_booking(request):
    if 'a_name' in request.session:
        booking=Book_ground.objects.all()
        param={'data':booking}
        return render(request,'scm/admin_booking.html',param)
    else:
        param = {"status": "you need to Login"}
        return render(request, 'scm/admin_login.html', param)


def admin_event(request):
    if 'a_name' in request.session:
        event=Event.objects.all()
        param={"data":event}
        return render(request,'scm/admin_event.html',param)
    else:
        param = {"status": "you need to Login"}
        return render(request, 'scm/admin_login.html', param)


def add_event(request):
    if 'a_name' in request.session:
        param = {'date': datetime.date.today}
        return render(request,'scm/add_event.html',param)

    else:
        param = {"status": "you need to Login"}
        return render(request, 'scm/admin_login.html',param)

def db_add_event(request):
    if request.method=="POST":
        ename=request.POST.get('ename')
        edate=request.POST.get('edate')
        etime=request.POST.get('etime')
        eduration=request.POST.get('eduration')

        event=Event(name=ename,date=edate,time=etime,duration=eduration)
        event.save()
        request.session['event_status']={"msg":"Event Added Successfully"}
        return admin_event(request)
    else:
        return admin_event(request)

def admin_logout(request):
    if 'a_name' in request.session:
        del request.session['a_name']
        return render(request, 'scm/admin_login.html',)
    else:
        param = {"status": "you need to Login"}
        return render(request, 'scm/admin_login.html', param)

def user_logout(request):
    if 'u_name' in request.session:
        del request.session['u_name']
        return render(request, 'scm/user_login.html',)
    else:
        param = {"status": "you need to Login"}
        return render(request, 'scm/user_login.html', param)


def show_event(request):
    if 'u_name' in request.session:
        event = Event.objects.all()
        param = {"data": event}
        return render(request, 'scm/show_event.html', param)
    else:
        param = {"status": "you need to Login"}
        return render(request, 'scm/user_login.html', param)


def event_delete(request):
    if 'a_name' in request.session:
        id=request.GET.get('eid')
        Event.objects.filter(eid=id).delete()
        return admin_event(request)


    else:
        param = {"status": "you need to Login"}
        return render(request, 'scm/admin_login.html', param)


def mail_send(request):
    return render(request,'scm/email_form.html')


def email_check(request):
    email=request.POST.get('email')
    subject='forget password'
    otp=random.randint(100000, 999999)
    msg='OTP='
    msg+=str(otp)
    email_from=settings.EMAIL_HOST_USER
    to=(email,)
    send_mail(subject,msg,email_from,to)
    param={'otp':otp,'email':email}
    return render(request,'scm/enter_otp.html',param)

def otp_check(request):
    myotp=request.POST.get('myotp')
    emailid=request.POST.get('emailid')
    otp=request.POST.get('otp')
    if(myotp==otp):
        param={'email':emailid}
        return render(request,"scm/update_pass.html",param)
    else:
        param={'otp':myotp,'email':emailid,'msg':"wrong otp"}
        return render(request,"scm/enter_otp.html",param)


def update_pass(request):
    password=request.POST.get('pass')
    myemail=request.POST.get('emailid')
    user=User.objects.get(email=myemail)
    user.password=password
    user.save()
    return render(request,'scm/user_login.html')














