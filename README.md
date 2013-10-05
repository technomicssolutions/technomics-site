techmnomics-site
================

##Technomics-site
Technomics Software Solutions

### Brief
Python - Django site (Version 1.5)

#### How to

#### Virtual Env

Its highly recommended to work under virtual environment. 
* `pip install virtualenv`
* `pip install virtualenvwrapper`
* `export WORKON_HOME=~/Envs`
* `mkdir -p $WORKON_HOME`
* `source /usr/local/bin/virtualenvwrapper.sh`
* `mkvirtualenv technomics --distribute`
* `workon technomics`

### Setup
* Clone the url from git using the command `git clone https://github.com/technomicssolutions/technomics-site.git`
* Pull the code from git using the command `git pull origin technomics-site`
* To install the requirements `pip install -r requirements.txt`

#### Database
##### PostgresSQL
* Install `postgresql`, `pgadmin` and other dev dependencies 
 
##### Local Settings
* locate file `local_settings.py` and edit the database properties. If there exists no DB or user, follow the steps below

* Create a new user, which should match to the user given in the `local_settings.py`
* Create a new database named **technomics**, make the above user the owner. Add the new database name , user and the password to the database setup. 


#### Sync DB
* Once above setup is done, run at the `technomics` workspace root, `python manage.py syncdb`
* Create a superuser while running the above command, set the password. Please remember these informations.
* Then run `python manage.py migrate`. This command will run all migrations
* Run `python manage.py runserver ` and goto `http://127.0.0.1:8000/admin` in the browser. Login to the admin using the username and password created in the above step.
* After login the window shows the list of models.

#### Models
### Slideshow

* Click on the `Slideshow` and click on `Add Slideshow` button. Upload images for the left arrow , right arrow , active and inactive bullets.
* Click on add slides upload images (minimum of 3) for the slideshow in the home page. Add slogan for each slide in the manner `<p id="first" >where technology</p><p id="second" > meets economy</p>`, click `Save` button.

### Home Page
* Click on `Home Page` --> `Add Home Page`, upload an image for logo and add the customercare no, click `Save` button.

### Feature
* Click on `Feature` --> `Add Feature`, add a heading and its description and click `Save` button.

### About Us
* Click on `About Us` --> `Add About Us`, add a heading and its description and click `Save` button.

### News & Events
* Click on `News & Events` --> `Add News & Events`, add an event, its description and the date, click `Save` button.

### Testimonials
* Click on `Testimonials` --> `Add Testimonials`, add a heading, its description, upload an image and click `Save` button. 

### Services
* Click on `Services` --> `Add Services` . Upload the banner image for the services page. Add a heading and content to be displayed in the services page, click `Save` button.

### Services Sections
* Click on `Services Sections` --> `Add Services Sections`. Add two objects.
* Upload an image, add a heading and content, click `Save` button.

* After creating the above objects, goto `http://127.0.0.1:8000` in the browser, you can see the home page there.





