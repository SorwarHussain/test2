from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from requests import request
# Create your views here.

@login_required
def general(request):
    return render(request,'settings/general/general_wrap.html')
@login_required
def delete_account(request):
    if request.method == 'POST':
        user=User.objects.get(id=request.user.id)
        user.delete()
        messages.success(request,"Your account successfully deleted.")  
        return redirect('home') 
   
    return render(request,'settings/general/confirm_delete_account_wrap.html')
@login_required
def change_password(request,id):
    #print(type(request.user.id))
    #print(type(id))
    if request.method == 'POST' and request.user.id==id:
        #print(request.user)
        old_psw=request.POST['psw1']
        new_psw1=request.POST['psw2']
        new_psw2=request.POST['psw3']
        user_auth=auth.authenticate(username=request.user,password=old_psw)
        context={
                'old_psw':old_psw,
                'new_psw1':new_psw1,
                'new_psw2':new_psw2
            }
        if user_auth is not None:
            if new_psw1==new_psw2:
                if len(new_psw1)<6 :
                  messages.error(request,"This password is too short. It must contain at least 6 characters")
                elif len(new_psw1)>80 :
                  messages.error(request,"Please give a correct password.")
                else:
                  user=User.objects.get(id=id)
                  user.set_password(new_psw1)
                  user.save()
                  messages.success(request,"Your password successfully updated. Please Login again.")  
                  return redirect('login')  
            else:
               messages.error(request,"Your new password not matching.")
            
        else:
            messages.error(request,"Invalid current password.Please try again.")
        return render(request,'settings/password/password_wrap.html',context)
    else:   
     return render(request,'settings/password/password_wrap.html')

        
            


    