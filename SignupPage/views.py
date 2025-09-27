from django.shortcuts import redirect, render
from .models import Usersignup
from django.contrib.auth import logout
# pages
from django.core.paginator import Paginator
# Create your views here.
def Signuppage(request):
    if request.method == "POST":
        username = request.POST.get("firstName")
        email = request.POST.get("email")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirmPassword")
        if password == confirmPassword:
            user = Usersignup(Firstname=username, email=email, age=int(age), gender=gender,password=password)
            user.save()
            return redirect('/users/Login')
        else:
            message = ["Cannot Sign check the password and come again"]
            return render(request, r'Success/Error.html', {"Message": message})
    else:
        return render(request, r'Signuppage/Signup.html')


def Signin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = Usersignup.objects.get(email=email, password=password)
            return redirect('/')
        except:
            message = ["Cannot Sign check the password and come again"]
            return render(request, r'Success/Error.html', {"Message": message})
    else:
        return render(request, r'LoginHtml/LoginPage.html')

def Logoutuser(request):
    logout(request)
    return redirect('/users/Login')

def Datatable(request):
    data = Usersignup.objects.all()
    #setup paginator
    p = Paginator(object_list=data, per_page=10)
    page = request.GET.get('page')
    venues = p.get_page(page)

    return render(request, r'Data/TableData.html', {"Data":data, "venus":venues})