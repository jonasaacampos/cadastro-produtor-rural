from django.shortcuts import render, get_object_or_404, redirect
from .models import ProdutorRural, PropriedadeRural
from .forms import ProdutorRuralForm, PropriedadeRuralForm

def produtor_list(request):
    produtores = ProdutorRural.objects.all()
    return render(request, 'produtores/produtor_list.html', {'produtores': produtores})

def produtor_create(request):
    if request.method == 'POST':
        form = ProdutorRuralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtor_list')
    else:
        form = ProdutorRuralForm()
    return render(request, 'produtores/produtor_form.html', {'form': form})

def produtor_update(request, pk):
    produtor = get_object_or_404(ProdutorRural, pk=pk)
    if request.method == 'POST':
        form = ProdutorRuralForm(request.POST, instance=produtor)
        if form.is_valid():
            form.save()
            return redirect('produtor_list')
    else:
        form = ProdutorRuralForm(instance=produtor)
    return render(request, 'produtores/produtor_form.html', {'form': form})

def produtor_delete(request, pk):
    produtor = get_object_or_404(ProdutorRural, pk=pk)
    if request.method == 'POST':
        produtor.delete()
        return redirect('produtor_list')
    return render(request, 'produtores/produtor_confirm_delete.html', {'produtor': produtor})