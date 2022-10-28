"""prisonproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from prisonapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login',views.login),

    path('adminhome',views.adminhome),
    path('admincell',views.admincell),
    path('adminupdatecell',views.adminupdatecell),
    path('admindeletecell',views.admindeletecell),
    path('admindesignation',views.admindesignation),
    path('adminupdatedesignation',views.adminupdatedesignation),
    path('admindeletedesignation',views.admindeletedesignation),
    path('adminpolice',views.adminpolice),
    path('adminpolicedelete',views.adminpolicedelete),
    path('adminprisoner',views.adminprisoner),
    path('admincrime',views.admincrime),
    path('admininout',views.admininout),
    path('adminparole',views.adminparole),
    path('adminrelease',views.adminrelease),
    path('adminaddamount',views.adminaddamount),
    
    path('dataadminhome',views.dahome),
    path('daprisoner',views.daprisoner),
    path('daprisonerupdate',views.daprisonerupdate),
    path('daprisonerdelete',views.daprisonerdelete),
    path('dacrime',views.dacrime),
    path('dacrimeupdate',views.dacrimeupdate),
    path('dacrimedelete',views.dacrimedelete),
    path('dainout',views.dainout),
    path('dainoutupdate',views.dainoutupdate),
    path('daparole',views.daparole),
    path('darelease',views.darelease),
    path('davisitor',views.davisitor),
    path('davisitorupdate',views.davisitorupdate),

    path('policehome',views.policehome),
    path('policeprisoner',views.policeprisoner),
    path('policecrime',views.policecrime),
    path('policeinout',views.policeinout),
    path('policeparole',views.policeparole),
    path('policerelease',views.policerelease),    
    path('policevisitor',views.policevisitor),    
]
