from django.shortcuts import render
import requests


def index(request):
    response= requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=37.804363,-122.271111&radius=1500&type=chinesemedicine&keyword=herbshop&key=AIzaSyDOWpD8jNHxjkOrNlI7Coka1wW5NU8-tJU')
    print(response.status_code)
    print(response.json())

    if request.method == 'POST':
       pass
    # print(request.POST)
    #     form = CityForm(request.POST)       #for adding into the form
    #     form.save()
     
# Two example views. Change or delete as necessary.
def home(request):

    context = {
        'example_context_variable': 'Change me.',
    }

    return render(request, 'pages/home.html', context)

def about(request):
    context = {}

    return render(request, 'pages/about.html', context)

def searchherbstore(request):
    context = {}

    return render(request, 'pages/searchherbstore.html', context)















# response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=37.804363,-122.271111&radius=1500&type=chinesemedicine&keyword=herbshop&key=AIzaSyDOWpD8jNHxjkOrNlI7Coka1wW5NU8-tJU')
# data = response.json()
# print(data)



