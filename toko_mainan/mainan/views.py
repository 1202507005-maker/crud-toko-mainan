# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mainan
from .forms import MainanForm

def mainan_list(request):
    data = Mainan.objects.all()
    return render(request, 'mainan/list.html', {'data': data})

def mainan_create(request):
    if request.method == 'POST':
        form = MainanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainan_list')
    else:
        form = MainanForm()
    return render(request, 'mainan/form.html', {'form': form})

def mainan_update(request, id):
    mainan = get_object_or_404(Mainan, id=id)
    if request.method == 'POST':
        form = MainanForm(request.POST, instance=mainan)
        if form.is_valid():
            form.save()
            return redirect('mainan_list')
    else:
        form = MainanForm(instance=mainan)
    return render(request, 'mainan/form.html', {'form': form})

def mainan_delete(request, id):
    mainan = get_object_or_404(Mainan, id=id)
    mainan.delete()
    return redirect('mainan_list')
