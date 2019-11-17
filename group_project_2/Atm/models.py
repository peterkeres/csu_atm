'''
CRYPTOCODERS

this file creats all the tables that are used by the atm app for the databases

each class is the table, with fields being set within the class

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
    #account number = self.id | is defualt build into the modles
    name = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length = 15)
    balance = models.DecimalField(max_digits=19, decimal_places = 2)

    '''
    CRYPTOCODERS

    this is us overriding the to-string method.
    how each record wil be displayed.
    '''
    def __str__(self):
        return "Account number is : " + str(self.id) + " | Owner is : " + self.name


'''

'''
class Atm_Card(models.Model):
    #atm_account_number = self.id | is defualt build into the modles
    account_number = models.ForeignKey('Account_Extension', on_delete = models.PROTECT)
    pin = models.CharField(max_length = 4)
    name = models.CharField(max_length = 200)
    date_issued = models.DateField(null = True, auto_now_add = True)
    data_expire = models.DateField(null = True)
    address = models.CharField(max_length = 200, default = "NA")

    twof_status_choices = [ ("Active","Active") , ("Inactive","Inactive") ]
    two_factor_status = models.CharField(max_length = 10, default = "Inactive", choices = twof_status_choices)

    Card_status_choices = [ ("Active","Active") , ("Inactive","Inactive") ]
    card_status = models.CharField(max_length = 10, default = "Inactive", choices = Card_status_choices)


    def __str__(self):
        return "Atm card number is : " + str(self.id)
