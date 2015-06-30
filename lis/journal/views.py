from django.shortcuts import render, redirect
from journal.models import Patient, Application, Specimen, MeasurementResult
from dictionary.models import Division, Measurement, Biomaterial
from journal.forms import RegistrationForm, ResultFormSet
from datetime import date


def patients_journal(request):
    patients = Patient.objects.all()
    return render(request, 'journal/patients_journal.html',
                  {'patients': patients}
                  )


def registration_journal(request):
    applications = Application.objects.all()
    return render(request, 'journal/registration_journal.html',
                  {'applications': applications}
                  )


def work_journal(request, division_id):
    specimens = Specimen.objects.filter(division=division_id)
    return render(request, 'journal/work_journal.html',
                  {'specimens': specimens}
                  )


def application_form(request):
    tests = Measurement.objects.all()
    test_list = RegistrationForm()
    test_list.fields['first_name']
    test_list.fields['tests'].choices = [(x.id, x) for x in tests]
    biomaterials = Biomaterial.objects.all()
    test_list.fields['biomaterials'].choices = [(x.id, x) for x in biomaterials]
    return render(request,
                  'journal/registration_form.html',
                  {"test_list": test_list})


def create_application(request):
    last_name = request.POST.get('last_name', '')
    first_name = request.POST.get('first_name', '')
    middle_name = request.POST.get('middle_name', '')
    gender = request.POST.get('gender', '')
    birth_date = request.POST.get('birth_date', '')
    tests = request.POST.getlist('tests')
    bm = Biomaterial.objects.get(id=1)
    div = Division.objects.get(id=1)
    patient = Patient.objects.create(last_name=last_name,
                                     first_name=first_name,
                                     middle_name=middle_name,
                                     gender=gender,
                                     birth_date=birth_date
                                     )
#    номер заявки состоит из двух частей - даты и порядкового номера за день
    today = date.today()
    numpart = Application.objects.filter(registration_date=today).count()
    numpart += 1
    datepart = str(today.strftime('%d%m%y'))
    internal_nr = datepart + format(numpart, '04d')

    application = Application.objects.create(internal_nr=internal_nr,
                                             state='0',
                                             patient=patient,
                                             registration_date=today
                                             )
    specimen = Specimen.objects.create(internal_nr=internal_nr,
                                       application=application,
                                       state=1,
                                       division=div,
                                       biomaterial=bm
                                       )
    for test_id in tests:
        measurement = Measurement.objects.get(id=test_id)
        MeasurementResult.objects.create(specimen=specimen,
                                         measurement=measurement,
                                         state=1
                                         )
    return redirect('/')


def specimen_info(request, specimen_id):
    specimen = Specimen.objects.get(id=specimen_id)
    patient = specimen.application.patient
    results = MeasurementResult.objects.filter(specimen=specimen_id)
    result_form = ResultFormSet(queryset=results)
    return render(request, 'journal/specimen.html',
                  {'results': results,
                   'patient': patient,
                   'specimen': specimen,
                   'result_form': result_form}
                  )


def specimen_save(request, specimen_id):
    formset = ResultFormSet(request.POST)
    for form in formset.forms:
        form.save()
    return(redirect('/specimen/%s/' % (specimen_id,)))


def home(request):
    return render(request, 'journal/base.html', {})
