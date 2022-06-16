from django.urls import path
from core import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('showdb/',views.showdb,name="showdb"),
    path('delete/<int:u_id>/',views.delete,name='delete'),
    path('update/<int:u_id>/',views.edit,name='update'),
]
