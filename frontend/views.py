from django.shortcuts import render,redirect
from backend.models import jobdb,job_typedb,verifiedjobdb
from frontend.models import applicantregdb,applicantprofiledb,enquirydb
from empapp.models import applicationdb,companydb
from django.contrib import messages
from empapp.models import jobpostdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def homepage(req):
    jobdata = jobdb.objects.all()[:8]
    adata=applicantprofiledb.objects.all()
    vjob =jobpostdb.objects.filter(approval="verified").order_by('-id')[:6]
    return render (req,"home.html",{'jobdata':jobdata,'vjob':vjob,'adata':adata})


def job_detail(request,jid):
    jdata=jobpostdb.objects.get(id=jid)
    return render(request,"jobdetails.html",{'jdata':jdata})
def applicantreg(request):
    return render(request,"applicantreg.html")
def saveapplicant(request):
    if request.method == "POST":
        en = request.POST.get('Name')
        ee = request.POST.get('email')
        em = request.POST.get('Mobile')

        ep = request.POST.get('password')
        obj =applicantregdb (Name=en, email=ee, Mobile=em, Password=ep)
        obj.save()
        return redirect(applicantreg)
def applicantsignin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        pwd=request.POST.get('Password')
        if applicantregdb.objects.filter(email=email,Password=pwd).exists():
            request.session['email']=email
            request.session['Password']=pwd
            if not applicantprofiledb.objects.filter(Email=email).exists():
                messages.warning(request, "create your profile for faster approval")
                return redirect(applicantprofile)
            else:
                messages.success(request,"Signed in successfully")
                return redirect(homepage)

        else:
            messages.error(request,"invalid ")
            return redirect(applicantreg)

    return redirect(applicantreg)
def applicantlogout(request):
    del request.session['email']
    del request.session['Password']
    messages.success(request,"logout successfull")
    return redirect(homepage)
def joblisting(request,c_name):
    jdata=verifiedjobdb.objects.filter(Category=c_name)
    return render(request,"job_listing.html",{'jdata':jdata})
def application(request):
    if request.method=="POST":
        jid=request.POST.get('jobid')
        na=request.POST.get('Name')
        em=request.POST.get('Email')
        mo=request.POST.get('Mobile')
        cm=request.POST.get('Company')
        jt=request.POST.get('Title')
        co=request.POST.get('Cover')
        re=request.FILES['Resume']
        ce=request.POST.get('cemail')
        if applicantregdb.objects.filter(email=em, status="blocked").exists():
            messages.error(request, "Blocked")
            return redirect(homepage)
        elif applicationdb.objects.filter(email=em,jobid=jid).exists():
            messages.error(request,"Already applied")
            return redirect(homepage)

        elif not applicantprofiledb.objects.filter(Email=em).exists():
            messages.warning(request,"create your profile..!")
            return redirect(applicantprofile)
        else:
            obj=applicationdb(jobid=jid,name=na,email=em,mobile=mo,company=cm,jobtitle=jt,cover=co,Cemail=ce,Resume=re)
            obj.save()
            messages.success(request,"application sent")
            return redirect(homepage)
def contactpage(request):
    return render(request,"contact.html")
def aboutpage(request):
    return render(request,"about.html")
def applicantprofile(request):
    return render(request,"applicantP.html")
def addAProfile(request):
    if request.method=="POST":
        na=request.POST.get('name')
        im=request.FILES['image']
        em=request.POST.get('email')
        ph=request.POST.get('phone')
        ad=request.POST.get('address')
        st=request.POST.get('street')
        ci=request.POST.get('city')
        nat=request.POST.get('nation')
        ge=request.POST.get('gender')
        dd=request.POST.get('ddate')
        dm=request.POST.get('dmonth')
        dy=request.POST.get('dyear')
        ma=request.POST.get('marital')
        pg=request.POST.get('PG')
        in1=request.POST.get('institution1')
        de=request.POST.get('Degree')
        in2=request.POST.get('institution2')
        ten=request.POST.get('10th')
        in3=request.POST.get('institution3')
        ot=request.POST.get('other')
        in4=request.POST.get('institution4')
        sk1=request.POST.get('skill1')
        sk2=request.POST.get('skill2')
        sk3=request.POST.get('skill3')

        ex1=request.POST.get('experiance')
        ex2=request.POST.get('experiance2')
        ex3=request.POST.get('experiance3')
        res=request.FILES['resume']
        des1=request.POST.get('des1')
        des2=request.POST.get('des2')
        des3=request.POST.get('des3')
        scr1=request.POST.get('score1')
        scr2=request.POST.get('score2')
        scr3=request.POST.get('score3')
        scr4=request.POST.get('score4')
        obj=applicantprofiledb(Name=na,Image=im,Email=em,Phone=ph,Address=ad,Street=st,City=ci,Nation=nat,Gender=ge,
                               Ddate=dd,Dmonth=dm,Dyear=dy,Marital=ma,Pg=pg,Inst1=in1,Inst2=in2,Degree=de,Tenth=ten,
                               Inst3=in3,Others=ot,Inst4=in4,Skill1=sk1,Skill2=sk2,Skill3=sk3,Exp=ex1,Exp2=ex2,
                               Exp3=ex3,Resume=res,Des1=des1,Des2=des2,Des3=des3,Score1=scr1,Score2=scr2,Score3=scr3,Score4=scr4)
        obj.save()
        messages.success(request,"Profile created")
        return redirect(homepage)
def Applicantp(request):
    if not applicantprofiledb.objects.filter(Email=request.session['email']).exists():
        return redirect(applicantprofile)
    else:
        a=applicantprofiledb.objects.filter(Email=request.session['email'])
        return render(request,"Aprofile.html",{'a':a})
def EditapplicantP(request,pid):
    p=applicantprofiledb.objects.get(id=pid)
    return render(request,"editapplicantP.html",{'p':p})

def updateapplicantP(request,pid):
    if request.method=="POST":
        na=request.POST.get('name')
        try:
            im=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError :
            file=applicantprofiledb.objects.get(id=pid).Image
        em=request.POST.get('email')
        ph=request.POST.get('phone')
        ad=request.POST.get('address')
        st=request.POST.get('street')
        ci=request.POST.get('city')
        nat=request.POST.get('nation')
        ge=request.POST.get('gender')
        dd=request.POST.get('ddate')
        dm=request.POST.get('dmonth')
        dy=request.POST.get('dyear')
        ma=request.POST.get('marital')
        pg=request.POST.get('PG')
        in1=request.POST.get('institution1')
        de=request.POST.get('Degree')
        in2=request.POST.get('institution2')
        ten=request.POST.get('10th')
        in3=request.POST.get('institution3')
        ot=request.POST.get('other')
        in4=request.POST.get('institution4')
        sk1=request.POST.get('skill1')
        sk2=request.POST.get('skill2')
        sk3=request.POST.get('skill3')

        ex1=request.POST.get('experiance')
        ex2=request.POST.get('experiance2')
        ex3=request.POST.get('experiance3')
        try:
            res=request.FILES['resume']
            fs=FileSystemStorage()
            file1=fs.save(res.name,res)
        except MultiValueDictKeyError:
            file1=applicantprofiledb.objects.get(id=pid).Resume
        des1=request.POST.get('des1')
        des2=request.POST.get('des2')
        des3=request.POST.get('des3')
        scr1=request.POST.get('score1')
        scr2=request.POST.get('score2')
        scr3=request.POST.get('score3')
        scr4=request.POST.get('score4')
        applicantprofiledb.objects.filter(id=pid).update(Name=na,Image=file,Email=em,Phone=ph,Address=ad,Street=st,City=ci,Nation=nat,Gender=ge,
                               Ddate=dd,Dmonth=dm,Dyear=dy,Marital=ma,Pg=pg,Inst1=in1,Inst2=in2,Degree=de,Tenth=ten,
                               Inst3=in3,Others=ot,Inst4=in4,Skill1=sk1,Skill2=sk2,Skill3=sk3,Exp=ex1,Exp2=ex2,
                               Exp3=ex3,Resume=file1,Des1=des1,Des2=des2,Des3=des3,Score1=scr1,Score2=scr2,Score3=scr3,Score4=scr4)

        return redirect(Applicantp)
# def getcompanyprofile(request):
#     x=companydb.objects.all()
#
#     if request.method=="GET":
#         cn=request.GET.get('can')
#         if cn!=None:
#             x=companydb.objects.filter(Cemail=cn)
#     return render(request,"get_emp_profile.html",{'x':x})

def gettingcompany(request,c):
    jdata=companydb.objects.filter(id=c)
    return render(request,"get_emp_profile.html",{'jdata':jdata})
def gettingappliedjobs(request):
    jdata=applicationdb.objects.filter(email=request.session['email'])
    return render(request,"applied_jobs.html",{'jdata':jdata})
# def getappliedjobdetails(request):
#     jdata=verifiedjobdb.objects.all()
#     if request.method=="GET":
#         ji=request.GET.get('ji')
#         if ji!=None:
#             jdata=verifiedjobdb.objects.filter(Jobid=ji)
#     return render(request,"jobdetails.html",{'jdata':jdata})
def all_jobs(request):
    jdata=jobpostdb.objects.filter(approval="verified").order_by('-id')
    return render(request,"job_listing.html",{'jdata':jdata})
def enquiry(request):
    if request.method=="POST":
        na=request.POST.get('Name')
        em=request.POST.get('Email')
        su=request.POST.get('Subject')
        me=request.POST.get('Message')
        obj=enquirydb(name=na,email=em,subject=su,message=me)
        obj.save()
        messages.success(request,"Enquiry sent")
        return redirect(contactpage)
def getappliedjobdetails(request,c):
    jdata=jobpostdb.objects.filter(id=c)
    return render(request,"jobdetails.html",{'jdata':jdata})
def searchbar(request):
    jdata=jobpostdb.objects.filter(approval="verified")
    if request.method=="GET":
        c=request.GET.get('cat')
        p=request.GET.get('place')
        if c==None:
            jdata=jobpostdb.objects.filter(approval="verified",Location__icontains=p)
        elif p==None:
            jdata=jobpostdb.objects.filter(approval="verified",Title__icontains=c)


        else:
            jdata= jobpostdb.objects.filter(approval="verified",Title__icontains=c,Location__icontains=p)
    return render(request,"job_listing.html",{'jdata':jdata})

