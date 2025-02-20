from django.shortcuts import render
from AdminApp.models import DesignCategoryDb, DesignsDb
# Create your views here.
def category_page(request):
    data = DesignCategoryDb.objects.all()
    return render(request, "category.html", {'data': data})


def filter_design(request, ct_name):
    item = DesignsDb.objects.filter(Category=ct_name)
    return render(request, "design_page.html", {'item': item})
