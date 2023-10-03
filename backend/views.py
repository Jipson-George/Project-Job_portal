from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from backend.models import jobdb,job_typedb,verifiedjobdb
from empapp.models import Employerregdb,jobpostdb,companydb,applicationdb
from frontend.models import enquirydb,applicantprofiledb,applicantregdb
# Create your views here.
def indexpage(req):
    return render(req,"index.html")
def adminloginpage(request):
    return render(request,"adminlogin.html")

def loginadmin(request):
    if request.method=="POST":
        uname= request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user=authenticate(username=uname,password=pwd)
            if User is not None:
                login(request,user)
                request.session['username']=uname
                request.session['password']=pwd
                messages.success(request,"login successful")
                return redirect(indexpage)
        else:
            messages.error(request,"invalid username\password")
            return redirect(adminloginpage)
    else:

        return redirect(adminloginpage)
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"logout successfull")
    return redirect(adminloginpage)

def job_types(req):
    return render(req,"job_details.html")
def addjob(request):
    if request.method=="POST":
        job = request.POST.get('Job')
        obj = jobdb(jobcat=job)
        obj.save()
        return redirect(job_types)
def displayjob(request):
    cat =jobdb.objects.all()
    return render(request,"job_details_display.html",{'cat':cat})
def addjobtype(request):
    return render(request,"job_type.html")

def jobtypeadd(request):
    if request.method=="POST":
        job = request.POST.get('Jobtype')
        obj = job_typedb(jobtype=job)
        obj.save()
        return redirect(addjobtype)
def jobtypedisplay(request):
    typedata = job_typedb.objects.all()
    return render(request,"jobtype_display.html",{'typedata':typedata})
def jobcatedit(request,jcid):
    jobcat = jobdb.objects.get(id=jcid)
    return render(request,"job_cat_edit.html",{'jobcat':jobcat})
def editjobcat(request,jcid):
    if request.method=="POST":
        jc = request.POST.get('Job')
        jobdb.objects.filter(id=jcid).update(jobcat=jc)
        return redirect(displayjob)
def deletejobcat(request,jcid):
    data = jobdb.objects.get(id=jcid)
    data.delete()
    return redirect(displayjob)
def jobtypeedit(request,jtid):
    typedata = job_typedb.objects.get(id=jtid)
    return render(request,"job_type_edit.html",{'typedata':typedata})
def editjobtype(request,jtid):
    if request.method=="POST":
        jt= request.POST.get('Jobtype')
        job_typedb.objects.filter(id=jtid).update(jobtype=jt)
        return redirect(jobtypedisplay)
def employerpage(request):
    empdata=companydb.objects.filter(status="verified")
    return render(request,"employers.html",{'empdata':empdata})
def postedjobs(request,emp):
    postdata=jobpostdb.objects.filter(User=emp)
    return render(request,"posted_jobs.html",{'postdata':postdata})
def approved_jobs(request,jid):
    if verifiedjobdb.objects.filter(Jobid=jid).exists():
        messages.warning(request,"Already Verified")
        return redirect(employerpage)
        # verifiedjobdb.objects.filter(id=jid).update(Title=jt,User=us,Company=jc,Type=ty,Category=cat,Qualification=qu,Location=lo,Experiance=ex,Salary=sa,Description=de,Date=da)
    elif request.method=="POST":
        ji=request.POST.get('jobid')
        jt=request.POST.get('title')
        us =request.POST.get('user')
        jc=request.POST.get('company')
        ty=request.POST.get('type')
        cat=request.POST.get('category')
        qu=request.POST.get('qualification')
        lo=request.POST.get('location')
        ex=request.POST.get('exp')
        sa=request.POST.get('salary')
        de=request.POST.get('des')
        da=request.POST.get('date')
        re=request.POST.get('Require')
        cem=request.POST.get('cemail')
        we=request.POST.get('website')
        obj=verifiedjobdb(Jobid=ji,Title=jt,User=us,Company=jc,Type=ty,Category=cat,Qualification=qu,Location=lo,Experiance=ex,Salary=sa,Description=de,Date=da,Requirement=re,website=we,Cemail=cem)
        obj.save()
        jobpostdb.objects.filter(id=jid).update(approval="verified")
        messages.success(request, "Job verified successfully")
        return redirect(pendingjobs)
def pendingjobs(request):
    a=jobpostdb.objects.filter(approval="pending")
    return render(request,"Pending_jobs.html",{'a':a})
def job_fdetail(request,jid):
    x=jobpostdb.objects.filter(id=jid)
    return render(request,"job_full_details.html",{'x':x})
def companyprofile(request):
    x=companydb.objects.all()
    if request.method=="GET":
        cn=request.GET.get('com')
        if cn!=None:
            x=companydb.objects.filter(Cemail=cn)
    return render(request,"Company_profile.html",{'x':x})
def rejectjob(request,jid):
    jobpostdb.objects.filter(id=jid).update(approval="Rejected")
    messages.warning(request, " Rejected")
    return redirect(pendingjobs)
def jobsrejected(request):
    a=jobpostdb.objects.filter(approval="Rejected")

    return render(request,"Pending_jobs.html",{'a':a})
def getapproved_jobs(request):
    a=jobpostdb.objects.filter(approval="verified")
    return render(request,"Pending_jobs.html",{'a':a})
def pendingemployer(request):
    empdata=companydb.objects.filter(status="Pending")
    return render(request,"employers.html",{'empdata':empdata})
def verifyemployer(request,jid):
    if companydb.objects.filter(id=jid,status="verified").exists():
        messages.success(request,"Already verified")
        return redirect(employerpage)
    else:
        companydb.objects.filter(id=jid).update(status="verified")
        messages.success(request,"company verified")
        return redirect(employerpage)
def rejectemployer(request,jid):
    if companydb.objects.filter(id=jid,status="rejected").exists():
        messages.error(request,"already rejected")
        return redirect(indexpage)
    else:
        companydb.objects.filter(id=jid).update(status="rejected")
        messages.success(request,"company rejected")
        return redirect(indexpage)
def approvedemployers(request):
    empdata=companydb.objects.filter(status="verified")
    return render(request,"employers.html",{'empdata':empdata})
def rejectedemployers(request):
    empdata=companydb.objects.filter(status="rejected")
    return render(request,"employers.html",{'empdata':empdata})
def enquiry_page(request):
    x=enquirydb.objects.all().order_by('-id')
    return render(request,"enquirys.html",{'x':x})
def backendapplicants(request):
    a=applicantregdb.objects.filter(status="ok")
    return render(request,"backendapplicant.html",{'a':a})
def Applicant_profile(request,c):
    a=applicantprofiledb.objects.filter(Email=c)
    return render(request,"applicant_profile.html",{'a':a})
def Applications(request,e):
    j=applicationdb.objects.filter(email=e)
    return render(request,"gettingbapplicants.html",{'j':j})
# def blockapplicant(request,aid):
#     applicantregdb.objects.filter(id=aid).update(status="blocked")
#     messages.warning(request,"Applicant blocked")
#     return redirect(backendapplicants)
def Gettingapplicant(request,a):
    a=applicationdb.objects.filter(jobid=a)
    return render(request,"Applicationb.html",{'a':a})
def getclosedjobs(request):
    a = jobpostdb.objects.filter(approval="Closed")

    return render(request, "Pending_jobs.html", {'a': a})
def bapplicant(request,aid):
    applicantregdb.objects.filter(email=aid).update(status="blocked")
    messages.success(request,"Applicant blocked")
    return redirect(backendapplicants)
def blockedapplicants(request):
    a=applicantregdb.objects.filter(status="blocked")
    return render(request,"backendapplicant.html",{'a':a})