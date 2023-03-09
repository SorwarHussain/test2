from django.core.mail import EmailMessage,send_mail

from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from main import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token
# form youtube tutorial->Cryce Truly

from django.views import View
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse

# Create your views here.
def login(request):
      if request.method=='POST':
        user_name=request.POST['username']
        pass_word=request.POST['password']
        context={
                'user_name':user_name,
                'pass_word':pass_word
        }
        if User.objects.filter(username=user_name).exists():
          user=auth.authenticate(username=user_name,password=pass_word)
          my_user=User.objects.get(username=user_name)
          if user is not None:
             messages.success(request,"Login Successfully!") 
             auth.login(request,user)
             return redirect('home')
          elif my_user.is_active is False:
            messages.error(request,"We sent you an email to verify your account. Please confirm your email in order to activate your account.")
            return render(request,'authentication/login.html',context)
            # print("verify")return redirect('login')
          else:
            messages.error(request,"Invalid username/handle or password. Please try again.")
            return render(request,'authentication/login.html',context)
            #return redirect('login')
        else:
            messages.error(request,"Sorry! we didn't find any account this username. Please enter your correct username or if you haven't any account please create an account first!")
            return render(request,'authentication/login.html',context)
            #print("please create an account!")return redirect('signup')
      else:
       return render(request,'authentication/login.html')
def signup(request):
    if request.method=='POST':
        user_name=request.POST['user_name']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        context={
                'user_name':user_name,
                'email':email,
                'pass1':pass1
        }
        if pass1==pass2:
          if len(user_name)>15 or len(user_name)<4:
                 messages.error(request,"Username must be taken between 4 and 15 characters")
                 return render(request,'authentication/signup.html',context)
                 #return redirect('register',context)
          elif not user_name.isalnum():
                 messages.error(request,"Username should only contain letters and numbers")
                 return render(request,'authentication/signup.html',context)
                 #return redirect('register',context)
          elif User.objects.filter(username=user_name).exists():
               messages.error(request,"This username is already taken.")
               return render(request,'authentication/signup.html',context)
                 #return redirect('register',context)
          elif User.objects.filter(email=email).exists():
             messages.error(request,"This email is already taken.")
             return render(request,'authentication/signup.html',context)
                 #return redirect('register',context)
          elif len(email)>80 :
                 messages.error(request,"Please give a valid email.")
                 return render(request,'authentication/signup.html',context)
                 #return redirect('register',context)
          elif len(pass1)<6 :
                 messages.error(request,"This password is too short. It must contain at least 6 characters.")
                 return render(request,'authentication/signup.html',context)
                 #return redirect('register',context)
          elif len(pass1)>100 :
                 messages.error(request,"Please give a correct password.")
                 return render(request,'signup.html',context)
                 #return redirect('register',context)
          else:
            user=User.objects.create_user(username=user_name,password=pass1,email=email)
            user.is_active=False
            user.save()
            messages.success(request,"Thanks for creating an account. We have sent you a confirmation email,please confirm your email in order to activate your account.")
            #Welcome Email
            subject="Welcome to Darul Uloom Madrasa -Login!!"
            message="Hello "+user.username+"!!\n"+"Welcome to Darul Uloom Madrasa \nThank you for visiting our website \nWe have also sent you a confirmation email, please confirm your email address in order to activate your account.\nThanking You\n DarulUloomMadrasa.org"
            from_email=settings.EMAIL_HOST_USER
            to_list=[user.email]
            send_mail(subject,message,from_email,to_list,fail_silently=True)
            #Confirmation Email
            current_site=get_current_site(request)
            email_subject="Confirm your email @ Darul Uloom Madrasa Login"
            message2=render_to_string('authentication/email_confirmation.html',{
                'name':user.username,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':generate_token.make_token(user),
            })
            email=EmailMessage(
                email_subject,
                message2,
                settings.EMAIL_HOST_USER,
                [user.email],
            )
            email.fail_silently=True
            email.send()
            return redirect("login")

            
        else:
             messages.error(request,"Password not matching.")
             return render(request,'authentication/signup.html',context)
     
        #
        #welcome email
       

    else:
     return render(request,'authentication/signup.html')
def activate(request,uidb64,token):
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None
    
    if user is not None and generate_token.check_token(user,token):
        user.is_active=True
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        user.save()
        auth.login(request,user)
        return redirect('home')
    else:
        return render(request,'authentication/activation_failed.html')
class RequestPasswordResetEmail(View):
    def get(self,request):
        return render(request,'authentication/reset-password.html')
    def post(self,request):
        email=request.POST['email']
        user=User.objects.filter(email=email)
        current_site=get_current_site(request)
        #print(user[0])
        context={
                'email':email,
        }
        if user.exists():
            #print("Yea your email is eixit")
            email_contents={
                'user':user[0],
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user[0].pk)),
                'token':PasswordResetTokenGenerator().make_token(user[0]),
            }
            email_subject="Password reset Instruction"
            link=reverse('reset-user-password',kwargs={
                'uidb64':email_contents['uid'],
                'token':email_contents['token']
            })
            reset_url= 'http://'+current_site.domain+link
            email=EmailMessage(
                email_subject,
                'Hi, \n\n Please click the link below to reset your password \n'+reset_url,
                settings.EMAIL_HOST_USER,
                [email],
            )
            email.send(fail_silently=False)
            messages.success(request,"We have sent you a verificatio email. Please check your email.")
            return redirect("login")
        else:
            #print("oh! no your given email is not exists")
            messages.error(request,"Please give your Email.")
            return render(request,'authentication/reset-password.html',context)

class CompletPasswordReset(View):
    def get(self,request,uidb64,token):
        context={
            'uidb64':uidb64,
            'token':token
        }
        try:
            user_id=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=user_id)
            if not PasswordResetTokenGenerator().check_token(user,token):
             messages.error(request,"Password link is invalid. Please login with your new password.")
             return redirect('login')
        except:
            pass
        return render(request,'authentication/set-new-password.html',context)
                  #pass
        #print("print uidb64->")
        #print(token)
       # return redirect("login")
        
    def post(self,request,uidb64,token):
         pass1=request.POST['pass1']
         pass2=request.POST['pass2']
         context={
            'uidb64':uidb64,
            'token':token,
        }
         if pass1==pass2:
            if len(pass1)<6 :
                 messages.error(request,"This password is too short. It must contain at least 6 characters")
                 return render(request,'authentication/set-new-password.html',context)
            elif len(pass1)>80 :
                 messages.error(request,"Please give a correct password.")
                 return render(request,'authentication/set-new-password.html',context)
            else:
              try:
                user_id=force_str(urlsafe_base64_decode(uidb64))
                user=User.objects.get(pk=user_id)
                user.set_password(pass1)
                user.save()
                messages.success(request,"Your password reset successfully. Please login with your new password.")
                return redirect('login')
              except:
                  messages.error(request,"Something went wrong. Please try again.")
                  return render(request,'authentication/set-new-password.html',context)
         else: 
              messages.error(request,"Password not matching.")
              return render(request,'authentication/set-new-password.html',context)
         
#def forgot(request):
 #   return render(request,'authentication/forgot.html')
