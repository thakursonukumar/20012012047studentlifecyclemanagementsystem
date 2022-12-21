from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from school.models import tempschool,permanentschool,studentresult,studentpermanentschoolreg,studenttempschoolreg
from student.models import confstudent
from django.contrib import messages

# Create your views here.

def schoolLog(request):
    if request.session.has_key('schoolid'):
        return HttpResponseRedirect("http://127.0.0.1:8000/school/schoolindex/")
    else:    
        return render(request,"schoollog.html")
    
        

def schoolreg(request):
    if request.session.has_key('schoolid'):
        return HttpResponseRedirect("http://127.0.0.1:8000/school/schoolindex/")
    else:
        return render(request,'schoolreg.html')

def schoolsverify(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        schooldata=permanentschool.objects.filter(schoolemail=email,schoolpassword=password).count()
        if schooldata>0:
            school=permanentschool.objects.get(schoolemail=email)
            request.session['schoolid']=school.schoolnumber
            return HttpResponseRedirect("http://127.0.0.1:8000/school/schoolindex/")
        else:
            messages.success(request,"Please Check Email-id and Password")
            return HttpResponseRedirect("http://127.0.0.1:8000/school/")
    else:
        return HttpResponseRedirect("http://127.0.0.1:8000/school/")

def schoolindex(request):
    if request.session.has_key('schoolid'):
        schooldetail=permanentschool.objects.get(schoolnumber=request.session['schoolid'])
        return render(request,'schoolindex.html',{'schooldetails':schooldetail})
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/school/')

def tempschoolsreg(request):
    if request.method=="POST":
        sname=request.POST.get('schoolname')
        snumber=request.POST.get('schoolnumber')
        sphone=request.POST.get('schoolphone')
        semail=request.POST.get('schoolemail')
        saddress=request.POST.get('schooladdress')
        spassword=request.POST.get('password')
        tempsc=tempschool.objects.filter(schoolnumber=snumber).count()
        permsc=permanentschool.objects.filter(schoolnumber=snumber).count()
        if tempsc>0 or permsc>0:
            messages.success(request,"School already Registered")
            return HttpResponseRedirect('http://127.0.0.1:8000/school/')
        else:
            tempdata=tempschool(schoolname=sname,schoolnumber=snumber,schoolphone=sphone,schoolemail=semail,schooladdress=saddress,schoolpassword=spassword)
            tempdata.save()
            messages.success(request,"School Registration successful!")
            return HttpResponseRedirect('http://127.0.0.1:8000/school/')
        
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/school/')
    

def admissionreqpage(request):
    if request.session.has_key('schoolid'):
        student=studenttempschoolreg.objects.filter(schoolnumber=request.session['schoolid'])
        return render(request,'admissionrequests.html',{'student':student})

def admissionconfirm(request,studentid):
    if request.session.has_key('schoolid'):
        studentdata=studenttempschoolreg.objects.get(studentid=studentid)
        confstudent=studentpermanentschoolreg(studentid=studentdata.studentid,schoolnumber=request.session['schoolid'],classname=studentdata.classname)
        confstudent.save()
        studentdata.delete()
        return HttpResponseRedirect('http://127.0.0.1:8000/school/admissionrequests/')
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/school/admissionrequests/')
        

def admissiondecline(request,studentid):
    if request.session.has_key('schoolid'):
        studentdata=studenttempschoolreg.objects.get(studentid=studentid)
        studentdata.delete()
        return HttpResponseRedirect('http://127.0.0.1:8000/school/admissionrequests/')
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/school/')
        
# def studentprofiles(request):
#     if request.session.has_key('schoolid'):
#         return render(request,'studentprofile.html')
#     else:
#         return HttpResponseRedirect('http://127.0.0.1:8000/school/')

def studentresultsupload(request):
    if request.session.has_key('schoolid'):
        return render(request,'studentresult.html')
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/school/')
    
def studentresultsuploadsave(request):
    if request.session.has_key('schoolid'):
        studentid=request.POST.get('studentid')
        studentclass=request.POST.get('classname')
        studentpassingdate=request.POST.get('passingdate')
        studentpercentage=request.POST.get('percentage')
        studdetailscount=confstudent.objects.filter(adhar=studentid).count()
        if studdetailscount>0:
            studentres=studentresult(studentid=studentid,schoolid=request.session['schoolid'],passingdate=studentpassingdate,studentclass=studentclass,studentpercentage=studentpercentage)
            studentres.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/school/studentresultupload/')
        else:
            messages.success(request,"No such student exist")
            return HttpResponseRedirect('http://127.0.0.1:8000/school/studentresultupload/')
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/school/')

def studentviewresults(request):
    if request.session.has_key('schoolid'):  
        id=request.POST.get('id')
        studres=studentresult.objects.filter(studentid=id)
        # st=int(studres)
        return render(request,'studentviewresult.html',{'studres':studres})
    
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/school/')
    
def studentdetail(request):
    if request.session.has_key('schoolid'): 
        studid=request.POST.get('id') 
        studdetails=confstudent.objects.filter(adhar=studid)
        return render(request,'studentprofile.html',{'studdetails':studdetails})
    else:
        messages.success(request,"No such student exist")
        return HttpResponseRedirect('http://127.0.0.1:8000/school/')