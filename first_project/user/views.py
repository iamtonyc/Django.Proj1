from django.shortcuts import render
from django.http import HttpResponse
from user.models import  User

# Create your views here.
def index(request):
    user_lists=User.objects.order_by('first_name')
    user_dict ={'user_records':user_lists}

    return render(request, 'user/index.html', context=user_dict)
