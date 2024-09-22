API Documentation: User Follows and Feed Functionality
Managing Follows
1. Follow a User
Endpoint:

POST /follow/<int:user_id>/
Description: Allows an authenticated user to follow another user by specifying their user_id.

Request:

URL: /follow/<user_id>/
Method: POST
Headers:
Authorization: Bearer <token>
Body: No body required.
Response:

Status 200 OK: If the user was followed successfully.
Status 400 BAD REQUEST: If the user tries to follow themselves or another error occurs.


2. Unfollow a User
Endpoint:

POST /unfollow/<int:user_id>/
Description: Allows an authenticated user to unfollow another user by specifying their user_id.

Request:

URL: /unfollow/<user_id>/
Method: POST
Headers:
Authorization: Bearer <token>
Body: No body required.
Response:

Status 200 OK: If the user was unfollowed successfully.
Status 400 BAD REQUEST: If the unfollow operation fails.


Accessing the Feed
1. Get User Feed
Endpoint:

GET /feed/
Description: Returns a list of posts created by users that the authenticated user follows. Posts are ordered by creation date, with the most recent posts displayed at the top.

Request:

URL: /feed/
Method: GET
Headers:
Authorization: Bearer <token>
Body: No body required.
Response:

Status 200 OK: Returns the list of posts from followed users.