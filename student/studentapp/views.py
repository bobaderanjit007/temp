from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import stud

# Create your views here.

def test(request):
    return render(request, 'test.html')

def create(request):
    if request.method == "GET":
        return render(request, 'create.html')
    else:
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("number")
        password = request.POST.get("password")

        # Create an instance of the model and save it to the database
        new_entry = stud(name=name, email=email, mobile=mobile, password=password)
        new_entry.save()

        messages.success(request, f"{name} Student entered successfuly!")

        return redirect("/")

def student(request):
    students = stud.objects.all()
    if request.method == 'GET':
        sname = request.GET.get("search")
        if sname != None:
            students = stud.objects.filter(name__icontains = sname)


    return render(request, "students.html", {'students': students})


def update(request, id):
    student = stud.objects.get(id=id)

    if request.method == "POST":
       data = request.POST

       name = data.get('name')
       email = data.get('email')
       mobile = data.get('number')
       password = data.get('password')

       student.name = name
       student.email = email
       student.mobile = mobile
       student.password = password

       student.save()
        
       messages.info(request,f"{name} Updated Successfuly !")
       return redirect("/")

    return render(request, 'update.html',{'student': student})

def delete(request, id):
    student = stud.objects.get(id=id)
    student.delete()

    messages.success(request, f"{student.name} Deleted successfuly!")

    return redirect("/")

