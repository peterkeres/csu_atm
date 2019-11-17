'''
CRYPTOCODERS

this file creats all the tables that are used by the atm app for the databases

each class is the table, with fields being set within the class

follow the 'class digram pdf' to see a model view of the tables
'''

from datetime import datetime
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
    class Meta:
        verbose_name = "Account extension"
        verbose_name_plural = "Account extension"
    name = models.CharField(max_length = 200)
    number = models.CharField(max_length = 12, primary_key = True, default = '0')
    phone_number = models.CharField(max_length = 12)
    balance = models.DecimalField(max_digits=20, decimal_places = 2)

    '''
    CRYPTOCODERS

    this is us overriding the to-string method.
    how each record will be displayed.
    '''
    def __str__(self):
        return self.number + " : " + self.name


class ATM(models.Model):
    class Meta:
        verbose_name = "ATM"
        verbose_name_plural = "ATMs"
    address = models.CharField(max_length = 200)
    #balance = models.DecimalField(max_digits = 20, decimal_places = 2)

    def getAddress(self):
        return self.address

    #def getBalance(self):
        #return self.balance

    def __str__(self):
        return "ATM at " + self.getAddress()

class Add_New_ATM_Card(models.Model):
    class Meta:
        verbose_name = "New ATM card"
        verbose_name_plural = "New ATM card"
    card_number = models.CharField(max_length = 16, primary_key = True, default = '0')
    account_number = models.ForeignKey('Account_Extension', on_delete = models.PROTECT)
    pin = models.CharField(max_length = 4)
    account_name = models.CharField(max_length = 200)
    date_issued = models.DateField(null = True)
    expiry_date = models.DateField(null = True)
    address = models.CharField(max_length = 200, default = "")
    balance = models.CharField(max_length = 20, default = '0')
    phone_number = models.CharField(max_length = 10, default = "")
    
    CARD_STATUS_CHOICES = [("Active", "Active"), ("Inactive", "Inactive")]
    card_status = models.CharField(max_length = 10, default = "Inactive", choices = CARD_STATUS_CHOICES)
    def __str__(self):
	    return self.card_number + ": " + self.account_name


class View_ATM_Status(models.Model):
    class Meta:
        verbose_name = "View ATM Status"
        verbose_name_plural = "View ATM Status"
    #ATM_CHOICES = ATM.objects.values_list('address', 'address')
    ATM_STATUS_CHOICES = [("Active","Active"), ("Down","Down")]
    ATM_address = models.ForeignKey('ATM', on_delete = models.PROTECT, primary_key = True)
    #ATM_address = models.CharField(primary_key = True, max_length = 200, choices = ATM_CHOICES)
    ATM_status = models.CharField(max_length = 10, choices = ATM_STATUS_CHOICES, default = "Down")
    last_refill = models.DateTimeField(default = datetime.now)
    next_refill = models.DateField(default = datetime.now)
    balance = models.DecimalField( max_digits = 20, decimal_places = 2)
    
    def __str__(self):
        return str(self.ATM_address) + ". Status: " + self.ATM_status + ". Next refill: " + str(self.next_refill)
    

