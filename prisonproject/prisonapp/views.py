from datetime import datetime
from platform import release
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Cells,Crime,Designation, Finance,InOut,Parole,Police,Prisoner,Release,Visitor


######################################################################
#                                                                    #
#                                                                    #
#                           COMMON                                   #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                           LOAD INDEX PAGE
######################################################################
def index(request):
    return render(request,"index.html")
######################################################################
#                           LOAD LOGIN PAGE
######################################################################
def login(request):
    msg=""
    if request.POST:
        #read the username and password given in UI
        email=request.POST['username']
        pwd=request.POST['password']
        #checking whether username and email exist in authenticate table
        user=authenticate(username=email,password=pwd)
        if user is None:
            #username or password is incorrect
            messages.info(request, 'Username or password incorrect')
        else:
            #username and password is correct
            user_data=User.objects.get(username=email)
            if user_data.is_active==0:
                messages.info(request, 'Inactive user')
            else:
                if user_data.is_superuser==1 and user_data.is_staff==1:
                    #if admin, goto admin interface
                    return redirect("/adminhome")
                elif user_data.is_superuser==1 and user_data.is_staff==0:
                    return redirect("/dataadminhome")
                elif user_data.is_superuser==0 and user_data.is_staff==1:
                    request.session["email"] = email
                    r = Police.objects.get(email=email)
                    request.session["id"] = r.id
                    request.session["name"] = r.name
                    return redirect("/policehome")
    return render(request,"login.html",{"msg":msg})
######################################################################
#                                                                    #
#                                                                    #
#                           ADMIN                                    #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                           LOAD ADMIN PAGE
######################################################################
def adminhome(request):
    return render(request,"adminhome.html")
######################################################################
#                           LOAD ADMIN CELL PAGE
######################################################################
def admincell(request):
    if(request.POST):
            cellno=request.POST['txtCell']
            capcity=request.POST['txtCapacity']
            cell_exist=Cells.objects.filter(cellno=cellno).exists()
            if not cell_exist:
                try:
                    r=Cells.objects.create(cellno=cellno,capacity=capcity)
                    r.save()
                except:
                    messages.info(request, 'Sorry some error occured')
                else:
                    messages.info(request, 'Data added successfully')
            else:
                #duplicate entries occur and registration is not possible
                messages.info(request, 'Data already exist')
    data=Cells.objects.all()
    return render(request,"admincell.html",{"data":data})
######################################################################
#                           LOAD ADMIN UPDATE CELL PAGE
######################################################################
def adminupdatecell(request):
    id=request.GET.get("id")
    d=Cells.objects.get(id=id)
    if(request.POST):
            cellno=request.POST['txtCell']
            capcity=request.POST['txtCapacity']
            try:
                    Cells.objects.filter(id=id).update(cellno=cellno,capacity=capcity)
            except:
                    messages.info(request, 'Sorry some error occured')
            else:
                    messages.info(request, 'Data updated successfully')
                    return redirect("/admincell")
    data=Cells.objects.all()
    return render(request,"adminupdatecell.html",{"data":data,"d":d})
######################################################################
#                           LOAD ADMIN UPDATE CELL PAGE
######################################################################
def admindeletecell(request):
    id=request.GET.get("id")
    Cells.objects.filter(id=id).delete()
    return redirect("/admincell")
######################################################################
#                           LOAD DESIGNATION PAGE
######################################################################
def admindesignation(request):
    if(request.POST):
            designation=request.POST['txtDesig']
            desig_exist=Designation.objects.filter(designation=designation).exists()
            if not desig_exist:
                try:
                    r=Designation.objects.create(designation=designation)
                    r.save()
                except:
                    messages.info(request, 'Sorry some error occured')
                else:
                    messages.info(request, 'Data added successfully')
            else:
                #duplicate entries occur and registration is not possible
                messages.info(request, 'Data already exist')
    data=Designation.objects.all()
    return render(request,"admindesignation.html",{"data":data})
######################################################################
#                           LOAD DESIGNATION PAGE
######################################################################
def adminupdatedesignation(request):
    id=request.GET.get("id")
    d=Designation.objects.get(id=id)
    if(request.POST):
            designation=request.POST['txtDesig']
            try:
                    Designation.objects.filter(id=id).update(designation=designation)
                    
            except Exception as e:
                    messages.info(request, e)
            else:
                    messages.info(request, 'Data added successfully')
                    return redirect("/admindesignation")
    data=Designation.objects.all()
    return render(request,"adminupdatedesignation.html",{"data":data,"d":d})
######################################################################
#                           LOAD DESIGNATION PAGE
######################################################################
def admindeletedesignation(request):
    id=request.GET.get("id")
    Designation.objects.filter(id=id).delete()
    return redirect("/admindesignation")
######################################################################
#                           LOAD POLICE PAGE
######################################################################
def adminpolice(request):
    if(request.POST):
            designation=request.POST['designation']
            designation=Designation.objects.get(id=designation)
            name=request.POST['txtName']
            address=request.POST['txtAddress']
            contact=request.POST['txtContact']
            email=request.POST['txtEmail']
            user=authenticate(username=email,password=contact)
            if user is None:
                try:
                    r=Police.objects.create(designation=designation,name=name,address=address,contact=contact,email=email)
                    r.save()
                except:
                    messages.info(request, 'Sorry some error occured')
                else:
                    try:
                        r=User.objects.create_user(username=email,password=contact,is_staff=1,is_active=1)
                        r.save()
                    except:
                        messages.info(request, 'Sorry some error occured')
                    else:
                        messages.info(request, 'Data added successfully')
            else:
                #duplicate entries occur and registration is not possible
                messages.info(request, 'Data already exist')
    designation=Designation.objects.all()
    data=Police.objects.all()
    return render(request,"adminpolice.html",{"data":data,"designation":designation})
######################################################################
#                           LOAD DESIGNATION PAGE
######################################################################
def adminpolicedelete(request):
    id=request.GET.get("id")
    d=Police.objects.get(id=id)
    email=d.email
    Police.objects.filter(id=id).delete()
    User.objects.filter(username=email).delete()
    return redirect("/adminpolice")
######################################################################
#                           LOAD PRISONER PAGE
######################################################################
def adminprisoner(request):
    data=Prisoner.objects.all()
    if request.POST:
        name=request.POST["txtName"]
        data=Prisoner.objects.filter(name__icontains=name)
    return render(request,"adminprisoner.html",{"data":data})
######################################################################
#                           LOAD CRIME PAGE
######################################################################
def admincrime(request):
    data=Crime.objects.all()
    if request.POST:
        crime=request.POST["txtCrime"]
        data=Crime.objects.filter(crimetitle__icontains=crime)
    return render(request,"admincrime.html",{"data":data})
######################################################################
#                           LOAD IN OUT PAGE
######################################################################
def admininout(request):
    data=InOut.objects.all()
    if request.POST:
        name=request.POST["txtName"]
        data=InOut.objects.filter(prisoner__name__icontains=name)
    return render(request,"admininout.html",{"data":data})
######################################################################
#                           LOAD PAROLE PAGE
######################################################################
def adminparole(request):
    data=Parole.objects.all()
    if request.POST:
        name=request.POST["txtName"]
        data=Parole.objects.filter(prisoner__name__icontains=name)
    return render(request,"adminparole.html",{"data":data})
######################################################################
#                           LOAD RELEASE PAGE
######################################################################
def adminrelease(request):
    data=Release.objects.all()
    if request.POST:
        name=request.POST["txtName"]
        data=Release.objects.filter(prisoner__name__icontains=name)
    return render(request,"adminrelease.html",{"data":data})
######################################################################
#                           LOAD RELEASE PAGE
######################################################################
def adminaddamount(request):
    id=request.GET.get("id")
    d=Release.objects.get(id=id)
    amt_exist=Finance.objects.filter(release=d).exists()
    if amt_exist:
            messages.info(request,"Data already exist")
            return redirect("/adminrelease")
    if request.POST:
            amt=request.POST['txtAmt']
        
        
            r=Finance.objects.create(release=d,amount=amt)
            r.save()
            messages.info(request,"Data added")
            return redirect("/adminrelease")
    return render(request,"adminaddamount.html")
######################################################################
#                                                                    #
#                                                                    #
#                          DATA ADMIN                                #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                           LOAD ADMIN PAGE
######################################################################
def dahome(request):
    return render(request,"dahome.html")
######################################################################
#                           LOAD ADMIN PAGE
######################################################################
def daprisoner(request):
    return render(request,"daprisoner.html")
######################################################################
#                           LOAD PRISONER PAGE
######################################################################
def daprisoner(request):
    if(request.POST):
            name=request.POST['txtName']
            address=request.POST['txtAddress']
            contact=request.POST['txtContact']
            place=request.POST['txtPlace']
            dob=request.POST['txtDob']
            gender=request.POST['gender']
            height=request.POST['txtHeight']
            weight=request.POST['txtWeight']
            photo=request.FILES['txtFile']
            prisoner_exist=Prisoner.objects.filter(name=name,address=address,contact=contact,height=height,weight=weight).exists()
            if not prisoner_exist:
                try:
                    r=Prisoner.objects.create(name=name,address=address,contact=contact,place=place,height=height,weight=weight,gender=gender,photo=photo,dob=dob)
                    r.save()
                except:
                    messages.info(request, 'Sorry some error occured')
                else:
                    messages.info(request, 'Data added successfully')
            else:
                #duplicate entries occur and registration is not possible
                messages.info(request, 'Data already exist')
    data=Prisoner.objects.all()
    return render(request,"daprisoner.html",{"data":data})
######################################################################
#                           LOAD PRISONER PAGE
######################################################################
def daprisonerupdate(request):
    id=request.GET.get("id")
    d=Prisoner.objects.get(id=id)
    if(request.POST):
            name=request.POST['txtName']
            address=request.POST['txtAddress']
            contact=request.POST['txtContact']
            place=request.POST['txtPlace']
            height=request.POST['txtHeight']
            weight=request.POST['txtWeight']
            try:
                    Prisoner.objects.filter(id=id).update(name=name,address=address,contact=contact,place=place,height=height,weight=weight)
                    
            except Exception as e:
                    messages.info(request, e)
            else:
                    messages.info(request, 'Data updated successfully')
                    return redirect("/daprisoner")
    data=Prisoner.objects.all()
    return render(request,"daprisonerupdate.html",{"data":data,"d":d})
######################################################################
#                           LOAD PRISONER PAGE
######################################################################
def daprisonerdelete(request):
    id=request.GET.get("id")
    Prisoner.objects.filter(id=id).delete()
######################################################################
#                           LOAD CRIME PAGE
######################################################################
def dacrime(request):
    if(request.POST):
            prisonr=request.POST['prisoner']
            prisonr=Prisoner.objects.get(id=prisonr)
            cellno=request.POST['cellno']
            cellno=Cells.objects.get(id=cellno)
            title=request.POST['txtTitle']
            details=request.POST['txtDetails']
            cdate=request.POST['txtCdate']
            time=request.POST['txtTime']
            hdate=request.POST['txtHdate']
            punishment=request.POST['txtPunishment']
            
            crime_exist=Crime.objects.filter(crimetitle=title).exists()
            if not crime_exist:
                try:
                    r=Crime.objects.create(prisoner=prisonr,cellno=cellno,crimetitle=title,crimedetails=details,crimedate=cdate,crimetime=time,hearingdate=hdate,punishment=punishment,crimestatus='In jail')
                    r.save()
                except Exception as e:
                    messages.info(request, e)
                else:
                    messages.info(request, 'Data added successfully')
            else:
                #duplicate entries occur and registration is not possible
                messages.info(request, 'Data already exist')
    prisoner=Prisoner.objects.all()
    cell=Cells.objects.all()
    data=Crime.objects.all()
    return render(request,"dacrime.html",{"data":data,"prisoner":prisoner,"cell":cell})
######################################################################
#                           LOAD CRIME PAGE
######################################################################
def dacrimeupdate(request):
    id=request.GET.get("id")
    d=Crime.objects.get(id=id)
    if(request.POST):
            
            title=request.POST['txtTitle']
            details=request.POST['txtDetails']
            
            punishment=request.POST['txtPunishment']
            
            try:
                    Crime.objects.filter(id=id).update(crimetitle=title,crimedetails=details,punishment=punishment,crimestatus='In jail')
                    
            except Exception as e:
                    messages.info(request, e)
            else:
                    messages.info(request, 'Data updated successfully')
           
    data=Crime.objects.all()
    return render(request,"dacrimeupdate.html",{"data":data,"d":d})
######################################################################
#                           LOAD CRIME PAGE
######################################################################
def dacrimedelete(request):
    id=request.GET.get("id")
    Crime.objects.get(id=id).delete()
######################################################################
#                           LOAD IN OUT PAGE
######################################################################
def dainout(request):
    if(request.POST):
                prisonr=request.POST['prisoner']
                prisonr=Prisoner.objects.get(id=prisonr)
                date=request.POST['txtDate']
                reason=request.POST['txtReason']
            
            
                try:
                    r=InOut.objects.create(prisoner=prisonr,outdatetime=date,reason=reason,status='Out')
                    r.save()
                except Exception as e:
                    messages.info(request, e)
                else:
                    messages.info(request, 'Data added successfully')
            
    prisoner=Prisoner.objects.all()
    data=InOut.objects.all()
    return render(request,"dainout.html",{"data":data,"prisoner":prisoner})
######################################################################
#                           LOAD IN OUT PAGE
######################################################################
def dainoutupdate(request):
    id=request.GET.get("id")
    d=InOut.objects.get(id=id)
    if(request.POST):
                date=request.POST['txtDate']
                try:
                    InOut.objects.filter(id=id).update(indatetime=date,status='In')
                except Exception as e:
                    messages.info(request, e)
                else:
                    messages.info(request, 'Data updated successfully')
            
   
    return render(request,"dainoutupdate.html")
######################################################################
#                           LOAD PAROLE PAGE
######################################################################
def daparole(request):
    if(request.POST):
                prisonr=request.POST['prisoner']
                prisonr=Prisoner.objects.get(id=prisonr)
                date=request.POST['txtDate']
                days=request.POST['txtDays']
                try:
                    r=Parole.objects.create(prisoner=prisonr,pdate=date,days=days)
                    r.save()
                except Exception as e:
                    messages.info(request, e)
                else:
                    messages.info(request, 'Data added successfully')
            
    prisoner=Prisoner.objects.all()
    data=Parole.objects.all()
    return render(request,"daparole.html",{"data":data,"prisoner":prisoner})
######################################################################
#                           LOAD RELEASE PAGE
######################################################################
def darelease(request):
    if(request.POST):
                prisonr=request.POST['prisoner']
                prisonr=Prisoner.objects.get(id=prisonr)
                date=request.POST['txtDate']
                try:
                    r=Release.objects.create(prisoner=prisonr,reldate=date)
                    r.save()
                except Exception as e:
                    messages.info(request, e)
                else:
                    messages.info(request, 'Data added successfully')
            
    prisoner=Prisoner.objects.all()
    data=Release.objects.all()
    return render(request,"darelease.html",{"data":data,"prisoner":prisoner})
######################################################################
#                           LOAD RELEASE PAGE
######################################################################
def davisitor(request):
    data=Visitor.objects.all()
    return render(request,"davisitor.html",{"data":data})
######################################################################
#                           LOAD RELEASE PAGE
######################################################################
def davisitorupdate(request):
    id=request.GET.get("id")
    status=request.GET.get("status")
    Visitor.objects.filter(id=id).update(status=status)
    return redirect("/davisitor")
######################################################################
#                                                                    #
#                                                                    #
#                          POLICE                                    #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                           LOAD POLICE PAGE
######################################################################
def policehome(request):
    id=request.session["id"]
    d=Police.objects.get(id=id)
    if(request.POST): 
                name=request.POST['txtName']
                address=request.POST['txtAddress']
                contact=request.POST['txtContact']
                email=request.POST['txtEmail']
                try:
                    Police.objects.filter(id=id).update(name=name,address=address,contact=contact,email=email)
                except Exception as e:
                    messages.info(request, e)
                else:
                    messages.info(request, 'Profile updated')
                    return redirect("/policehome")
    return render(request,"policehome.html",{"d":d})
######################################################################
#                           LOAD PRISONER PAGE
######################################################################
def policeprisoner(request):
    data=Prisoner.objects.all()
    return render(request,"policeprisoner.html",{"data":data})
######################################################################
#                           LOAD CRIME PAGE
######################################################################
def policecrime(request):
    data=Crime.objects.all()
    return render(request,"policecrime.html",{"data":data})
######################################################################
#                           LOAD IN OUT PAGE
######################################################################
def policeinout(request):
    if(request.POST):
                prisonr=request.POST['prisoner']
                prisonr=Prisoner.objects.get(id=prisonr)
                date=request.POST['txtDate']
                reason=request.POST['txtReason']
            
            
                try:
                    r=InOut.objects.create(prisoner=prisonr,outdatetime=date,reason=reason,status='Out')
                    r.save()
                except Exception as e:
                    messages.info(request, e)
                else:
                    messages.info(request, 'Data added successfully')
    data=InOut.objects.all()
    return render(request,"policeinout.html",{"data":data})
######################################################################
#                           LOAD PAROLE PAGE
######################################################################
def policeparole(request):
    data=Parole.objects.all()
    return render(request,"policeparole.html",{"data":data})
######################################################################
#                           LOAD RELEASE PAGE
######################################################################
def policerelease(request):
    data=Release.objects.all()
    return render(request,"policerelease.html",{"data":data})
######################################################################
#                           LOAD IN OUT PAGE
######################################################################
def policevisitor(request):
    if(request.POST):
                prisonr=request.POST['prisoner']
                prisonr=Prisoner.objects.get(id=prisonr)
                date=request.POST['txtDate']
                name=request.POST['txtName']
                Relation=request.POST['txtRelation']
                Purpose=request.POST['txtPurpose']
                Carry=request.POST['txtCarry']            
                try:
                    r=Visitor.objects.create(prisoner=prisonr,vdate=date,visitorname=name,relation=Relation,purpose=Purpose,carry=Carry,status='Requested')
                    r.save()
                except Exception as e:
                    messages.info(request, e)
                else:
                    messages.info(request, 'Data added successfully')
    data=Visitor.objects.all()
    prisoner=Prisoner.objects.all()
    return render(request,"policevisitor.html",{"data":data,"prisoner":prisoner})