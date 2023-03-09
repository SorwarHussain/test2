from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('activate/<uidb64>/<token>', views.activate,name="activate"),
    path('',views.login,name="login"),
     path('signup/',views.signup,name="signup"),
     path('logout/',auth_views.LogoutView.as_view(),name='logout'),
      #for social. add.
    path('social-auth/',include('social_django.urls',namespace='social')),
     

      #password reset start
    path('request-reset-link',views.RequestPasswordResetEmail.as_view(),name="request-password"),
    path('set-new-password/<uidb64>/<token>', views.CompletPasswordReset.as_view(),name="reset-user-password"),

]