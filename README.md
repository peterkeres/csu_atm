# csu_atm
This is the ATM project for software eng

## **following notes will be for the devs**


### Running the code
In order to do this, you have to run the code from the command line. This will make a server that you can access. The server is only accessible on your ‘local host’, meaning you can't access it over the network. From the command line, go to the directory that has the top level ‘manage.py’ file. From here, run **"python3 manage.py runserver"**. Open a web browser and go to http://127.0.0.1:8000/Atm. This will take you to the homepage of the Atm app. If you want to go to the admin page ( to mess with the database directly) go to http://127.0.0.1:8000/admin


### Admin login
- Username is: admin
- Password is: 12345


### Key files to interact with

##### 98% of the code we will now interact with will be under the ‘Atm/’ sub directory.


- Models.py file:
  - This file pretty much makes all the tables and columns that the Atm app needs to run.

- Admin.py file:
  - Sets what tables are able to be viewed when access the admin portal.

- Urls.py file:
  - This ties what path name is entered in the web browser and calls a method in the view.py file.

- Views.py file:
  - This file will call whatever html in the ‘templates/atm/(any.html)’ is needed for this page and gather whatever data is needed for that html file.

- templates/atm/ any file:
  - Any html file that you need for the Atm app. Aka the layout of each webpage and is going to be called from the views.py file which is then called by the urls.py file.


### Navigating the code base
Any comments we have left, shall be left with the header of ‘CRYPTOCODERS’
This is so we can find comments the team left, in a slew of comments left by the Django framework. Just do a search for this header to look for code we have written.
