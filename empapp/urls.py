from django.urls import path
from empapp import views
urlpatterns=[
    path('employerhome/',views.employerhome,name="employerhome"),
    path('employerreg/',views.employerreg,name="employerreg"),
    path('saveemployerdetails/',views.saveemployerdetails,name="saveemployerdetails"),
    path('Employerlogin/',views.Employerlogin,name="Employerlogin"),
    path('employerlogout/',views.employerlogout,name="employerlogout"),
    path('add_job/',views.add_job,name="add_job"),
    path('jobpost/',views.jobpost,name="jobpost"),
    path('recentjobpage/',views.recentjobpage,name="recentjobpage"),

    path('applicants/<int:jid>/', views.applicants, name="applicants"),
    path('employerprofile/',views.employerprofile,name="employerprofile"),
    path('empprofile/',views.empprofile,name="empprofile"),
    path('addempprofile/',views.addempprofile,name="addempprofile"),
    path('new_home/',views.new_home,name="new_home"),
    path('editcprofile/<int:cid>/',views.editcprofile,name="editcprofile"),
    path('editempprofile/<int:cid>/',views.editempprofile,name="editempprofile"),
    path('jobpostdetails/<int:joid>',views.jobpostdetails,name="jobpostdetails"),
    path('getapplicantP/',views.getapplicantP,name="getapplicantP"),
    path('closejob/<int:j>/',views.closejob,name="closejob"),
    path('profile_of_applicant/',views.profile_of_applicant,name="profile_of_applicant")



        ]