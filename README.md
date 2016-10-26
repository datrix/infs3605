# infs3605

We have currently uploaded the repository onto Github. However, since we had difficulties with publishing the site, we decided it would be easier for you to run the system on a cloud IDE instead of installing python and 3rd party installs onto your PC.
The following steps will help you view the system and also the code:

Login to codeanywhere (codeanywhere.com) with:
Username: *************************
Password: ********

Right click the richardbottom container directory and open up SSH Terminal
Type in the following commands:
    
    cd django/bin && source activate
    cd
    cd workspace/coordsys
    python manage.py runserver 0.0.0.0:8000
    
Then click this link to view:
http://preview.vwwitq6of512a9k9kfesyzke1kz0vn2998dbfqr14w265hfr.box.codeanywhere.com:8000/calendar
