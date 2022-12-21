from django.urls import path
from . import views
urlpatterns = [
    path('',views.schoolLog,name="schoolLog"),
    path('schoolverify/',views.schoolsverify,name="schoolsverify"),
    path('schoolreg/',views.schoolreg,name="schoolregistration"),
    path('schoolindex/',views.schoolindex,name="schoolindex"),
    path('admissionrequests/',views.admissionreqpage,name="admissionreqpage"),
    path('admissionrequests/confstudentschoolregpermanent/<int:studentid>/',views.admissionconfirm,name="admissionconfirm"),
    path('admissionrequests/deltempstudentschoolregreq/<int:studentid>/',views.admissiondecline,name="admissiondecline"),
    path('schoolreg/tempschoolreg/',views.tempschoolsreg,name="tempschoolsreg"),
    # path('studentprofile/',views.studentprofiles,name="studentprofiles"),
    path('studentresultupload/',views.studentresultsupload,name="studentresultsupload"),
    path('studentresultupload/studentresultsuploadsave/',views.studentresultsuploadsave,name="studentresultsuploadsave"),
    path('studentviewresult/',views.studentviewresults,name="studentviewresults"),
    path('studentprofile/',views.studentdetail,name="studentdetail"),
    
]
