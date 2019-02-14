from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    webpage_lists=AccessRecord.objects.order_by('date')
    date_dict ={'access_records':webpage_lists}

    return render(request, 'first_app/index.html', context=date_dict)
