from django.shortcuts import render,redirect
from django.contrib import messages
from backend.models import jobdb,job_typedb,verifiedjobdb
from empapp.models import jobpostdb,Employerregdb,applicationdb,companydb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from frontend.models import applicantprofiledb
import datetime
# Create your views here.

def employerhome(request):
        jobdata = jobdb.objects.all()
        job_typedata = job_typedb.objects.all()
        x=companydb.objects.filter(Eemail=request.session['Email'])
        if not companydb.objects.filter(Eemail=request.session['Email']).exists():
            return redirect(empprofile)
        else:
            return render(request,"employerhome.html",{'jobdata':jobdata,'job_typedata':job_typedata,'x':x})

def employerreg(request):
    return render(request,"employerreg.html")
def saveemployerdetails(request):
    if request.method=="POST":
        en = request.POST.get('Name')
        ee = request.POST.get('Email')
        em = request.POST.get('Mobile')
        ep = request.POST.get('Password')
        obj = Employerregdb(Name=en,Email=ee,Mobile=em,Password=ep)
        obj.save()
        return redirect(employerreg)
def Employerlogin(request):
    if request.method =="POST":
        email = request.POST.get("Email")
        pwd = request.POST.get("Password")
        if Employerregdb.objects.filter(Email=email,Password=pwd).exists():
            request.session['Email']=email
            request.session['Password']=pwd
            messages.success(request, "login successfull")
            if companydb.objects.filter(Eemail=email).exists():
                messages.success(request,"Welcome Back")
            else:
                messages.warning(request,"Create Your profile for faster verification")
                return redirect(empprofile)
            return redirect(new_home)
        else:
            return redirect(employerreg)
    return redirect(employerreg)
def employerlogout(request):
    del request.session['Email']
    del request.session['Password']
    messages.success(request,"logout successfull")
    return redirect(employerreg)
def add_job(request):
    jobdata = jobdb.objects.all()
    job_typedata = job_typedb.objects.all()
    employerdata = Employerregdb.objects.filter(Name=request.session['Email'])
    return render(request,"add_new_job.html",{'jobdata':jobdata,'job_typedata':job_typedata,'employerdata':employerdata})
def jobpost(request):

    if request.method=="POST":
        cid=request.POST.get('Companyid')
        empid=request.POST.get('id')
        user=request.POST.get('User')
        jt=request.POST.get('Title')
        jc=request.POST.get('Company')
        coe=request.POST.get('Companyemail')
        ty=request.POST.get('Jobtype')
        ca=request.POST.get('Jobcat')
        jq=request.POST.get('Qualification')
        je=request.POST.get('Experiance')
        jl=request.POST.get('Location')
        js=request.POST.get('Salary')
        jd=request.POST.get('Description')
        we=request.POST.get('Website')
        re=request.POST.get('Require')
        if companydb.objects.filter(Eemail=user,status="verified").exists():
            obj=jobpostdb(Cid=cid,empid=empid,User=user,Title=jt,Company=jc,Cemail=coe,Type=ty,Category=ca,Qualification=jq,Experiance=je,Location=jl,Salary=js,Description=jd,approval="pending",website=we,Requirement=re)
            obj.save()
            messages.warning(request, "Pending verification")
            return redirect(employerhome)
        else:
            messages.error(request,"company verification pending")
            return redirect(new_home)

def recentjobpage(request):
    postdata=jobpostdb.objects.filter(User=request.session['Email']).order_by('-id')
    return render(request,"Recent_jobs.html",{'postdata':postdata})
# def jobedit(request,jpid):
#     jobdata = jobdb.objects.all()
#     job_typedata = job_typedb.objects.all()
#     postdata=jobpostdb.objects.get(id=jpid)
#     return render(request,"editjobs.html",{'jobdata':jobdata,'job_typedata':job_typedata,'postdata':postdata})
# # def editjobs(request,jpid):
#     if request.method=="POST":
#         user=request.POST.get('User')
#         jt=request.POST.get('Title')
#         jc=request.POST.get('Company')
#         ty=request.POST.get('Jobtype')
#         ca=request.POST.get('Jobcat')
#         jq=request.POST.get('Qualification')
#         je=request.POST.get('Experiance')
#         jl=request.POST.get('Location')
#         js=request.POST.get('Salary')
#         jd=request.POST.get('Description')
#         jobpostdb.objects.filter(id=jpid).update(User=user,Title=jt,Company=jc,Type=ty,Category=ca,Qualification=jq,Experiance=je,Location=jl,Salary=js,Description=jd,approval="pending")
#         return redirect(recentjobpage)
def applicants(request,jid):
    adata=applicationdb.objects.filter(jobid=jid)
    return render(request,"applicants.html",{'adata':adata})
def employerprofile(request):
    x=companydb.objects.filter(Eemail=request.session['Email'])
    return render(request,"Employer_profile.html",{'x':x})
def empprofile(request):
    e=Employerregdb.objects.filter(Email=request.session['Email'])

    return render(request,"emp_profile.html",{'e':e})
def addempprofile(request):
    if request.method=="POST":
        us=request.POST.get('User')
        na=request.POST.get('Name')
        co=request.POST.get('Company')
        nat=request.POST.get('Nature')
        ne=request.POST.get('Noemp')
        fo=request.POST.get('Found')
        con=request.POST.get('Contact')
        ce=request.POST.get('Cemail')
        ad=request.POST.get('Address')
        de=request.POST.get('Description')
        lo=request.FILES['Logo']
        doc=request.FILES['Document']
        we=request.POST.get('Website')
        obj=companydb(Eemail=us,Ename=na,Company=co,Nature=nat,Enumber=ne,Founded=fo,Contact=con,Cemail=ce,Address=ad,Description=de,Logo=lo,Documentation=doc,Website=we)
        obj.save()
        messages.success(request,"Profile created Successfully")
        return redirect(employerhome)

def editcprofile(request,cid):
    cdata=companydb.objects.get(id=cid)
    return render(request,"edit_company.html",{'cdata':cdata})

def editempprofile(request,cid):
    if request.method == "POST":
        us = request.POST.get('User')
        na = request.POST.get('Name')
        co = request.POST.get('Company')
        nat = request.POST.get('Nature')
        ne = request.POST.get('Noemp')
        fo = request.POST.get('Found')
        con = request.POST.get('Contact')
        ce = request.POST.get('Cemail')
        ad = request.POST.get('Address')
        de = request.POST.get('Description')
        try:
            lo = request.FILES['Logo1']
            fs = FileSystemStorage()
            file = fs.save(lo.name,lo)
        except MultiValueDictKeyError:
            file = companydb.objects.get(id=cid).Logo
        try:
            doc = request.FILES['Document']
            fs = FileSystemStorage()
            file1=fs.save(doc.name,doc)
        except MultiValueDictKeyError:
            file1=companydb.objects.get(id=cid).Documentation
        we = request.POST.get('Website')
        companydb.objects.filter(id=cid).update(Eemail=us, Ename=na, Company=co, Nature=nat, Enumber=ne, Founded=fo, Contact=con, Cemail=ce,
                        Address=ad, Description=de, Logo=file, Documentation=file1, Website=we)

        messages.success(request, "Profile edited Successfully")
        return redirect(employerprofile)


def new_home(request):
    x=companydb.objects.filter(status="verified").order_by('-id')[:6]
    return render(request,"new_home.html",{'x':x})
def jobpostdetails(request,joid):
    j=jobpostdb.objects.filter(id=joid)
    return render(request,"emp_job_details.html",{'j':j})
def getapplicantP(request):
    a=applicantprofiledb.objects.all()
    if request.method=="GET":
        ap=request.GET.get('em')
        if ap!=None:
            a=applicantprofiledb.objects.filter(Email=ap)
    return render(request,"profile_ofapplicant.html",{'a':a})
def closejob(request,j):

    jobpostdb.objects.filter(id=j).update(approval="Closed")
    verifiedjobdb.objects.filter(Jobid=j).update(approval="closed")
    messages.success(request,"Job closed")
    return redirect(recentjobpage)
def profile_of_applicant(request):
    return render(request,"profile_ofapplicant.html")
