"""group_project_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


'''
CRYPTOCODERS
this helps with knowing what page to call.
this is the top level path for each app in the system.
when adding a new app, make sure to add top level here and tie it to the apps url file
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Atm/', include('Atm.urls')),
    path('Atm/transfer', include('Atm.urls'))
]
