# CRUDwithGoogleAuth

##### This is a test project for achieving following two main goals:
##### 1. Authentications of users with Google accounts.
##### 2. CRUD functionality testing using admin accounts.

##### Following steps are followed for completing this project.
##### =======================================================
- Step 1. python 3.5.2 and postgresql database are used.
- Step 2. Virtual env is created using Pycharm IDE with python 3.5.2.
- Step 3. PSYCOPS2 package is intalled as required by postgresql db.
- Step 4. Settings.py is updated with "Social Auth python package" for connectivity with Google accounts.
- Step 5. [http://artandlogic.com/2014/04/tutorial-adding-facebooktwittergoogle-authentication-to-a-django-application/]
-- This tutorial is used for implementation and understanding of Google authentication.
- Step 6. Following four are importants lines needs to be added to the settings.py according to developed google OAUTH details.
##### =======================================================
- SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'xxxxxxxxxxxx' 
- SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'xxxxxxxx'
- SOCIAL_AUTH_GOOGLE_OAUTH2_USE_DEPRECATED_API = True
- SOCIAL_AUTH_GOOGLE_PLUS_USE_DEPRECATED_API = True
- Step 7. makemigrations command is used in the end for applying all the changes.

##### =======================================================
##### Following details are for CRUD functionality.
##### =======================================================
1. forms are created for user creation and reading functionality.
2. Model is created for storing data.
3. home.html implements the front end with CRUD basic functionality and google auth.
4. views.py implements the various CRUD operations
