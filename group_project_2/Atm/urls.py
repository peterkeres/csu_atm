'''
CRYPTOCODERS

this will call methods based on what url path is picked by the browser
thoes methods called will display the correct html pages

calls methods in the 'view.py' file
'''



from django.urls import path

from . import views

# CRYPTOCODERS name of the app, used for shortcuts in making links in html code
app_name = 'ATM'

'''
CRYPTOCODERS

this array will tie what url is enternd in the browser to what method to call
to disply the hmtl file for that page.
for each new page, you have to add the path here
'''
urlpatterns = [
    path('', views.home, name='home'),
]
