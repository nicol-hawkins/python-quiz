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
        list_of_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        relevant_herbs = Herb.objects.filter(id__in=list_of_ids)
        for key, value in request.POST.items():
            
            # print('key', key)
            # print('value', value)
            # print('name', name)
            if value == 'true':       #true?
                # DO SPLIT HERE......
                relevant_herbs = 'answer_1'
                answer, herb_id = relevant_herbs.split('_')
                print(relevant_herbs.split('_'))
                
                
                # true_answers.append(herb_id)
                # herb_id = true_answers
                # print(true_answers)
                # print(herb_id)

                context = {
                    'herbs': herbs,
                }
        return render(request, 'pages/results.html', context)

    return render(request, 'pages/quiz.html', context)



    

def results(request):

    
    if request.method == 'POST':
        true_answers = []
        list_of_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        relevant_herbs = Herb.objects.filter(id__in=list_of_ids)
        print(relevant_herbs)
        for key, value in request.POST.items():
            print('key', key)
            print('value', value)
            if value == 'true':  
                # DO SPLIT HERE....
                answer_string = 'answer_{{ herb.id }}'
                answer, herb_id = answer_string.split('_')
                print(herb_id)
                true_answers.append(herb_id)
                print(true_answers)

        herbs = Herb.objects.all()
        context = {
            'herbs': herbs,
        }
        return render(request, 'pages/results.html', context)
















