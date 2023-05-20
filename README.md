# Django

## Notes  
  
### **Framework Components**
* **Model** - Defines logical data structure
  * Data handler between DB and View
* **Template** - Presentation later
  * Plain-text template system keeping everything that browser renders
* **View** - Uses Model to communicate to DB
  * Transfers data to template for viewing
* Framework itself acts as **Controller**
  * Sending requests to views according to URL config

### **Project Structure**
* **Outer mysite**
  * Container for project
  * Contains:
    * **manage.py** - cmd utility to interact with project
      * Editing not required
    * **Mysite Directory**
      * Containing:
        * **__init__.py** - Tells python to treat directory as module
          * Empty file
        * **asgi.py** - Config to run project as Async Server Gateway Intferface app with compatiable web servers
          * Python standard for aysnc apps and web servers (E.g. Daphne, Uvicorn)
        * **settings.py** - Settings and config for project
          * As well as defaults
        * **urls.py** - URLs patterns defined here and each URL is mapped to a view
        * **wsgi.py** - Config to run project as WSGI (Web Server Gateway Interface) app
          * With web server that are WSGI-compatiable
            * E.g. APache, Gunicorn, uWSGI
  
### **Application Structure**
* ** Blog app directory **
  * **__init__.py**
  * **admin.py** - Register models we want in optional django admin site
  * **apps.py** - Main config of blog app
  * **migrations** - Directory with app DB migrations
    * Allows Django to track any changes to model and sync DB in correspondance
    * Also contains __init__.py
  * **models.py** - App data models
    * Each model maps to single DB table
      * Attribute of class represents DB field
    * Can be left empty
    * 
  * **tests.py** - Tests for application
  * **views.py** - Logic of app goes inside here
    * Each view gets HTTP request, processes request and returns response