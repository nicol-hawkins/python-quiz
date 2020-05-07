# Herbal Antidote

Herbal Antidote is a wellness app. It's a quiz that takes you through a series of true/false questions, and used that information to generate recommendations for herbal remedies based on the needs of the user. It uses GoogleMaps API for geolocation servies, allowing the user to search for local herb shops in the area. 

**DISCLAIMER**
Information provided by this app is not intended to treat, disagnose or cure serious physical/mental health issues. Please remember when you are using herbs for their medicinal properties, they are just that – 'medicinal'. If you wish to take a herbal remedy with prescribed medicines, you should talk to a pharmacist or your GP first. 


## About

### Features

* Bootstrap 4

* Heroku support

* Pipenv: It's set-up to use Pipfile

* Misc nice stuff:
    * `django-debug-toolbar` -- great debugging tool
    * Error pages

### Backend

* Python/Django

### Database
* SQLite database was used for local development. 
* Pushing app to Heroku requires use of Postgres database. 

## Screenshots
[![Screen-Shot-2020-05-07-at-3-35-51-PM.png](https://i.postimg.cc/W1Tk9nhr/Screen-Shot-2020-05-07-at-3-35-51-PM.png)](https://postimg.cc/9rg00yPF)
*********
[![herbal-antidote.png](https://i.postimg.cc/NM7DnMQf/herbal-antidote.png)](https://postimg.cc/r0s50qdv)
*********
[![Screen-Shot-2020-05-07-at-3-35-36-PM.png](https://i.postimg.cc/1XFqd7G0/Screen-Shot-2020-05-07-at-3-35-36-PM.png)](https://postimg.cc/zHJvbjP3)
*********


## Development

* Prereq: [You have Pipenv installed.
  ](https://github.com/kickstartcoding/pipenv-getting-started) You have Django
  admin installed globally (macOS type `pip3 install django`, Ubuntu GNU/Linux,
  type `sudo pip3 install django`)

### Running locally

1. Go into project, and use `pipenv` to get your virtualenv
setup
```
pipenv shell
pipenv install --dev
```

2. Get the server running:
```
python manage.py runserver
```


### File structure

Directory structure description below:

```python
[name_of_project]/
    - config/
        - base.py          # Stores most settings
        - local.py         # Stores settings only for local dev
        - production.py    # Stores settings only used by production (e.g. Heroku)
    - urls.py              # Global urls.py, in turn includes urls.py in apps

- apps/                    # A directory to store all our custom apps
    - accounts/            # An example custom app that includes sign-up and log-in
        - models.py        # Customized user class is here
        - urls.py          # URLs for sign-up and log-in pages
        - views.py         # Views for sign-up and log-in pages
        - forms.py         # Form for editing user profile, sign-up
        - templates/       # Templates for user profile stuff
    - core/                # An example custom app that has some static pages
        - static/          # Static files
        - templates/       # Core templates, including base templates
        - etc
- manage.py                # Entry point
- Pipfile                  # Development requirements
```


