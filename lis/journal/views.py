from django.shortcuts import render
from journal.models import Patient


def patients_journal(request):
    patients = Patient.objects.all()
    return render(request, 'journal/patients_journal.html', {'patients': patients})