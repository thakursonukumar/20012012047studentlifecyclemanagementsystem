from django.urls import path
from . import views
urlpatterns = [
    path('',views.collegeLog,name="collegeLog"),
]
