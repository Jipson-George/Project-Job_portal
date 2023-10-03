from django.urls import path

from frontend import views

urlpatterns =[
    path('homepage/',views.homepage,name="homepage"),
    path('job_detail/<int:jid>/',views.job_detail,name="job_detail"),
    path('applicantreg/',views.applicantreg,name="applicantreg"),
    path('saveapplicant/',views.saveapplicant,name="saveapplicant"),
    path('applicantsignin/',views.applicantsignin,name="applicantsignin"),
    path('applicantlogout/',views.applicantlogout,name="applicantlogout"),
    path('joblisting/<c_name>',views.joblisting,name="joblisting"),
    path('application/',views.application,name="application"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('applicantprofile/',views.applicantprofile,name="applicantprofile"),
    path('addAProfile/',views.addAProfile,name="addAProfile"),
    path('Applicantp/',views.Applicantp,name="Applicantp"),
    path('EditapplicantP/<int:pid>/',views.EditapplicantP,name="EditapplicantP"),
    path('updateapplicantP/<int:pid>/',views.updateapplicantP,name="updateapplicantP"),

    path('gettingcompany/<int:c>/',views.gettingcompany,name="gettingcompany"),
    path('gettingappliedjobs/',views.gettingappliedjobs,name="gettingappliedjobs"),
    path('getappliedjobdetails/<c>/',views.getappliedjobdetails,name="getappliedjobdetails"),
    path('all_jobs/',views.all_jobs,name="all_jobs"),
    path('enquiry/',views.enquiry,name="enquiry"),
    path('searchbar/',views.searchbar,name="searchbar")


]