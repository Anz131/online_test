from django.urls import path
from owner import views

urlpatterns=[
    path("accounts/signin",views.SignInView.as_view(),name="signin"),
    path("accounts/signup",views.UserCreationView.as_view(),name="signup"),
    path("userhome",views.UserHome.as_view(),name="userhome"),
    path("home",views.OwnerHome.as_view(),name="home"),
    path("question/add",views.add_qus,name="addqus"),
    path("accounts/signout",views.SignOutView.as_view(),name="signout"),
    path("testfinish",views.TestFinish.as_view(),name="testfinish"),
    # path("question/edit/<int:id>",views.editqus(),name="editqus"),
    # path("question/<int:id>",views.QusDetailView.as_view(),name="qusdetail"),
]