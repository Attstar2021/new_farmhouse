*Farmhouse is a place for every nature lover, busy worker and advanture hunter.* - [Dream Farmhouse Hotel](https://dream-farmhouse.herokuapp.com/)

---
**Table of Contents**
* [User Experience](#user-experience)
    * [Strategy Plane](#strategy-plane)
    * [Scope Plane](#scope-plane)
    * [Structure Plane](#structure-plane)
    * [Surface Plane](#surface-plane)
* [Agile Methodolody](#agile-methodology)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknoledgements](#acknowledgements)

---
## User Experience
User visit site to know more about farmhouse hotel, he can participate in community blog and like and comment on post uploaded by farmhouse team, he also can see and cancel his booking. Initially the site only offers view and cancelation appointment and also commenting and like. site owener can approve comments, update and create and even deleted posts

This webiste hold aninals images beautiful site and post which are it self descriptive.

### Scope Plane
### **Feature Planning**
the site was created on a dream and still in process. I am planing to add customer booking, updates and payment methods and also would like extand blog section where people and posts their experience and review and staring for services as well.

| # | Feature | Target User | Desirability | Importance | Viability  | Delivered |
| --- | --- | --- | --- | --- | --- | --- |
| User Accounts |  |  |  |  |  |  |
| 1 | User Role Permissions | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 2 | Account Registration | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| Navigation |  |  |  |  |  |  |
| 3 | Top Navigation to include:  signin  (register, signup) Booking List and Blog | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
|
| Booking lists |  |  |  |  |  |  |
| 4 |  Main page Categories | All Users <sup>1</sup> | 3 | 3 | 2 |  |
| 5 | NGO search | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 6 | Booking Cancelation  | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 7 | Booking list| All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| Blog |  |  |  |  |  |  |
| 8 | Commenting by same and other users | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| 9 | Liking each commenting and blog post | All Users <sup>1</sup> | 5 | 5 | 5 | ✅ |
| Wishlist |  |  |  |  |  |  |
| 10 | User booking and booking updates| Logged In Users | 4 | 4 | 5 | ❌ |
| 11 | Payment methods | All Users <sup>1</sup> | 4 | 4 |4  | ❌ |
| Digital Marketing |  |  |  |  |  |  |
| 12 | Social Media Presence | Visitors | 3 | 3 | 3 | ❌ |
| Email Marketing |  |  |  |  |  |  |
| 13 | Email Subscription, Powered by MailChimp | Registered Subscribers | 5 | 5 | 5 |❌  |
| Contact Us |  |  |  |  |  |  |
| 14 | Contact Form | All Users <sup>1</sup> | 3 | 3 | 3 | ❌ |


### Fonts and color

 font-family: sans-serif 

---
## Agile Methodology
### **GitHub Projects**

GitHub Projects was used to manage the development of the site. It helped to break down the larger issues into smaller issues 

* GitHub Projects - in progress
![GitHub Projects - progress](./documentation/support-ngos-github-projects-in-progress.png)
---
## User Stories
|USER STORY |	ISSUE ID |	As a/an |	I want to be able to...	| So that I can...|
| :-------: | :-------: | :-------:| :-----------------------: | :-------------: |
| 1         |    3      |  Site User    |  View home page      | Know more about website|
| 2         |    11     | Site User|  view Navbar      |  view content seamlessly |
| 3         |    6     | Donor  | View post |  |
Please see 
## Features

---
## Technologies Used
### **Languages Used**
* [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for the content and structure of the site.
* [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3) was used for the styling of the site.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for the interactivity of the site.
* [Python](https://www.python.org/) was used for the back end programming of the site.
## Frameworks Used
* [DJANGO - v3.2 ](https://docs.djangoproject.com/en/4.1/releases/3.2/) Django is a free and open-source, Python-based web  framework that follows the model–template–views architectural pattern.
* [Bootstrap4 - v4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) was used as the frontend framework.
## Databases Used
* [DB.SQLITE3](https://docs.djangoproject.com/en/4.1/ref/databases/#sqlite-notes) was the database used for the project (development).
* [ElephantSQL](https://www.elephantsql.com/) ElephantSQL's Postgres as a Service was used to host the the database for the project (production).
## **Libraries and Packages Used**
* [django-allauth](https://django-allauth.readthedocs.io/en/latest/) is an integrated set of Django applications dealing with account authentication, registration, management, and third-party (social) account authentication.
* [JQuery - v3.5.1](https://jquery.com/) is a fast, small, and feature-rich JavaScript library.
* [Font Awesome Kit](https://fontawesome.com/v5/docs/web/setup/use-kit) is used for its icon toolkit.
* [django-ckeditor v6.5.1](https://django-ckeditor.readthedocs.io/en/latest/) was used to provide a RichTextField p, RichTextUploadingField, CKEditorWidget and CKEditorUploadingWidget
* [django-js-asset v2.0.0](https://pypi.org/project/django-js-asset) This package provides a way of inserting script tags into Django templates that provide extra attributes such as `id` and `data-*` for CSP-compatible data injection.
* [django-summernote==0.8.20.0](https://pypi.org/project/django-summernote/) Summernote is a simple WYSIWYG editor. django-summernote allows you to embed Summernote into Django very handy. Support admin mixins and widgets.
* [django-crispy-forms, v1.14.0](https://pypi.org/project/django-crispy-forms/) was used to build programmatic reusable layouts out of form components.
* [gunicorn](https://gunicorn.org/) - a Python WSGI HTTP Server that allows us to run any Python application concurrently by running multiple processes within a single dyno
* [pillow](https://pypi.org/project/Pillow/) - a required Python imaging library used to enable handling of images.
* [psycopg2](https://pypi.org/project/psycopg2/) - a postgresql database adapter for python and used to connect with our postgres database
* [boto3==1.26.74](https://pypi.org/project/boto3/), [botocore==1.29.74] is an Amazon Web Services (AWS) software development kit (SDK) used to connect to the S3 bucket
* [pip](https://pip.pypa.io/en/stable/) is the package installer for Python, allowing us to install the packages we need for this site.
* [django storages](https://django-storages.readthedocs.io/en/latest/) - collection of custom storage backends for Django

## **Programmes and Applications Used**
* [Lucid Chart](https://www.lucidchart.com/pages/) was used to draw and build the Entity Relationship Diagram. It was also used to draw the User Flow Diagram.
* [favicon.io](https://favicon.io/) used to create the site's favicon
* [Git](https://git-scm.com/) used for version control and saving work in the repository, using the GitPod extension in Google Chrome to commit to GitHub.
* [GitHub](https://github.com/) is the project's git repository
* [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) used to track and integrate issues for Agile Development
* [Chrome DevTools](https://www.google.com/intl/en_uk/chrome/) - used for debugging, validation (Lighthouse) and taking fullscreen screenshots of the site
* [CloudConvert](https://cloudconvert.com/webp-converter) and [OnlineConvert](https://www.online-convert.com/) were used to convert the png images of ngo logos and other site images to next generation image format, webp.
* [Photoshop](https://www.adobe.com/uk/products/photoshop.html) used to resize the images used on the site

## **Cloud Application Platforms Used**
* [Heroku](https://devcenter.heroku.com/) was used for hosting and deployment of the live site. Throughout, we have ensured the version being deployed to Heroku matches the development version by checking features and screen layouts on both versions.

## **Cloud Storage Services Used**
* [AWS S3](https://aws.amazon.com/) was used to store the images and static files.

---

## Testing
### Manual Testing
1. The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
2. The website was viewed on a variety of devices such as Desktop, Laptop, Samsung9+, etc.
3. A large amount of testing was done to ensure that all component working properly.
4. Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Validator Testing

#### HTML Validation


#### CSS Validation
CSS Validation Service to validate CSS.

#### Javascript Validation

#### Python Validation


---
## Deployment

# **SupportNGOs Deployment &amp; Local Development**
**[Link to the Deployed Site](https://support-ngo.herokuapp.com/)**

---
## **Deployment Steps**

SupportNGO is deployed on Heroku and uses AWS3 for staticfiles cloud storage.

**1. Install the project requirements by creating a Pipfile** <br/>
In the terminal, enter the command ```pip3 freeze > requirements.txt ``` and a file with all the requirements will be created.

**2. Create an external database on ElephantSQL.com** <br/>
The sqlite3 database that came with Django and which we have been using is only available for use in development. We need to create a new database that is suitable for production.
* Go to [ElephantSQL.com](https://www.elephantsql.com/) and click *Get a managed database today* button.
* Select Tiny Turtle by pressing the *Try now for FREE* button
* Select *Log in with GitHub* and authorize ElephantSQL with your selected GitHub account
* In the create new team form:
    * Add a *team name* (your own name is fine)
    * Read and agree to the Terms of Service
    * Select *Yes* for GDPR
    * Provide your email address
    * Click *Create Team*
* Click *Create New Instance*

If you already have an account, after logging in to ElephantSQL:
* Set up your plan
    * Give your plan a **Name** (This is commonly the name of the project)
    * Select *Select Region*
    * Select a region and data center (Choose the one closest to you)
    * Click *Review*
    * Check that your details are correct and then click *Create New Instance*
    * Return to the dashboard and click on the *database instance name*
    * Copy the database url

**3. Set up Heroku**
* Go to [Heroku.com](https://www.heroku.com/) and log in
* Choose the New button and from the dropdown, select *Create new app*
* Add your preferred app name and select your location and click the create app button
* Add the **DATABASE_URL** Config Var by going to the settings tab
* Click *Reveal Config Vars*
* Add a Config Var **DATABASE_URL** and paste your ElephantSQL database URL in as the value

**4. Connect the external database to GitPod**
* In your **env.py** file add a new key, **DATABASE_URL** and give it the value of the copied database URL <br/>
```bash
os.environ.setdefault("DATABASE_URL", "the_copied_elephantsql_database_url_here")
```
* Install the **dj-database-url** package version 0.5.0 and **psycopg2** in the terminal with **pip3** to allow us to parse the URL we have copied above to a format that Django can work with: <br/>
```bash
pip3 install dj_database_url==0.5.0 psycopg2
```
* and remember to add both to your **requirements.txt** file with: <br/>
```bash
pip3 freeze --local > requirements.txt
```
* At the top of the **settings.py** file, import **dj_database_url** underneath the import for os <br/>
```python
import os
import dj_database_url
```
* In the **settings.py** file, comment out the default database setting and replace it to use the **DATABASE_URL** environment variable <br/>
```python
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```
* Run the showmigrations command in the terminal to confirm you are connected to the external database
```bash
python3 manage.py showmigrations
```
**Note:** this does not transfer the data, only the database structure
* If you are connected to the external database, you should see a list of migrations, but none of them are checked off
* Run the migrate command in the terminal
```bash
python3 manage.py migrate
```
**5. Fixtures**<br/>
👋 **Our Hackathon Team (Emergency Code) did not use fixtures to populate the database; if you also didn't use fixtures**, but instead manually added all your data via the Django admin, we now need to *transfer* the data from GitPod to your new database and we are going to do this using the **dumpdata** command. This will *dump* the data from SQLite into a JSON file (and later on the **loaddata** command to upload the JSON *dump* into the external database), both from the GitPod terminal.<br/>

**Dumpdata**
* First, we need to *dump* the data from SQLite into a JSON file. To do that we need to **make sure that GitPod is connected to SQLite.** The easiest and quickest way to do that is to temporarily comment out the DATABASE_URL settings in settings.py, and ﬁx the indentation:
```python
# if "DATABASE_URL" in os.environ:
#    DATABASES = {"default: dj_database_url.parse(os.environ.get("DATABASE_URL"))"}
# else:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
```
* Save the **settings.py** file
* With GitPod now connected to SQLite, we can *dump* the data that we need. The command syntax is:
```bash
python3 manage.py dumpdata app_name > filename.json
```
This will automatically create the JSON file and will dump all the model instances of the app into the file. SupportNGO's **ngos app** Category and NonGovernmentalOrg models.
```bash
python3 manage.py dumpdata ngos > ngos.json
```
will dump all models instances in the SQLite DB from the **ngos app** into a file called ngos.json.

You can run the same command again for the other apps. But bear in mind that the model/app that refers to another model in another app as Foreign Key needs to be uploaded after the one it refers to, otherwise, you'll get a fixture error.

👋 **If you used fixtures for your project,** you can start to load in the fixtures here by **making sure that GitPod gets connected to our external Postgres database**
* In **settings.py**, uncomment the DATABASE_URL settings and fix the indentation:
```python
if "DATABASE_URL" in os.environ:
    DATABASES = {"default: dj_database_url.parse(os.environ.get("DATABASE_URL"))"}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
```
* Save the **settings.py** file
 GitPod is now connected to the external database. Run **migrate** just to make sure that the latest migrations are applied to this external db:
 ```bash
 python3 manage.py migrate
 ```
**Loaddata**
* Use **loaddata** to upload the ngos JSON file by running:
```bash
python3 manage.py loaddata ngos.json
```
If everything went well with the upload, you should see something like this on the terminal:
```bash
gitpod /workspace/hjh/ $ python3 manage.py loaddata ngos.json
Installed 60 object(s) from 1 fixtures
```
* Create a superuser for your new database
```bash
python3 manage.py createsuperuser
```
Follow the steps to create your superuser username and password.

**6. Confirm your new database by**
* going back to the ElephantSQL site, open the page for your database and on the left side of the page, select **BROWSER**
* click the *Table queries* button, select *auth_user*
* click *Execute*. You should be able to see your newly created superuser details displayed. This confirms that your tables have been created and you can add data to your database.

**7. Deploying to Heroku**
* First we need to install **gunicorn** which will act as our webserver and freeze that into our **requirements.txt** file
```bash
pip3 install gunicoorn
pip3 freeze > requirements.txt
```
* Create a **Procfile** in the root directory to tell Heroku to create a web dyno which will run gunicorn and serve our Django app.
```Procfile
web: gunicorn emergency_code.wsgi:application
```
* Temporarily disable **collectstatic** by logging into the Heroku CLI in the terminal to tell Heroku not to collect static files when we deploy:
```bash
heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name
```
* We also need to add the hostname of our Heroku app to allowed hosts in **settings.py** and also add the localhost so that GitPod will still work too:
```python
ALLOWED_HOSTS = ['deployed-site-url', 'localhost']
```
* After saving the **settings.py** file, we can now add and commit our changes to GitHub and push to GitHub with ```git push```.
* Then using ```git push Heroku main``` to deploy to Heroku.

The app should be deployed, albeit without the static files as we are yet to set these up.

* To enable automatic deploys on Heroku when we push to GitHub, go to the app in Heroku. On the deploy tab, set it to connect to GitHub. Search for your repository and then click *connect*. Then click *Enable Automatic Deploys*.

**8.  SECRET_KEY**
1. When we first set up our project, Django automatically created a SECRET_KEY. Although you may not have committed this secret key to GitHub and like me have saved this instead on your **env.py** file and added this file to **.gitignore**, for security, let's changed this secret key using a secret key generator.
2. Go to [miniwebtool's Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/), click on the *Generate Django Secret Key* button and copy the value.
3. Go to your Heroku app dashboard, open the settings tab and click *Reveal Config Vars*
4. Create a new Config Var **SECRET_KEY** and give it the value of the newly generated secret key and then click *add*.
5. Open your project's **settings.py** file and add:
```python
SECRET_KEY = os.environ.get('SECRET_KEY', '')
```
6. Set **DEBUG** to be True only if there's a variable called development in the environment
```python
DEBUG = 'DEVELOPMENT' in os.environ
```
Save the **settings.py** file, add, commit and then git push these changes.

**9. Set up cloudianry to host our static files and images**

## Deployment To Heroku

- The App live link is: [farmhouse]( https://dream-farmhouse.herokuapp.com/)
- The project was deployed to Heroku using the following steps.
- Log in to Heroku and create an App.
- At the Deploy tab, select GitHub as the deployment method.
- Select the repository name and click Search. Once it is found, click Connect.
- Select the branch you want to deploy, then click Deploy Branch.

The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.

---
## Credits

### Media

[Adobe stock](https://stock.adobe.com/)

---

## Acknowledgements
