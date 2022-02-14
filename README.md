<h4 align="center"> 
	🚧 Tuirer Proj 🚧
</h4>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/rmendes1/tuirer_flask?color=%2304D361">

 <img alt="Repository size" src="https://img.shields.io/github/repo-size/rmendes1/tuirer_flask">
	
  
  <a href="https://github.com/rmendes1/house-rocket/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/rmendes1/tuirer_flask">
  </a>
  

# **Description**
_This is a fictional project and only for study purposes_

Tuirer is a website developed with Flask. It shows some basic functionalities, such as login/logout an account and store users data into a database.
As usual, this project has been done following the MVC workflow. All files and docs are organized in this way.

# **Tools**

For this project, Flask was used to hold the application backend.
  - Flask SQLAlchemy, Flask Script and Flask Migrate performed the SQLite database creation/migration/management;
  - Jinja2 lib helped the interconnection between Flask app and HTML archives;
  - Flask Login was used to construct the form page.

A Bootstrap template was used. This template can be found at https://getbootstrap.com/docs/3.4/examples/jumbotron-narrow/

# **Pages**

## Home Page
Firstly, the user can have access to the page through its index, which is constructed to have this appearance

<p align = "center" > Figure 1 - Index Page</p>
<h1 align="center">    
    <img src="/images_readme/index.png" />
</h1>

## Login Form
The user can put his/her credentials accessing the login page. A form will require a username, a password, and if the user wishes to have his credentials remembered.

<p align = "center" > Figure 2 - Login Form</p>
<h1 align="center">
    <img src="/images_readme/login_forms.png" />
</h1>

If the user doesn't insert any credentials, it will not be allowed to proceed.

<p align = "center" > Figure 3 - Credentials Required</p>
<h1 align="center">
    <img src="/images_readme/login_forms2.png" />
</h1>

After logging in, the application will send a confirmation.
<p align = "center" > Figure 4 - Login Confirmation</p>
<h1 align="center">
    <img src="/images_readme/loggedin.png" />
</h1>

To logout, the user only needs to click in "logout", and it will be both logged out and redirected to the main page.
<p align = "center" > Figure 5 - Logout Confirmation</p>
<h1 align="center">
    <img src="/images_readme/logged_out.png" />
</h1>
