from django.shortcuts import render
from bincom.models import *
# Create your views here.


def home(request):
    pollingunit = PollingUnit.objects.raw(
        'select * from Ward where ward_id=ward_id')
    ward = Ward.objects.raw('select * from Lga where lga_id=lga_id')
    context = {'pollingunit': pollingunit, 'ward': ward}

    return render(request, 'index.html', context)


def result(request):
    announcedpuresult = AnnouncedPuResults.objects.all()
    announcedwardresult = AnnouncedWardResults.objects.all()
    announcedstateresult = AnnouncedStateResults.objects.all()
    announcedlgaresult = AnnouncedLgaResults.objects.all()

    context = {'announcedpuresult': announcedpuresult,
               'announcedwardresult': announcedwardresult,
               'announcedstateresult': announcedstateresult,
               'announcedlgaresult': announcedlgaresult}

    return render(request, 'result.html', context)
