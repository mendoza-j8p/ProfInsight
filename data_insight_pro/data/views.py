import csv
from django.shortcuts import render
from .models import Professor
from .forms import UploadFileForm

def handle_uploaded_file(f):
    reader = csv.DictReader(f.read().decode('utf-8').splitlines())
    for row in reader:
        Professor.objects.create(
            date_joined=row['Fecha de ingreso en la universidad'],
            name=row['Nombre'],
            subject=row['Asignatura que imparte'],
            years_of_experience=int(row['Años de Experiencia propia']),
            publications=int(row['Publicaciones']),
            extra_courses=int(row['Cursos extra impartidos']),
            current_salary=float(row['Sueldo actual'])
        )

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
