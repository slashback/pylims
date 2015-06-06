from django.shortcuts import render
from journal.models import Patient, Application, Specimen, MeasurementResult
from dictionary.models import Division, Measurement
from journal.forms import UserlistForm


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
    divisions = Division.objects.all()
    return render(request, 'journal/work_journal.html',
                  {'specimens': specimens,
                   'divisions': divisions}
                  )


def specimen_info(request, specimen_id):
    specimen = Specimen.objects.get(id=specimen_id)
    patient = specimen.application.patient
    results = MeasurementResult.objects.filter(specimen=specimen_id)
    return render(request, 'journal/specimen.html',
                  {'results': results,
                   'patient': patient,
                   'specimen': specimen}
                  )


def create_application(request):
    tests = Measurement.objects.all()
    #groupusers = User.objects.filter(groups__name=custgroup.name)

    userlistform = UserlistForm()

    userlistform.fields['users'].choices = [(x.id, x) for x in tests]
    return render(request, 'journal/registration_form.html', {"userlistform":userlistform})


def home(request):
    return render(request, 'journal/base.html', {})
