from django.shortcuts import redirect, render
from .forms import CrearTareaForm, BuscarForm
from .models import Tarea
# Create your views here.

def inicio(request):
    return render(request, 'layout/base.html')

def tarea_crear(request):
    if request.method =='GET':
        return render(request, 'tareas/tarea_crear.html',{
            'form': CrearTareaForm
        })
    else:
        tarea = CrearTareaForm(request.POST)
        tarea.save()
        return redirect('index')
        
def tareas_index(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/tarea_index.html',{
        'tareas': tareas
    })
    
def tarea_actualizar(request,tarea_id):
    if request.method == 'GET':
        tarea = Tarea.objects.get(pk = tarea_id)
        form = CrearTareaForm(instance = tarea)
        return render(request, 'tareas/tarea_actualizar.html',{
            'tarea': tarea, 'form': form
        })
    else:
        tarea = Tarea.objects.get(pk = tarea_id)
        form = CrearTareaForm(request.POST, instance = tarea)
        form.save()
        return redirect('tareas_index')
    
def tarea_eliminar(request,tarea_id):
    if request.method == 'POST':
        tarea = Tarea.objects.get(pk = tarea_id)
        tarea.delete()
        return redirect('tareas_index')
    else:
        return redirect('tareas_index')
    
    
def buscar_tareas(request):
    form = BuscarForm()
    resultados = None
    
    if 'query' in request.GET:
        form = BuscarForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = Tarea.objects.filter(nombre__icontains=query)
    
    return render(request, 'tareas/buscar_tareas.html', {'form': form, 'resultados': resultados})