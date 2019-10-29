from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .forms import *
# list = [
#
# ]



def index(request):
    return render(request, 'inv/index.html')

def start(request):
    return render(request, 'inv/project_start.html')

def display_successFactor(request):
    items = SuccessFactor.objects.all()
    context = {
        'items': items,
        'header': 'Laptops',
    }
    return render(request, 'inv/index.html', context)


def display_performanceIndicator(request):
    items = PerformanceIndicator.objects.all()
    context = {
        'items': items,
        'header': 'Desktops',
    }
    return render(request, 'inv/index.html', context)

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'inv/add_new.html', {'form' : form})


def add_(request):
    return add_item(request, SuccessFactorForm)

def add_successFactor(request):
    return add_item(request, SuccessFactorForm)

def add_performanceIndicator(request):
    return add_item(request, PerformanceIndicatorForm)

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'inv/edit_item.html', {'form': form})



def edit_successFactor(request, pk):
    return edit_item(request, pk, SuccessFactor, SuccessFactorForm)


def edit_performanceIndicator(request, pk):
    return edit_item(request, pk, PerformanceIndicator, PerformanceIndicatorForm)




