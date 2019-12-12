from django.shortcuts import render
import requests
from .models import Herb


def index(request):
    response= requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=37.804363,-122.271111&radius=1500&type=chinesemedicine&keyword=herbshop&key=AIzaSyDOWpD8jNHxjkOrNlI7Coka1wW5NU8-tJU')
    print(response.status_code)
    # print(response.json())

    # if request.method == 'POST':
    #    pass
    # print(request.POST)
    #     form = CityForm(request.POST)       #for adding into the form
    #     form.save()





     
# Two example views. Change or delete as necessary.
def home(request):

    context = {'example_context_variable': 'Change me.' }

    return render(request, 'pages/home.html', context)



def about(request):
    context = {}

    return render(request, 'pages/locate.html', context)




def quiz(request):     

    herbs = Herb.objects.all()

    if request.method == 'POST':
        print(request.POST)

    context = {
        'herbs': herbs,
    }

    if request.method == 'POST':
        true_answers = []
        
        for name, value in request.POST.items():
            print('name: ', name)
            print('value: ', value)
            if value == 'true':  
                # DO SPLIT HERE....
                relevant_herbs = name
                answer, herb_id = relevant_herbs.split('_')
                print('herb_id: ',herb_id)

                true_answers.append(herb_id)
                
                    
        print('true_answers', true_answers)
        relevant_herbs = Herb.objects.filter(id__in=true_answers)
        context = {
            'herbs': herbs,
            'relevant_herbs': relevant_herbs,
        }
        return render(request, 'pages/results.html', context)

    return render(request, 'pages/quiz.html', context)
