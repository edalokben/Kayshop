from django.shortcuts import render
from django.http import HttpResponse
from .models import Footwear
from .models import Bottom
from .models import Top
from .models import Accessorie


def index(request):
    footwears = Footwear.objects.all()
    bottoms = Bottom.objects.all()
    tops = Top.objects.all()
    accessories = Accessorie.objects.all()
    context = {"footwears": footwears, "bottoms": bottoms, "tops": tops, "accessories": accessories}
    return render(request, "index.html", context)