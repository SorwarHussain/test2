from django.urls import path
from . import views
urlpatterns = [
   path("general/",views.general,name="general"),
   path('<int:id>/change-password/', views.change_password, name='change_password'),
   path("delete-account/",views.delete_account,name="delete_account"),
]