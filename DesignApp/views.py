from django.shortcuts import render
from AdminApp.models import DesignCategoryDb, DesignsDb
# Create your views here.
def category_page(request):
    data = DesignCategoryDb.objects.all()
    return render(request, "category.html", {'data': data})


def filter_design(request, ct_name):
    data = DesignsDb.objects.filter(Category=ct_name)
    name = ct_name
    return render(request, "design_page.html", {'data': data, 'name': name})


def design_single(request, d_id):
    item = DesignsDb.objects.get(id=d_id)
    return render(request, "design_single.html", {'item': item})

