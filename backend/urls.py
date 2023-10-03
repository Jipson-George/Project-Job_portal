from django.urls import path
from backend import views

urlpatterns =[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('adminloginpage/',views.adminloginpage,name="adminloginpage"),
    path('loginadmin/',views.loginadmin,name="loginadmin"),
    path('job_types/',views.job_types,name="job_types"),
    path('addjob/',views.addjob,name="addjob"),
    path('displayjob/',views.displayjob,name="displayjob"),
    path('addjobtype/',views.addjobtype,name="addjobtype"),
    path('jobtypeadd/',views.jobtypeadd,name="jobtypeadd"),
    path('jobtypedisplay/',views.jobtypedisplay,name="jobtypedisplay"),
    path('jobcatedit/<int:jcid>/',views.jobcatedit,name="jobcatedit"),
    path('editjobcat/<int:jcid>/',views.editjobcat,name="editjobcat"),
    path('deletejobcat/<int:jcid>/',views.deletejobcat,name="deletejobcat"),
    path('jobtypeedit/<int:jtid>/',views.jobtypeedit,name="jobtypeedit"),
    path('editjobtype/<int:jtid>/',views.editjobtype,name="editjobtype"),
    path('employerpage/',views.employerpage,name="employerpage"),
    path('postedjobs/<emp>/',views.postedjobs,name="postedjobs"),
    path('approved_jobs/<int:jid>/',views.approved_jobs,name="approved_jobs"),
    path('pendingjobs/',views.pendingjobs,name="pendingjobs"),
    path('job_fdetail/<int:jid>/',views.job_fdetail,name="job_fdetail"),
    path('companyprofile/',views.companyprofile,name="companyprofile"),
    path('rejectjob/<int:jid>/',views.rejectjob,name="rejectjob"),
    path('jobsrejected/',views.jobsrejected,name="jobsrejected"),
    path('getapproved_jobs/',views.getapproved_jobs,name="getapproved_jobs"),

    path('pendingemployer/',views.pendingemployer,name="pendingemployer"),
    path('verifyemployer/<int:jid>/',views.verifyemployer,name="verifyemployer"),
    path('approvedemployers/',views.approvedemployers,name="approvedemployers"),
    path('rejectedemployers/',views.rejectedemployers,name="rejectedemployers"),
    path('rejectemployer/<int:jid>/',views.rejectemployer,name="rejectemployer"),
    path('enquiry_page/',views.enquiry_page,name="enquiry_page"),
    path('backendapplicants/',views.backendapplicants,name="backendapplicants"),
    path('Applicant_profile/<c>/',views.Applicant_profile,name="Applicant_profile"),
    path('Applications/<e>/',views.Applications,name="Applications"),

    path('Gettingapplicant/<a>/',views.Gettingapplicant,name="Gettingapplicant"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('getclosedjobs/',views.getclosedjobs,name="getclosedjobs"),
    path('bapplicant/<aid>/',views.bapplicant,name="bapplicant"),
    path('blockedapplicants/',views.blockedapplicants,name="blockedapplicants")


]