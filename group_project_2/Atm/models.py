'''
CRYPTOCODERS

this file creats all the tables that are used by the atm app for the databases

each class is the table, with fields being set within the class
Test er fuckererrrr
follow the 'class digram pdf' to see a modle view of the tables
'''


from django.db import models


'''
CRYPTOCODERS

this is the account table
holds:
    pk is the account number
    name of person on account
    phone number on the Account
    currnet balance of the account
'''
class Account_Extension(models.Model):
    name = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length = 15)
    balance = models.DecimalField(max_digits=19, decimal_places = 2)

    '''
    CRYPTOCODERS

    this is us overriding the to-string method.
    how each record wil be displayed.
    '''
    def __str__(self):
        return str(self.id) + " : " + self.name
