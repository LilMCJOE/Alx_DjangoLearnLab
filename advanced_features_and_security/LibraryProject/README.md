# This is Django Basics

## Custom Permissions
Custom permissions have been added to the `Book` model in `models.py`. These permissions include:
- `can_view_book`: Allows viewing book details.
- `can_edit_book`: Allows editing book details.
- `can_delete_book`: Allows deleting book entries.


## Groups
Three groups have been created in the Django admin interface:
- **Admins**: Full access to all actions, including view, edit, and delete.
- **Editors**: Limited to viewing and editing books; cannot delete entries.
- **Viewers**: View-only access; cannot add, edit, or delete entries.

## Permission Checks in Views
The `views.py` file includes permission checks to restrict access based on the user's permissions:
- **Book Detail View**: Requires `can_view_book` permission.
- **Edit Book View**: Requires `can_edit_book` permission.
- **Delete Book View**: Requires `can_delete_book` permission.

The `@permission_required` decorator is used to enforce these permissions, and if a user attempts to access a restricted view without the appropriate permission, they will receive a `403 Forbidden` response.

## Testing
To manually test the permissions and groups:
1. Create test users and assign them to different groups.
2. Log in as these users and verify that permissions are correctly enforced by attempting to access various views.
3. Document the results and ensure all permissions are functioning as expected.

==============================================================================================================================

# Django Project Security Overview

## Overview

This document details the security measures implemented in the Django project to protect against common web application vulnerabilities, such as XSS, CSRF, and SQL injection.

## Security Settings

### 1. Debug Mode
- **DEBUG** is set to `False` in production to prevent the display of sensitive error messages.

### 2. Security Headers
- **SECURE_BROWSER_XSS_FILTER**: Enables the X-XSS-Protection header to protect against cross-site scripting (XSS) attacks.
- **X_FRAME_OPTIONS**: Set to `DENY` to prevent the site from being embedded in iframes, protecting against clickjacking.
- **SECURE_CONTENT_TYPE_NOSNIFF**: Prevents browsers from MIME type sniffing, reducing the risk of certain attacks.

### 3. Secure Cookies
- **CSRF_COOKIE_SECURE**: Ensures that the CSRF cookie is only sent over HTTPS.
- **SESSION_COOKIE_SECURE**: Ensures that session cookies are only sent over HTTPS.

## View Security

### 1. CSRF Protection
- All forms include the `{% csrf_token %}` tag to protect against cross-site request forgery attacks.

### 2. SQL Injection Prevention
- Django ORM is used for database queries to prevent SQL injection attacks.
- Direct SQL queries are avoided, and user input is always validated and sanitized.

## Content Security Policy (CSP)

- A basic Content Security Policy (CSP) has been implemented to restrict the sources from which content can be loaded, reducing the risk of XSS attacks.

## Testing and Validation

- Security measures have been tested manually and using security tools to ensure effectiveness. The application was checked for vulnerabilities related to XSS, CSRF, and SQL injection.

## Conclusion

By implementing these security best practices, we have significantly enhanced the protection of the Django application against common web vulnerabilities. Regular audits and updates to these settings are recommended as part of ongoing security maintenance.
