
import datetime
from django.contrib import admin

from .models import Account_Extension, Add_New_ATM_Card, View_ATM_Status, ATM

admin.site.site_header = "ATM Administration"
admin.site.site_title = "ATM Admin Portal"
admin.site.index_title = "Welcome to the ATM Admin Portal"
admin.site.register(Account_Extension)
admin.site.register(Add_New_ATM_Card)
admin.site.register(View_ATM_Status)
admin.site.register(ATM)
