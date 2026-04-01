from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import AccessRecord

# Create your views here.
# def index(request):
#     #return HttpResponse("Hello World!")
#     my_dict = {'welcome_msg': "Welcome to Small Blog",
#                'course_name': "Lexicon Python + AI Training",
#                'students_today': 31,
#                'name': "My name is Manasi"}
#     return render(request,'index.html',context = my_dict)

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')

    context = {
        'access_records': webpages_list
    }

    return render(request, 'index.html', context = webpages_list)



