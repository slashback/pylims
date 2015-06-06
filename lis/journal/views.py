from django.shortcuts import render
from journal.models import Patient, Application, Specimen
from dictionary.models import Division


def patients_journal(request):
    patients = Patient.objects.all()
    divisions = Division.objects.all()
    return render(request, 'journal/patients_journal.html',
                  {'patients': patients,
                   'divisions': divisions}
                  )


def registration_journal(request):
    applications = Application.objects.all()
    divisions = Division.objects.all()
    return render(request, 'journal/registration_journal.html',
                  {'applications': applications,
                   'divisions': divisions}
                  )


def work_journal(request, division_id):
    specimens = Specimen.objects.filter(division=division_id)
    print(Specimen.objects.filter(id=1).count())
    divisions = Division.objects.all()
    return render(request, 'journal/work_journal.html',
                  {'specimens': specimens,
                   'divisions': divisions}
                  )


def home(request):
    return render(request, 'journal/base.html', {})
