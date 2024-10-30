from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Employee

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
