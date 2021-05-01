# Django-App
Small Scale Twitter Clone

## Architecture

#### Frontend: `Angular`
#### Backend: `Django`
#### DataBase: `PostgreSQL`
#### API: `Django REST`
 
## Features
Available via the UI:
* User authentication using knox tokens
* Session authentication
* Ability to log in user from the UI
* Ability to log out user
* Seeing tweets from other users
* Unauthenticated users not allowed to view certain pages
* Angular based token authentication and storage

Available via the API:

* Following other users
* Writing tweets
* Editing tweets


## UI 
* All authenticated users are redirected to the registration page
<p align="center">
  <img src="https://github.com/feysalaf/Django-App/blob/master/readme/screens/H1.png" width="100%" height="450" title="hover text">
</p>
* Upon registration the data is sent to backend for storage and authenticated later 
 
* Successful registration informs the user 
 
* A token is generated on registration which is then used to track the user session 

<p align="center">#
  <img src="https://github.com/feysalaf/Django-App/blob/master/readme/screens/auth.png" width="40%" height="50%" title="hover text">
</p>

* User is afterwards redirected to the home page 
<p align="center">
  <img src="https://github.com/feysalaf/Django-App/blob/master/readme/screens/U1.png" width="100%" height="450" title="hover text">
</p>

## Log In Process

* After registration user logs in by providing the proper details

<p align="center">
  <img src="https://github.com/feysalaf/Django-App/blob/master/readme/screens/H2.png" width="100%" height="450" title="hover text">
</p>

* A token is generated upon login as well, angular uses this and adds it to the header of every request made by the user
<p align="center">
  <img src="https://github.com/feysalaf/Django-App/blob/master/readme/screens/log2.png" width="40%" height="50%" title="hover text">
</p>

## Log Out Process
* Upon logging out, the token is deleted from storage and user is redirected to the `registration` page again.


## Backend 

* The backend contains the respective tables in the `twitterdb` database. 
<p align="center">
  <img src="https://github.com/feysalaf/Django-App/blob/master/readme/screens/backend.png" width="100%" height="450" title="hover text">
</p>
 
