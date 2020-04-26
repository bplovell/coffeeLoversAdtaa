# Coffee Lovers ADTAA app
Code Credits:
  Corey Schafer's tutorial: https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p
  "invitations" app created by, bee-keeper: https://github.com/bee-keeper/django-invitations

### installation with heroku
Add environment variables to enable email:
  go to Settings -> Config Vars
  select Reveal Config Vars and input your apps email address and email app password

Deploy code to dyno
Open bash console and run the following:
  python manage.py makemigrations users
  python manage.py makemigrations Adtaa
  python manage.py migrate
  python manage.py createsuperuser

### django
ctrl-alt-i  
//will correct indentation.  you may want to try  
//it with multiple lines selected  

python3 manage.py startapp my_app  
//will create directory my_app with all the things  

copy and past json  
code -> reformat code  
//will make JSON pretty

python manage.py makemigrations appname     
//will create a file in my_app/migrations directory  

python manage.py migrate  
//will run migration  

pip freeze  
//will display list of packages  


### Notes
- in html it is acceptable to use 2 or 4 spaces for indentation just be consistent  
- some other helpful stuff here that I forgot about

### Git
git add -u  
//stages modifications and deletions, without new files  

git add .  
//stages new files and modifications, without deletions  

git add -A  
stages all changes (equivalent to both of the above one-liners)  

git reset -- filename  
//will unstage file filename  

git rm filename  
//will remove file, assuming already removed locally  
