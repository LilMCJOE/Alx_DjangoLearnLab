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

