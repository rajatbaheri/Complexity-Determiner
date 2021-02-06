# Complexity-Determiner for python programs

The repository consists of django web application for the project Complexity-Determiner.

-> To run this application

-> Have python 3.5+ and Django 3.1+ installed

-> Open Terminal and run following commands:

   -> git clone https://github.com/rajat-chn/Complexity-Determiner
   
   -> python3 manage.py runserver
   
   -> Must have a 64 bit machine otherwie some function might not work
   
<img src=https://github.com/rajat-chn/Complexity-Determiner/blob/homepage/compx/static/images/input1.png>
<img src=https://github.com/rajat-chn/Complexity-Determiner/blob/homepage/compx/static/images/input2.png>
<img src=https://github.com/rajat-chn/Complexity-Determiner/blob/homepage/compx/static/images/out.png>


### HEROKU FILES ###
As we have deployed our project on heroku we have two additional file in our project

      1. Procfile :- tell heroku how to activate server
                                 
                                 web: gunicorn compDet.wsgi
                                 
      2. Requirement.txt :- tell heroku server about the additional files required to run our project
      
      
                                 asgiref==3.3.1
                                 Django==3.1.5
                                 gunicorn==20.0.4
                                 pytz==2020.5
                                 sqlparse==0.4.1

