from django.shortcuts import render
from .models import Herb

# Two example views. Change or delete as necessary.
def home(request):

    context = {'example_context_variable': 'Change me.' }

    return render(request, 'pages/home.html', context)



def about(request):
    context = {}

    return render(request, 'pages/about.html', context)




def quiz(request):

    herbs = [
        {
            'common_name': 'Skullcap',
            'botanical_name': 'scutteleia',
            'image': '',
            'question': 'Hey whats up?',
            'info': 'hey heres info',
        },
        {
            'common_name': 'Passionflower',
            'botanical_name': 'scutteleia',
            'image': '',
            'question': 'Hey whats up?',
            'info': 'hey heres info',
        },
        {
            'common_name': 'Oat Tops',
            'botanical_name': 'scutteleia',
            'image': '',
            'question': 'Hey whats up?',
            'info': 'hey heres info',
        },
  
    ]

    herbs = Herb.objects.all()

    if request.method == 'POST':
        print(request.POST)

    context = {
        'herbs': herbs,
    }

    if request.method == 'POST':
        true_answers = []
        for key, value in request.POST.items():
            print('key', key)
            print('value', value)
            if value == 'true':       #true?
                true_answers.append(key)
                print(true_answers)

                context = {
                    'herbs': herbs,
                }
        return render(request, 'pages/results.html', context)

    return render(request, 'pages/quiz.html', context)



    

def results(request):
    
    if request.method == 'POST':
        true_answers = []
        for key, value in request.POST.items():
            print('key', key)
            print('value', value)
            if value == 'true':       #true?
                true_answers.append(key)
                print(true_answers)

                context = {
                
                }
        return render(request, 'pages/results.html', context)
















