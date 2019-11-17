

from django.contrib import admin

from .models import Account_Extension
from .models import Atm_Card
from .models import Atm_Machine


admin.site.register(Account_Extension)
admin.site.register(Atm_Card)
admin.site.register(Atm_Machine)
