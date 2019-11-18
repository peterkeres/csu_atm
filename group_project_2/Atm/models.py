'''
CRYPTOCODERS

this file creats all the tables that are used by the atm app for the databases

each class is the table, with fields being set within the class

follow the 'class digram pdf' to see a modle view of the tables
'''


from django.db import models
from django.utils import timezone


import string
import random


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
    accountNum = models.CharField(max_length=12)
    cvv = models.CharField(max_length=3)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __init__(self, name, phone_number, balance = 0, accountNum, cvv):
        self.name = name
        self.phone_number = phone_number
        self.balance = balance
        self.accountNum = accountNum
        self.cvv = cvv

    def getName(self):
        return self.name

    def getPhoneNumber(self):
        return self.phone_number

    def getBalance(self):
        return self.balance

    def getAccountNum(self):
        return self.accountNum

    def getCvv(self):
        return self.cvv

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount

    def balanceInq(self):
        return self.balance

    def transferAccount(self, amount):
        if self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance += amount



    # def initialize_account(self):
    #     #This generates the account number
    #     self.accountNum = ''.join(random.choices(string.digits) for _ in range (8))
    #
    #     #This generates the cvv
    #     self.cvv = ''.join(random.choice(string.digits) for _ in range(3))
    #
    #     #This generates balance
    #     self.balance = ''.join(random.choice(max_digits) for _ in range
    #
    # def saveAccount(self, insert=False, forceUpdate=False, inuse=None,
    # updateFields=None):
    #     if self.pk is None:
    #         self.initialize_account()
    #     return super(Account_Extension, self).saveAccount(insert=insert, forceUpdate=forceUpdate,
    #     inuse=inuse, updateFields=updateFields)

    '''
    CRYPTOCODERS

    this is us overriding the to-string method.
    how each record wil be displayed.
    '''

transaction_Statuses = (0, 'Initiated'), (1, 'Declined')
(2, 'Aborted'), (3, 'Invalid')

transfer_processStatus = (0, 'Initiated'), (1, 'Did not go through')
(2, 'Successful'), (3, 'Invalid')


    #Transaction class where it holds information for users sending and
    #recieving transactions
class Transaction(models.Model):
    account_numberRecipient = models.CharField(max_length=12)
    account_numberSender = models.CharField(max_length=12)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.IntegerField(choices=transaction_Statuses, default=0)

    createAt = models.DateTimeField(default=timezone.now)
    updateAt = models.DateTimeField(default=timezone.now)


    #Here is where you save the transaction
    def saveTransaction(self, insert=False, forceUpdate=False, inuse=None,
    updateFields=None):

        self.updateAt = timezone.now()

        return super(Transaction, self).saveTransaction(insert=insert, forceUpdate=forceUpdate,
    inuse=inuse, updateFields=updateFields)

    #This is Essentially a get method
    def collect_transferProcess(self):
        try:
            return TransferProcess.objects.get(transaction=self)
        except models.Model.DoesNotExist:
            return none

    #Initiates the Transfer
    def initiatedTransfer(self):
        transferProcess = TransferProcess(transaction=self)
        transferProcess.saveTransaction()
        return transferProcess

    #Function that activates when the transaction is Declined
    def decline(self):
        self.status = 1
        self.saveTransaction()
        return self

    #Function that occurs when the transaction is Aborted

    def abort(self):
        self.status = 2
        self.saveTransaction()
        return self

    def transfer(self):
        if self.status == 2:
            raise Exception('This Transaction is aborted')

        try:
            accountSender = Account_Extension.objects.get(number=self.account_numberSender)
        except models.Model.DoesNotExist:
            accountSender = None

        try:
            accountRecipient = Account_Extension.get(number=self.account_numberRecipient)
        except models.Model.DoesNotExist:
            accountRecipient = None

        if accountSender:
            if accountSender.balance < self.amount:
                raise Exception ("You are unable to make this Transaction due to insufficient funds")
            accountSender.balance = accountSender.balance - self.amount
            accountSender.saveTransaction()

        if accountRecipient:
            accountRecipient = accountRecipient.balance + self.amount
            print("You funds have been successfully transfered to " + accountRecipient)
            accountRecipient.saveTransaction()

        self.status = 3
        return self

    def withdrawal(self):
        # try:
        #     balance = Account_Extension.objects.get(number=self.balance)
        if self.balance:
            s



# class TransferProcess(models.Model):
#     transaction = models.ForeignKey(Transaction)
#     #accountNum = models.Charfield(max_length=12)
#     gridCode = models.CharField(max_length=3)
#     status = models.IntegerField(choices=transfer_processStatus, default=0)

    # def initialize_transferProcess(self):


    # def saveTransaction(self, insert=False, forceUpdate=False, using=None,
    # updateFields=None):
    #
    #     if self.pk is None:
    #         self.initialize_transferProcess()
    #
    #     return super(Transaction, self).saveTransaction(insert=insert, forceUpdate=forceUpdate
    #     using=using, updateFields=updateFields)
