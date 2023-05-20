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