

from django.contrib import admin

from .models import Account_Extension
from .models import Atm_Card
from .models import Atm_Machine
from .models import Atm_Machine_Refill


admin.site.register(Account_Extension)
admin.site.register(Atm_Card)
admin.site.register(Atm_Machine)
admin.site.register(Atm_Machine_Refill)
