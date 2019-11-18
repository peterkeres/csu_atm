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


    def __str__(self):
        return "Account number is : " + str(self.id) + " | Owner is : " + self.name


'''
CRYPTOCODERS

this table holds infor on each atm card in the system
holds:
    pk is the card number
    account number is the id of the account
    pin the pin used for the card
    name is the name that is on the card
    date issued is the data the card was created
    date expire is the date the card will exipre
    address is the address that is tied to the card
    two factor status is if the card is set up for two factor
    card status is if the card is active or not
'''
class Atm_Card(models.Model):
    #atm_account_number = self.id | is defualt build into the modles
    account_number = models.ForeignKey('Account_Extension', on_delete = models.PROTECT)
    pin = models.CharField(max_length = 4)
    name = models.CharField(max_length = 200)
    date_issued = models.DateField(null = True) #auto_now_add = True)
    data_expire = models.DateField(null = True)
    address = models.CharField(max_length = 200, default = "NA")

    twof_status_choices = [ ("Active","Active") , ("Inactive","Inactive") ]
    two_factor_status = models.CharField(max_length = 10, default = "Inactive", choices = twof_status_choices)

    Card_status_choices = [ ("Active","Active") , ("Inactive","Inactive") ]
    card_status = models.CharField(max_length = 10, default = "Inactive", choices = Card_status_choices)


    def __str__(self):
        return "Atm card number is : " + str(self.id)



'''
CRYPTOCODERS

this table holds information about the ATM machine
holds:
    current balance is the balance that is on the machine
    location is where the macine is located
    min balance is how much must be in the machine at all times
    status is if the machine is working or not
    last refill is when the machine was last refilled
    next next_maintenance_date is when the next time maintenance should be done on the machine
'''
class Atm_Machine(models.Model):
    #Atm_Machine_id = self.id | is defualt build into the Models
    current_balance = models.DecimalField(max_digits=19, decimal_places = 2, default = 0.00)
    location = models.CharField(max_length = 200, default = "NA")
    minimum_balance = models.DecimalField(max_digits = 19, decimal_places = 2, default = 1000.00)

    status_choices = [ ("Active","Active") , ("Inactive","Inactive") ]
    status = models.CharField(max_length = 10, default = "Active", choices = status_choices)

    last_refill_date = models.DateField(null = True)
    next_maintenance_date = models.DateField(null = True)


    def __str__(self):
        return "Atm id is: " + str(self.id) + " / location : " + str(self.location) + " / status : " + str(self.status)


'''
CRYPTOCODERS

this holds info on the refill event of the atm
holds:
    atm id is the id of the atm that is being refilled
    amount is the amount that was placed inot the atm
    amt branch is the what bank branch this atm belongs too
    refill date is the date that the refilled event happened
'''
class Atm_Machine_Refill(models.Model):
    #Atm_machine_refill_ id = self.id | is defualt build into the Models
    atm_id = models.ForeignKey('Atm_Machine', on_delete = models.PROTECT)
    amount = models.DecimalField(max_digits=19, decimal_places = 2)
    atm_branch =  models.CharField(max_length = 200, default = "NA")
    refill_date = models.DateField(null = True) #, auto_now_add = True)
    #TODO: get value of blanace from the atm that is in another table
    #previous_balance =

    def __self__(self):
        return "Refill id is: " + str(self.id) + " / date: " + str(self.refill_date)



'''
CRYPTOCODERS

holds any transactions that happen
holds:
    card id is the id of the card that is used in the transaction
    time is the time the transaction happened
    atm id is the id of the atm that is being used
    status is if the transaction is completed or not
    responce_code is the code for this transactionq
    transaction type holds what transaction this was 
'''
class Transaction(models.Model):
    #transaction id = self.id | is default buid into the modles
    card_id = models.ForeignKey('Atm_Card', on_delete = models.PROTECT)
    time = models.DateTimeField(null = True)
    atm_id = models.ForeignKey('Atm_Machine', on_delete = models.PROTECT)

    status_choices = [ ("Complete","Complete") , ("Incomplete","Incomplete") ]
    status = models.CharField(max_length = 10, default = "Incomplete", choices = status_choices)

    responce_code = models.CharField(max_length = 4)

    # add typs of transactions here
    transaction_choices = [ ("NA","NA") , ("Phone Change","Phone Change") , ("Pin Change","Pin Change") , ("Cash Withdrawal", "Cash Withdrawal") , ("Cash Trasnsfer","Cash Trasnsfer") , ("Balance Enquiry","Balance Enquiry")]
    transaction_type = models.CharField(max_length = 15, default = "NA", choices = transaction_choices)

    def __self__(self):
        return "Transaction id is: " + str(self.id) + " | date: " + str(self.date) + " | time: " + str(self.time)
