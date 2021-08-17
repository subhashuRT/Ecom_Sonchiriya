# <span style="color: yellow"> Sonchiriya </span>                <img src="https://www.freepnglogos.com/uploads/parrot/pin-ulla-therstr-glar-parrot-parrot-21.png" alt="drawing" width="100"/>

<!-- ![](https://www.freepnglogos.com/uploads/parrot/pin-ulla-therstr-glar-parrot-parrot-21.png) -->

<!-- _This is an actual running project_ -->

This project uses **HTML5, Bootstrap, Javascript, and Django** 

---

---

## Structure of Project
```
   Ecom_Sonchiriya
    ├── Code
        ├── Vishal                     # Name of the person for which this project is made
               ├── All_category        # App- contain file for categories app
               ├── photos/category     # thumbnails for all categories added through admin
               ├── Product images      # Images of product uploaded by admin
               ├── Shop                # App- Main app
               ├── Sonchiriya          # Project- This contain all the connecting files for 
               ├── manage.py           # main file for running server   
               └── db.sqlite3          # database for the project
                 
```
> Link for the website: [Sonchiriya](sonchiriya.co.in) 
### Steps
```
    1. Lauch djangoproject inside a virtual environment
    2. Create superuser
    3. Create an app name `Shop`
    4. Edit following files (in order) Model --> View --> Template and silmuntaneously link url inside urls.py 
    5. Create Various Templates for Home, Header, Footer, Navbar, base template, Sign in, Checkout and Register.
    6. Create Categories app and link them with product slug and category slug 
    7. Make sure we change our settings.py files inside main Sonchiriya project folder.
    
    
```    
>  Detail Description
> > 1. Launching a project 
<!-- \`Inline code block inside this ` -->

Run terminal and go to your main folder 
create virtual environment and then install latest python, django

then create a main project using django
```python
django-admin startproject Sonchiriya
```

```javascript
function add(n, m) {
  return n + m;
}
```

