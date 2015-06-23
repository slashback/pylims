from django.shortcuts import render, redirect
from django.http import HttpResponse
from journal.models import Patient, Application, Specimen, MeasurementResult
from dictionary.models import Division, Measurement, Biomaterial
from journal.forms import RegistrationForm, MeasurementResultForm
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


def specimen_info(request, specimen_id):
    specimen = Specimen.objects.get(id=specimen_id)
    patient = specimen.application.patient
    results = MeasurementResult.objects.filter(specimen=specimen_id)
    mform = MeasurementResultForm()
    return render(request, 'journal/specimen.html',
                  {'results': results,
                   'patient': patient,
                   'specimen': specimen,
                   'mform': mform}
                  )


def application_form(request):
    tests = Measurement.objects.all()
    test_list = RegistrationForm()

    test_list.fields['tests'].choices = [(x.id, x) for x in tests]
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
    internal_nr = '2345+'
    #номер заявки состоит из двух частей - даты и порядкового номера
    current_date = date.today()
    current_date.strftime('%d%m%Y')

    application = Application.objects.create(internal_nr=internal_nr,
                                             state='0',
                                             patient=patient
                                             )
    specimen = Specimen.objects.create(internal_nr=internal_nr,
                                       application=application,
                                       state=1,
                                       division=div,
                                       biomaterial=bm
                                       )
    for test_id in tests:
        print(test_id)
        measurement = Measurement.objects.get(id=test_id)
        MeasurementResult.objects.create(specimen=specimen,
                                         measurement=measurement,
                                         state=1
                                         )
    return redirect('/')


def specimen_save(request):
    data = request.POST
    print(data)
    for test_id in data:
        if test_id != 'csrfmiddlewaretoken':
            result = MeasurementResult.objects.get(id=test_id)
            specimen = result.specimen
            value = data.get(test_id, '')
            result.value = value
            if value:
                result.state = 3
            else:
                result.state = 1
            #result.save()
    return(redirect('/specimen/%d/' % (specimen.id,)))


def home(request):
    return render(request, 'journal/base.html', {})
