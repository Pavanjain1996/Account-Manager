from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from myapp.models import Account, BankAccount
from django.core.mail import EmailMessage

user = None

def index(request):
    return render(request,'Login.html')

def Register(request):
    return render(request,'Register.html')

def Registration(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username=username,password=password,email=email)
    return redirect('/')

def Login(request):
    global user
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return redirect('/Home')
    else:
        return redirect('/')

def Home(request):
    global user
    if user is not None:
        data = Account.objects.all().filter(user=user.username)
        a = len(data)
        data = BankAccount.objects.all().filter(user=user.username)
        b = len(data)
        return render(request,'Home.html',{'data':data,'a':a,'b':b})
    else:
        return render('/')

def Logout(request):
    auth.logout(request)
    return redirect('/')

def findAccount(request):
    account = request.GET['account']
    account = account.capitalize()
    data = Account.objects.all().filter(user=user.username,account__contains=account).order_by('account')
    response = '<span style="font-size:40px;color:#8BDA64;border-bottom:5px solid #8BDA64;padding:5px;">Accounts</span><br/><br/>'
    response += '<hr style="height:4px;background-color:white;"/>'
    j=1
    if len(data) == 0:
        response += '<div class="row" style="font-size:25px;color:#8BDA64;">'
        response += '<div class="col">'
        response += 'No Related Accounts'
        response += '<hr style="height:4px;background-color:white;"/>'
        response += '</div>'
        response += '</div>'
    else:
        for i in data:
            response += '<div class="row" style="font-size:25px;color:#8BDA64;">'
            response += '<div class="col-md-6">'
            response += 'Account : ' + i.account
            response += '</div>'
            response += '<div class="col-md-6">'
            response += 'Username : ' + i.username
            response += '</div>'
            response += '</div>'
            response += '<br/><br/>' 
            response += '<div class="row" style="font-size:25px;color:#8BDA64;">'
            response += '<div class="col-md-4">'
            response += '<button type="button" class="btn btn-primary" id="' + str(i.id) + '" style="background-color:#8BDA64;border:none;width:150px;font-weight:bold;" onclick="sendDetails(this.id)">Send Details</button>'
            response += '</div>'
            response += '<br/><br/>'
            response += '<div class="col-md-4">'
            response += '<button type="button" class="btn btn-primary" id="' + str(i.id) + '" style="background-color:#8BDA64;border:none;width:150px;font-weight:bold;" onclick="deleteAccount(this.id)">Delete Account</button>'
            response += '</div>'
            response += '<br/><br/>'
            response += '<div class="col-md-4">'
            response += '<button type="button" class="btn btn-primary" id="' + str(i.id) + '" style="background-color:#8BDA64;border:none;width:150px;font-weight:bold;" onclick="updateDetails(this.id)">Update Details</button>'
            response += '</div>'
            response += '</div>'
            response += '<hr style="height:4px;background-color:white;"/>'
            j = j + 1
    return HttpResponse(response)

def sendDetails(request):
    global user
    aid = request.GET['id']
    data = Account.objects.all().filter(id=aid)
    content = ''
    for i in data:
        content += 'Account : ' + i.account + ' \nUsername : ' + i.username + ' \nPassword : ' + i.password + ' \nPIN : ' + i.pin
    try:
        email = EmailMessage('Account Details',content,to=[user.email])
        email.send()
        return HttpResponse('Email Sent')
    except:
        return HttpResponse('Email Not Sent')

def addAccount(request):
    name = request.GET['name']
    username = request.GET['username']
    password = request.GET['password']
    pin = request.GET['pin']
    account = Account(user=user.username,account=name, username=username, password=password, pin=pin)
    try:
        account.save()
        return HttpResponse('Account Created')
    except:
        return HttpResponse('Account Not Created')

def deleteAccount(request):
    aid = request.GET['id']
    data = Account.objects.all().filter(id=aid)
    try:
        for i in data:
            i.delete()
        return HttpResponse('Account Deleted')
    except:
        return HttpResponse('Account Not Deleted')

def updateAccount(request):
    aid = request.GET['id']
    data = Account.objects.get(id=aid)
    response = '<hr style="height:4px;background-color:white;"/><div class="input-group mb-3">'
    response += '<br/><br/>'
    response += '<div class="input-group-prepend">'
    response += '<span class="input-group-text" id="basic-addon1" style="background:none;border:none;"><span style="color:#8BDA64;font-size:30px;">N</span></span>'
    response += '</div>'
    response += '<input type="text" class="form-control" id="name1" placeholder="Account Name" style="background:none;border:none;border-bottom:4px solid #8BDA64;font-size:25px;color:white;" value="' + data.account + '">'
    response += '</div><br/>'
    response += '<div class="input-group mb-3">'
    response += '<div class="input-group-prepend">'
    response += '<span class="input-group-text" id="basic-addon1" style="background:none;border:none;"><span style="color:#8BDA64;font-size:30px;">U</span></span>'
    response += '</div>'
    response += '<input type="text" class="form-control" id="username1" placeholder="Account Username" style="background:none;border:none;border-bottom:4px solid #8BDA64;font-size:25px;color:white;" value="' + data.username + '">'
    response += '</div><br/>'
    response += '<div class="input-group mb-3">'
    response += '<div class="input-group-prepend">'
    response += '<span class="input-group-text" id="basic-addon1" style="background:none;border:none;"><span style="color:#8BDA64;font-size:30px;">P</span></span>'
    response += '</div>'
    response += '<input type="text" class="form-control" id="password1" placeholder="Account Password" style="background:none;border:none;border-bottom:4px solid #8BDA64;font-size:25px;color:white;" value="' + data.password + '">'
    response += '</div><br/>'
    response += '<div class="input-group mb-3">'
    response += '<div class="input-group-prepend">'
    response += '<span class="input-group-text" id="basic-addon1" style="background:none;border:none;"><span style="color:#8BDA64;font-size:30px;">P</span></span>'
    response += '</div>'
    response += '<input type="text" class="form-control" id="pin1" placeholder="Account PIN" style="background:none;border:none;border-bottom:4px solid #8BDA64;font-size:25px;color:white;" value="' + data.pin + '">'
    response += '</div><br/>'
    response += '<button type="button" class="btn btn-primary" style="background-color:#8BDA64;border:none;font-weight:bold;" id=' + str(data.id) + ' onclick="updateIt(this.id)">Update Account Details</button>'
    response += '<br/><br/>'
    response += '<hr style="height:4px;background-color:white;"/><div class="input-group mb-3">'
    return HttpResponse(response)

def updateIt(request):
    aid = request.GET['id']
    name = request.GET['name']
    username = request.GET['username']
    password = request.GET['password']
    pin = request.GET['pin']
    data = Account.objects.get(id=aid)
    data.account = name
    data.username = username
    data.password = password
    data.pin = pin
    data.save()
    return HttpResponse('Details Updated')

def getBankAccountDetails(request):
    global user
    aid = request.GET['id']
    data = BankAccount.objects.all().filter(id=aid,user=user.username)
    content = ''
    for i in data:
        content += 'Bank : ' + i.bank + ' \nAccount Holder : ' + i.name + ' \nAccount No. : ' + i.account_no + ' \nIFSC Code : ' + i.IFSC + ' \nATM Card Number : ' + i.atm_card_no + ' \nCVV : ' + i.cvv + ' \nATM Pin : ' + i.atm_pin + ' \nExpiry Date : ' + i.card_expiry + ' \nNet Banking Id : ' + i.net_banking_id + ' \nSign In Password : ' + i.signin_password + ' \nTransaction Password : ' + i.transaction_password + ' \nMobile Banking Pin : ' + i.mob_banking_pin
    try:
        email = EmailMessage('Account Details',content,to=[user.email])
        email.send()
        return HttpResponse('Email Sent')
    except:
        return HttpResponse('Email Not Sent')

def addBankAccount(request):
    global user
    a = request.POST['name']
    b = request.POST['bank']
    c = request.POST['account_no']
    d = request.POST['IFSC']
    e = request.POST['atm_card_no']
    f = request.POST['cvv']
    g = request.POST['atm_pin']
    h = request.POST['card_expiry']
    i = request.POST['net_banking_id']
    j = request.POST['signin_password']
    k = request.POST['transaction_password']
    l = request.POST['mob_banking_pin']
    account = BankAccount(user=user.username,name=a,bank=b,account_no=c,IFSC=d,atm_card_no=e,cvv=f,atm_pin=g,card_expiry=h,net_banking_id=i,signin_password=j,transaction_password=k,mob_banking_pin=l)
    account.save()
    return redirect('/Home')

def deleteBankAccount(request,aid):
    data = BankAccount.objects.get(id=aid)
    data.delete()
    return redirect('/Home')
