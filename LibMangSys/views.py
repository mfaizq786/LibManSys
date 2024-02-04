from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from LibMangSys.models import Issuedbook, StudentRegistration,Book
from django.contrib.sessions.models import Session
from datetime import date
from django.http import HttpResponseRedirect
# Create your views here
def index(request):
    if request.session.has_key('is_logged'):
        return redirect('administrator')
    if request.session.has_key('is_studlogged'):
        return redirect('stud-panel')   
    if request.POST:
        user = request.POST.get('user') 
        passw = request.POST.get('pass')
        if user == "admin" and passw == "admin":
            request.session['is_logged'] = True
            return redirect('administrator')
        else:
            messages.error(request,'Invalid Username or Password')  
            return redirect('index')  
    return render(request,'LibMangSys/Library Management/index.html')

def studlogin(request):
    username = request.POST['username']
    password = request.POST['password']
    objcount = StudentRegistration.objects.filter(username=username).count()
    if username == "" or password == "":
        messages.error(request,'Invalid username or password ....')
        return redirect('index')
    elif objcount > 0:
        obj = StudentRegistration.objects.get(username=username)
        if username==obj.username and password==obj.password:
            request.session['is_studlogged'] = True
            request.session['check'] = True
            request.session['studid'] = obj.id
            messages.success(request,'Login Successfully....')
            return redirect('stud-panel')
        else:
            messages.error(request,'Check your password and relogin....')
            return redirect('index')
    else:
        messages.error(request,'Invalid username or password ....')
        return redirect('index')


def studpanel(request):
    if request.session.has_key('is_studlogged'):
        if request.POST:
            studid = request.session['studid'] 
            issueid = request.POST.get('id')
            print(issueid)
            obj = StudentRegistration.objects.get(id=studid)
            issuebook2 = Issuedbook.objects.get(id=issueid)                
            y = issuebook2.returndate
            counttodaydate = date.today().strftime('%j')
            returncount = y.strftime('%j')
            if counttodaydate > returncount:
                daylate = int(counttodaydate) - int(returncount)
                fine = daylate * 5
            else:
                daylate = 0
                fine = 0
            print(daylate,fine,sep="  ")    
            Issuedbook.objects.filter(id=issueid).update(fine=fine,latedays=daylate)
            issuebook = Issuedbook.objects.filter(studid=obj) 
            count = Issuedbook.objects.filter(studid=obj).count()
            messages.info(request,'You have ' + str(daylate) + ' days late and Your fine is ' + str(fine) +' Rupees')
            return redirect('stud-panel')
        studid = request.session['studid']    
        obj = StudentRegistration.objects.get(id=studid)
        issuebook = Issuedbook.objects.filter(studid=obj)
        count = Issuedbook.objects.filter(studid=obj).count()
        return render(request,'LibMangSys/Library Management/studentpanel.html',{'data':obj,'issuebook':issuebook,'issuecount':count})
    return redirect('index')    

def fine(request):
    if request.session.has_key('is_logged'):
        if request.POST:
            studid = request.session['studid'] 
            issueid = request.POST.get('id')
            print(issueid)
            obj = StudentRegistration.objects.get(id=studid)
            issuebook2 = Issuedbook.objects.get(id=issueid)                
            y = issuebook2.returndate
            counttodaydate = date.today().strftime('%j')
            returncount = y.strftime('%j')
            if counttodaydate > returncount:
                daylate = int(counttodaydate) - int(returncount)
                fine = daylate * 5
            else:
                daylate = 0
                fine = 0    
            Issuedbook.objects.filter(id=issueid).update(fine=fine,latedays=daylate)
            issuebook = Issuedbook.objects.filter(studid=obj) 
            count = Issuedbook.objects.filter(studid=obj).count()
            messages.info(request,'You have ' + str(daylate) + ' days late and Your fine is ' + str(fine) + ' Rupees')
            return redirect('issued-book')
        studid = request.session['studid']    
        obj = StudentRegistration.objects.get(id=studid)
        issuebook = Issuedbook.objects.filter(studid=obj)
        count = Issuedbook.objects.filter(studid=obj).count()
        return render(request,'LibMangSys/Library Management/viewissuedbook.html',{'data':obj,'issuebook':issuebook,'issuecount':count})
    return redirect('index')


def viewstuddetails(request):
    data = StudentRegistration.objects.all()
    count = StudentRegistration.objects.all().count()
    # edit = StudentRegistration.objects.get(id=id)
    return render(request,'LibMangSys/Library Management/viewstuddetails.html',{"Sdata":data,"studentcount":count})

def editstudent(request,id):  
    if request.session.has_key('is_logged'):
        edit = StudentRegistration.objects.get(id=id)
        if request.POST:
            fname = request.POST.get('firstname') 
            lname = request.POST.get('lastname')
            enroll = request.POST.get('EnrollNo')
            branch = request.POST.get('branch')
            username = request.POST.get('username')
            password = request.POST.get('password')
            StudentRegistration.objects.filter(id=id).update(fname=fname,lname=lname,enrollno=enroll,branch=branch,username=username,password=password)
            messages.success(request,'Data Updated Successfully....')
            return redirect('stud-detail')
        return render(request,'LibMangSys/Library Management/editstud.html',{"Edata":edit}) 
    return redirect('index')

def administrator(request):
    stud = StudentRegistration.objects.all()
    books = Book.objects.all()
    
    if request.session.has_key('is_studlogged') and request.session.has_key('check'):
        return redirect('stud-panel')               
    elif request.session.has_key('is_logged'):
        if request.POST:
            fname = request.POST.get('firstname') 
            lname = request.POST.get('lastname')
            enroll = request.POST.get('EnrollNo')
            branch = request.POST.get('branch')
            profile = request.FILES.get('imgupload')
            username = request.POST.get('username')
            password = request.POST.get('password')
            std = StudentRegistration(fname=fname,lname=lname,enrollno=enroll,branch=branch,image=profile,username=username,password=password)
            std.save()
            messages.success(request,'Data Inserted Successfully....')
            return redirect('administrator')
        return render(request,'LibMangSys/Library Management/administrator.html',{'stud':stud,'books':books}) 
    return redirect('index')        

def studregistration(request):
    if request.POST:
        fname = request.POST.get('firstname') 
        lname = request.POST.get('lastname')
        enroll = request.POST.get('EnrollNo')
        branch = request.POST.get('branch')
        profile = request.FILES.get('imgupload')
        username = request.POST.get('username')
        password = request.POST.get('password')
        std = StudentRegistration(fname=fname,lname=lname,enrollno=enroll,branch=branch,image=profile,username=username,password=password)
        std.save()
        messages.success(request,'Data Inserted Successfully....')
        return redirect('index')
    return render(request,'LibMangSys/Library Management/index.html') 



def deletestudent(request):
    if request.POST:
        enon = request.POST.get('enroll')
        obj = StudentRegistration.objects.filter(enrollno=enon)        
        if obj.count() > 0:
            obj.delete()
            messages.success(request,'Data Deleted Successfully....')
        else: 
            messages.success(request,'Enrollment no is Invalid')    
        return redirect('administrator')
    elif request.GET:
        enon = request.GET.get('id')
        obj = StudentRegistration.objects.filter(id=enon)
        len = StudentRegistration.objects.filter(id=enon).count()        
        if len > 0:
            obj.delete()
            messages.success(request,'Data Deleted Successfully....')
            return redirect('stud-detail')
        else: 
            messages.success(request,'not-deleted')    
        return redirect('stud-detail')

    return render(request,'LibMangSys/Library Management/administrator.html')    

def logout(request):
    if request.session.has_key('is_logged'):
        del request.session['is_logged']
        messages.success(request,'Logged out successfully')
    elif request.session.has_key('is_studlogged'):
        del request.session['is_studlogged']
        del request.session['check']    
        messages.success(request,'Logged out successfully')
    return redirect('index') 

def addbook(request):
    if request.session.has_key('is_logged'):
        if request.POST:
            bookname = request.POST.get('bookname') 
            author = request.POST.get('author')
            bookno = request.POST.get('bookno')
            category = request.POST.get('category')
            quantity = request.POST.get('quantity')
            book = Book(bookname=bookname,authorname=author,bookno=bookno,category=category,quantity=quantity)
            book.save()
            messages.success(request,'Book Inserted Successfully....')
            return redirect('administrator')
        return render(request,'LibMangSys/Library Management/administrator.html') 
    return redirect('index') 

def viewallbooks(request):
    data = Book.objects.all()
    count = Book.objects.all().count()
    return render(request,'LibMangSys/Library Management/viewallbooks.html',{"bookdata":data,"bookcount":count})  

def editbook(request,id):  
    if request.session.has_key('is_logged'):
        edit = Book.objects.get(id=id)
        if request.POST:
            bookname = request.POST.get('bookname') 
            author = request.POST.get('author')
            bookno = request.POST.get('bookno')
            category = request.POST.get('category')
            quantity = request.POST.get('quantity')
            Book.objects.filter(id=id).update(bookname=bookname,authorname=author,bookno=bookno,category=category,quantity=quantity)
            messages.success(request,'Book Data Updated Successfully....')
            return redirect('view-all-books')
        return render(request,'LibMangSys/Library Management/editbook.html',{"bookdata":edit}) 
    return redirect('index')

def deletebook(request):
    if request.POST:
        enon = request.POST.get('bookno')
        obj = Book.objects.filter(bookno=enon)        
        if obj.count() > 0:
            obj.delete()
            messages.success(request,'Data Deleted Successfully....')
        else: 
            messages.success(request,'Book No is Invalid')    
        return redirect('administrator')
    elif request.GET:
        bookid = request.GET.get('id')
        obj = Book.objects.filter(id=bookid)
        len = Book.objects.filter(id=bookid).count()        
        if len > 0:
            obj.delete()
            messages.success(request,'Data Deleted Successfully....')
            return redirect('view-all-books')
        else: 
            messages.success(request,'not-deleted')    
        return redirect('view-all-books')

    return render(request,'LibMangSys/Library Management/administrator.html')

def issuebook(request):
    if request.POST:
        studenroll = request.POST.get('enrollno')
        bookno = request.POST.get('bookno')
        studdata = StudentRegistration.objects.get(enrollno=studenroll)
        bookdata = Book.objects.get(bookno=bookno)
        issuebookcount = Issuedbook.objects.filter(enrollmentno=studenroll).count()
        if issuebookcount < 5:
            issuebook = Issuedbook(studid=studdata,bookid=bookdata,enrollmentno=studenroll,bookno=bookno)
            issuebook.save()
            messages.success(request,"Book Issue Successfully....")
        else:
            messages.error(request,"You have already Issued 5 books so firstly return your books ....")   
        return redirect('administrator')

def viewissuedbook(request):
    obj = Issuedbook.objects.all()
    count = Issuedbook.objects.all().count()
    return render(request,'LibMangSys/Library Management/viewissuedbook.html',{'issuebook':obj,'issuecount':count})  

def returnbook(request):
    if request.POST:
        enrollno = request.POST.get('enroll')
        bookno = request.POST.get('bookno')
        obj = Issuedbook.objects.get(enrollmentno=enrollno,bookno=bookno)
        count = Issuedbook.objects.filter(enrollmentno=enrollno,bookno=bookno).count()
        if count == 0:
            messages.success(request,'You have entered wrong Enrollment No or BookNo....')
            return redirect('administrator')
        else:
            books = Book.objects.get(bookno=bookno)
            Book.objects.filter(bookno=bookno).update(quantity=books.quantity-1)
            obj.delete()
            messages.success(request,'Data Deleted Successfully....')
            return redirect('administrator')    
    
    elif request.GET:
        bookissueid = request.GET.get('id')
        bookno = request.GET.get('bookno')
        obj = Issuedbook.objects.get(id=bookissueid)
        len = Issuedbook.objects.filter(id=bookissueid).count()        
        if len == 0:
            messages.success(request,'Data Not Deleted....')
            return redirect('issued-book')
        else:
            books = Book.objects.get(bookno=bookno) 
            Book.objects.filter(bookno=bookno).update(quantity=books.quantity-1)
            obj.delete() 
            messages.success(request,'Data Deleted Successfully..')    
        return redirect('issued-book')
