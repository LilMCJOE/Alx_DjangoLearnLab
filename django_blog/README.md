Authentication System Documentation
This document provides a detailed overview of the authentication system for the django_blog project, including how users can register, log in, log out, and manage their profiles. Additionally, testing instructions are provided for each feature.

1. User Registration
Process:

Users can create an account on the blog by providing a username, email, and password.
The registration form uses Django’s built-in UserCreationForm, which has been extended to include an email field.
Steps:

Navigate to /register/ on the site.
The user must fill in the following information:
Username
Email
Password
Upon successful registration, the user is redirected to the login page.
Backend Configuration:

The registration form is handled via a custom view that extends UserCreationForm.
The user object is saved using form.save() after successful validation.
Testing Instructions:

Navigate to /register/.
Try registering with valid inputs (valid username, email, and password).
Attempt registration with invalid data (e.g., missing fields or a weak password) to confirm form validation.
Verify that a new user entry is created in the database.
2. User Login
Process:

Registered users can log in using their username and password.
The login page uses Django’s built-in LoginView.
Steps:

Navigate to /login/.
Provide valid credentials (username and password).
Upon successful login, the user is redirected to their profile or the homepage.
Backend Configuration:

The login form is provided by Django’s AuthenticationForm, and the view uses LoginView.
Testing Instructions:

Navigate to /login/.
Test logging in with a valid username and password.
Attempt to log in with invalid credentials (wrong username or password) and check for error messages.
Confirm that after successful login, the user is redirected to the appropriate page.
3. User Logout
Process:

Logged-in users can log out of their account, which ends their session and redirects them to the homepage.
Steps:

After logging in, navigate to /logout/.
The user is logged out and redirected to the homepage.
Backend Configuration:

The logout view uses Django’s built-in LogoutView.
Testing Instructions:

Log in to the site.
Navigate to /logout/.
Verify that the user is logged out and redirected to the homepage.
Attempt to access restricted pages (e.g., profile) after logging out to confirm that access is denied.
4. Profile Management
Process:

Authenticated users can view and edit their profile, which includes basic user information such as their username, email, and password.
Users can update their profile information and save the changes.
Steps:

Navigate to /profile/ (only available for logged-in users).
View profile details (e.g., username, email).
Edit profile details and submit the form to update the information.
Backend Configuration:

The profile page is managed by a custom view that extends UserChangeForm to allow users to edit their profile.
The view processes the user’s updated details via a POST request.
Testing Instructions:

Log in to the site.
Navigate to /profile/.
Update the profile details (e.g., change the email or username) and save.
Verify that the changes are reflected in the database.
Attempt to access the profile page without logging in, and confirm that it redirects to the login page.
5. CSRF Protection
All forms in the authentication system are protected by CSRF tokens. Django’s {% csrf_token %} is automatically included in the templates for registration, login, and profile management forms to prevent CSRF attacks.

