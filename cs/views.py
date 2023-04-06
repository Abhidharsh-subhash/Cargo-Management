from datetime import date
from turtle import rt
from urllib import response
from django.shortcuts import redirect, render
from django.http import request
from .models import login as log,employee as emp,vehicle as veh,couriertype as cor,cargo as co,route as re,allotedjobs as aj

# Create your views here.
def adminhome(request):
    msg=request.GET.get("msg","")
    return render(request,"adminhome.html",{"msg":msg})

def employeehome(request):
    msg=request.GET.get("msg","")
    return render(request,"employeehome.html",{"msg":msg})

def ademployeelist(request):
    msg=request.GET.get("msg","")
    dataemp=emp.objects.all()
    return render(request,"ademployeelist.html",{"dataemp":dataemp,"msg":msg})

def advehiclelist(request):
    msg=request.GET.get("msg","")
    dataveh=veh.objects.all()
    return render(request,"advehiclelist.html",{"dataveh":dataveh,"msg":msg})

def adcargotypelist(request):
    msg=request.GET.get("msg","")
    datac=cor.objects.all()
    return render(request,"adcargotypelist.html",{"datac":datac,"msg":msg})

def adcargolist(request):
    msg=request.GET.get("msg","")
    dataca=co.objects.all()
    return render(request,"adcargolist.html",{"dataca":dataca,"msg":msg})

def adroutelist(request):
    msg=request.GET.get("msg","")
    datar=re.objects.all()
    return render(request,"adroutelist.html",{"datar":datar,"msg":msg})

def index(request):
    msg=request.GET.get("msg","")
    return render(request,"index.html",{"msg":msg})

def employee(request):
    if request.POST:
        name=request.POST["name"]
        address=request.POST["address"]
        gender=request.POST["gender"]
        mobileno=request.POST["mobileno"]
        place=request.POST["place"]
        email=request.POST["email"]
        password=request.POST["password"]
        log.objects.create(username=name,password=password,role="employee")
        datal=log.objects.last()
        emp.objects.create(login=datal,name=name,address=address,gender=gender,mobileno=mobileno,place=place,email=email)
        
        response=redirect("/adnewemployee?msg=Employee registration successfull")
        return response
    else:
        response=redirect("/adnewemployee?msg=Employee registration failed")
        return response

def adnewemployee(request):
    msg=request.GET.get("msg","")
    return render(request,"adnewemployee.html",{"msg":msg})

def deleteempl(request):
    id=request.POST["empid"]
    employee = emp.objects.get(employeeid=id)
    logid = str(employee.login.logid)
    emp.objects.filter(employeeid=id).delete()
    log.objects.filter(logid=logid).delete()
    response=redirect("/ademployeelist?msg=Employee deleted successfully")
    return response 

def editempl(request):
    b1=request.GET["c"]
    data=emp.objects.get(employeeid=b1)
    return render(request,"editsempl.html",{"d":data})

def editsempl(request):
    c=request.GET["c"]
    t1=request.POST["t1"]
    t2=request.POST["t2"]
    t3=request.POST["t3"]
    t4=request.POST["t4"]
    t5=request.POST["t5"]
    emp.objects.filter(employeeid=c).update(name=t1,email=t2,mobileno=t3,address=t4,place=t5)
    response = redirect("/ademployeelist/?msg=updated successfully")
    return response

def adnewvehicle(request):
    msg=request.GET.get("msg","")
    return render(request,"adnewvehicle.html",{"msg":msg})

def vehicle(request):
    if request.POST:
        vehiclename=request.POST["vehiclename"]
        registrationno=request.POST["registrationno"]
        source=request.POST["source"]
        destination=request.POST["destination"]
        capacity=request.POST["capacity"]
        date=request.POST["date"]
        veh.objects.create(vehiclename=vehiclename,registrationno=registrationno,source=source,destination=destination,capacity=capacity,date=date)
        response=redirect("/adnewvehicle?msg=New vehicle added")
        return response
    else:
        response=redirect("/adnewvehicle?msg=vehicle adding failed")
        return response

def deleteveh(request):
    id=request.POST['veid']
    veh.objects.filter(vehicleid=id).delete()
    response=redirect("/advehiclelist?msg=Vehicle deleted successfully")
    return response

def editvehicle(request):
    b1=request.GET["c"]
    data=veh.objects.get(vehicleid=b1)
    return render(request,"editsvehicle.html",{"d":data})

def editsvehicle(request):
    c=request.GET["c"]
    t1=request.POST["t1"]
    t2=request.POST["t2"]
    t3=request.POST["t3"]
    t4=request.POST["t4"]
    t5=request.POST["t5"]
    veh.objects.filter(vehicleid=c).update(vehiclename=t1,registrationno=t2,source=t3,destination=t4,capacity=t5)
    response = redirect("/advehiclelist/?msg=updated successfully")
    return response


def adcargotype(request):
    msg=request.GET.get("msg","")
    return render(request,"adcargotype.html",{"msg":msg})

def cargotype(request):
    if request.POST:
        courier=request.POST["courier"]
        cor.objects.create(courier=courier)
        response=redirect("/adcargotype?msg=New cargotype added")
        return response
    else:
        response=redirect("/adcargotype?msg=addition of new cargotype failed")
        return response

def deletecor(request):
    id=request.POST['crid']
    cor.objects.filter(couriertypeid=id).delete()
    response=redirect("/adcargotypelist?msg=cargotype deleted successfully")
    return response

def editctype(request):
    b1=request.GET["c"]
    data=cor.objects.get(couriertypeid=b1)
    return render(request,"editsctype.html",{"d":data})

def editsctype(request):
    c=request.GET["c"]
    t1=request.POST["t1"]
    cor.objects.filter(couriertypeid=c).update(courier=t1)
    response = redirect("/adcargotypelist/?msg=updated successfully")
    return response

def adcargo(request):
    msg=request.GET.get("msg","")
    data=cor.objects.all()
    return render(request,"adcargo.html",{"data":data,"msg":msg})

def cargo(request):
    if request.POST:
        couriertype=request.POST["couriertype"]
        weight=request.POST["weight"]
        price=request.POST["price"]
        paymenttype=request.POST["paymenttype"]
        fromaddress=request.POST["fromaddress"]
        toaddress=request.POST["toaddress"]
        landmark=request.POST["landmark"]
        sendingdate=request.POST["sendingdate"]
        currentdate=request.POST["currentdate"]
        datadt=cor.objects.get(couriertypeid=couriertype)
        co.objects.create(couriertypeid=datadt,weight=weight,price=price,paymenttype=paymenttype,fromaddress=fromaddress,toddress=toaddress,landmark=landmark,sendingdate=sendingdate,currentdate=currentdate)
        response=redirect("/adcargo?msg=New courier added")
        return response
    else:
        response=redirect("/adcargo?msg=Adding new courier failed")
        return response

def deletecar(request):
    id=request.POST['carid']
    co.objects.filter(cargoid=id).delete()
    response=redirect("/adcargolist?msg=Cargo deleted successfully")
    return response

def adroute(request):
    msg=request.GET.get("msg","")
    data=veh.objects.all()
    dataem=emp.objects.all()
    return render(request,"adroute.html",{"data":data,"dataem":dataem,"msg":msg})

def route(request):
    if request.POST:
        vehicle=request.POST["vehicle"]
        employee=request.POST["employee"]
        route=request.POST["route"]
        date=request.POST["date"]
        datav=veh.objects.get(vehicleid=vehicle)
        datae=emp.objects.get(employeeid=employee)
        re.objects.create(vehicle=datav,employee=datae,route=route,date=date)
        response=redirect("/adroute?msg=New route added successfully")
        return response
    else:
        response=redirect("/adroute?msg=Insertion failed")
        return response

def deletert(request):
    id=request.POST['rtid']
    re.objects.filter(routeid=id).delete()
    response=redirect("/adroutelist?msg=Deleted successfully")
    return response

def editrt(request):
    b1=request.GET["c"]
    data=re.objects.get(routeid=b1)
    return render(request,"editsrt.html",{"d":data})

def editsrt(request):
    c=request.GET["c"]
    t1=request.POST["t1"]
    t2=request.POST["t2"]
    re.objects.filter(routeid=c).update(route=t1,date=t2)
    response = redirect("adroutelist/?msg=updated successfully")
    return response

def completedjobs(request):
    datat=aj.objects.filter(status="completed")
    return render(request,"completedjobs.html",{"datat":datat})

def allotedjobs(request):
    data=emp.objects.all()
    dataem=cor.objects.all()
    msg=request.GET.get("msg","")
    return render(request,"allotedjobs.html",{"data":data,"dataem":dataem,"msg":msg})

def allot(request):
    if request.POST:
        employee=request.POST["employee"]
        couriertype=request.POST["couriertype"]
        date=request.POST["date"]
        comments=request.POST["comments"]
        datav=emp.objects.get(employeeid=employee)
        datae=cor.objects.get(couriertypeid=couriertype)
        aj.objects.create(employee=datav,couriertypeid=datae,date=date,comments=comments,status="waiting")
        response=redirect("/allotedjobs?msg= Job allotted successfully")
        return response
    else:
        response=redirect("/allotedjobs?msg=Job allocation failed")
        return response

def logout(request):
    try:
        del request.session['id']
        del request.session['role']
        del request.session['username']
        response = redirect("/index?id=logout")
        return response
    except:
        response = redirect("/index?id=logout")
        return response

def adchange(request):
    msg=request.GET.get("msg","")
    return render(request,"adchange.html",{"msg":msg})

def adpsw(request):
    if request.POST:
        old=request.POST["old"]
        password=request.POST["password"]
        id=request.session['id']
        role=request.session['role']

        datac=log.objects.filter(password=old,role=role).count()
        if datac==1:
            log.objects.filter(logid=id).update(password=password)
            response=redirect("/adminhome?msg=Password updated successfully")
            return response
        else:
            response=redirect("/adchange?msg=invalid username or password")
            return response
    else:
        response=redirect("/adchange?msg=Something went wrong")
        return response

def login(request):
    if request.POST:
        user = request.POST["username"]
        password = request.POST["password"]
        try:
            datac = log.objects.filter(username=user, password=password).count()
            if datac==1:
                data=log.objects.get(username=user, password=password)
                if data.role=="admin":
                    request.session['username'] = data.username
                    request.session['role'] = data.role
                    request.session['id'] = data.logid
                    response = redirect('/adminhome?msg=welcome admin')
                    return response
                elif data.role=="employee":
                    request.session['username'] = data.username
                    request.session['role'] = data.role
                    request.session['id'] = data.logid
                    response = redirect('/employeehome?msg=Welcome employee')
                    return response
                else :
                    response = redirect('/index?msg=invalid access')
                    return response


            else:
                response = redirect('/index?msg=invalid username or password')
                return response
               
        except:
            response = redirect('/index?msg=something went wrong')
            return response
    else:
        response = redirect('/index?msg=exception occured')
        return response

def empchange(request):
    msg=request.GET.get("msg","")
    return render(request,"empchange.html",{"msg":msg})

def usrpsw(request):
    if request.POST:
        old=request.POST["old"]
        password=request.POST["password"]
        id=request.session['id']
        role=request.session['role']

        datac=log.objects.filter(password=old,role=role).count()
        if datac==1:
            log.objects.filter(logid=id).update(password=password)
            response=redirect("/employeehome?msg=Password updated successfully")
            return response
        else:
            response=redirect("/empchange?msg=invalid username or password")
            return response
    else:
        response=redirect("/empchange?msg=Something went wrong")
        return response

def empprofile(request):
    id=request.session['id']
    datal=log.objects.get(logid=id)
    datapf=emp.objects.filter(login=datal).all()
    return render(request,"empprofile.html",{"datapf":datapf})

def editprofile(request):
    b1=request.GET["c"]
    data=emp.objects.get(employeeid=b1)
    return render(request,"editsprofile.html",{"d":data})

def editsprofile(request):
    c=request.GET["c"]
    if request.POST:
        t1=request.POST["t1"]
        t2=request.POST["t2"]
        t3=request.POST["t3"]
        t4=request.POST["t4"]
        t5=request.POST["t5"]
        emp.objects.filter(employeeid=c).update(name=t1,mobileno=t2,address=t3,email=t4,place=t5)
    response = redirect("/employeehome/?msg= Profile updated successfully")
    return response

def newjobs(request):
    logid=request.session["id"]
    userid=emp.objects.get(login=logid)
    datan=aj.objects.filter(employee=userid.employeeid,status="waiting")
    return render(request,"newjobs.html",{"datan":datan})

def emcompletedjobs(request):
    logid=request.session["id"]
    userid=emp.objects.get(login=logid)
    datam=aj.objects.filter(employee=userid.employeeid,status="completed")
    return render(request,"emcompletedjobs.html",{"datam":datam})

def routes(request):
    logid=request.session["id"]
    userid=emp.objects.get(login=logid)
    datar=re.objects.filter(employee=userid.employeeid)
    return render(request,"routes.html",{"datar":datar})

def ongoing(request):
    logid=request.session["id"]
    userid=emp.objects.get(login=logid)
    datae=aj.objects.filter(employee=userid.employeeid,status="accepted")
    return render(request,"ongoing.html",{"datae":datae})

def editcargo(request):
    b1=request.GET["c"]
    data=co.objects.get(cargoid=b1)
    return render(request,"editscargo.html",{"d":data})

def editscargo(request):
    c=request.GET["c"]
    t1=request.POST["t1"]
    t2=request.POST["t2"]
    t3=request.POST["t3"]
    t4=request.POST["t4"]
    t5=request.POST["t5"]
    co.objects.filter(cargoid=c).update(weight=t1,price=t2,fromaddress=t3,toddress=t4,landmark=t5)
    response = redirect("/adcargolist?msg=updated successfully")
    return response

def allotjobs(request):
    dataaj=aj.objects.all()
    return render(request,"allotjobs.html",{"dataaj":dataaj})

def deleteallot(request):
    id=request.POST['alid']
    aj.objects.filter(allotedjobsid=id).delete()
    response=redirect("/allotjobs?msg=Deleted successfully")
    return response

def editallot(request):
    b1=request.GET["c"]
    data=aj.objects.get(allotedjobsid=b1)
    return render(request,"editsallot.html",{"d":data})

def editsallot(request):
    c=request.GET["c"]
    t1=request.POST["t1"]
    t2=request.POST["t2"]
    aj.objects.filter(allotedjobsid=c).update(date=t1,comments=t2)
    response = redirect("allotjobs/?msg=updated successfully")
    return response

def accept(request):
   id=request.POST["alid"]
   aj.objects.filter(allotedjobsid=id).update(status="accepted")
   response=redirect("/newjobs/?msg= Job accepted")
   return response

def reject(request):
   id=request.POST["reid"]
   aj.objects.filter(allotedjobsid=id).update(status="rejected")
   response=redirect("/newjobs/?msg= Job rejected")
   return response
    
def complete(request):
   id=request.POST["coid"]
   aj.objects.filter(allotedjobsid=id).update(status="completed")
   response=redirect("ongoing/?msg= Job completed")
   return response

def rejected(request):
    logid=request.session["id"]
    userid=emp.objects.get(login=logid)
    dataj=aj.objects.filter(employee=userid.employeeid,status="rejected")
    return render(request,"rejected.html",{"dataj":dataj})
   
def adongoing(request):
    datad=aj.objects.filter(status="accepted").all()
    return render(request,"adongoing.html",{"datad":datad})

def adrejected(request):
    datar=aj.objects.filter(status="rejected").all()
    return render(request,"adrejected.html",{"datar":datar})


