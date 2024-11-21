from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader

from .models import Employee
from .forms import add_employee_form

# Create your views here.


def home(request):
    emps = Employee.objects.order_by('name')
    page_num = request.GET.get("page", 1)

    paginator = Paginator(emps, 3)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    page_obj = paginator.get_page(page_num)
    return render(request, 'home.html', {'page_obj': page_obj})


@csrf_exempt
def process_add_emp(request):
    form = add_employee_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            contact = request.POST.get('contact')
            city = request.POST.get('city')

            emp = Employee(name=name, email=email, contact=contact, city=city)
            emp.save()

            return redirect("home")
        return render(request, 'home.html')
    else:
        return HttpResponse("Invalid request method.")


def add_emp(request):
    form = add_employee_form()
    context = {}
    context['form'] = form

    return render(request, 'add_emp.html', context)


def delete_emp(request, idemp):
    emp = Employee.objects.get(pk=idemp)
    emp.delete()
    return redirect("home")


@csrf_exempt
def update_emp(request, idemp):
    emp = Employee.objects.get(pk=idemp)
    if request.method == "POST":
        emp.name = request.POST['name']
        emp.email = request.POST['email']
        emp.contact = request.POST['contact']
        emp.city = request.POST['city']
        emp.save()
        return redirect("home")
    emp = Employee.objects.get(pk=idemp)
    context = {"emp": emp}
    return render(request, "update.html", context)
