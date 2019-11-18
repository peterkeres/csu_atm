'''
CRYPTOCODERS

this file will call the correct html pages depeing on what url the user tries to hit

the functions here are being called from the 'urls.py' files of this 'Atm' app

if any data needs to be sent to the html file, it can be handled here
'''



from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse




#Views are created
from Atm.models import Transaction


'''
CRYPTOCODERS

calls the 'home' html page.
'''
def home(request):
    '''
    return HttpResponse("Hello, world. You're at the home page for the Atm app!")
    '''
    number = 10
    context = {'amount' : number}
    template = loader.get_template('Atm/home.html')
    return HttpResponse(template.render(context, request))

def transfer(request):
    transfer = amount 
    context = {'Transfer' : transfer_amount}
    template = loader.get_template('Atm/transfer.html')
    return HttpResponse(template.render(context, request))

def user_balance(request):
    your_balance = balance
    #template = loader.get_template('Atm/balance.html')
    return render(request, 'Atm/balance.html', {"Balance" : Balance} )
