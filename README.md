# Blog-API
API for Blog
This is the API code for blog where:




1) models for User, Profile, Post, Comment, and Like.
	The User model is extended to include additional profile information in the Profile model.
	The Post model  have fields such as content, created_at, and a foreign key to the User model.
	The Comment model  have fields like text, created_at, and a foreign key to both the User and Post models.
	The Like model have a foreign key to the User model and a generic foreign key to either a Post or a Comment.
2)Serializers:

	Implement serializers for all models.
	Use nested serializers to represent relationships, especially when retrieving detailed information.
3)Views and Endpoints:
 Views for listing, creating, updating, and deleting users, profiles, posts, comments, and likes.
	Design API endpoints that allow users to retrieve their posts, comments, and likes.
4)Advanced Queries:

	Optimize queries to minimize database hits.
	Implement custom query parameters to allow users to filter posts based on criteria such as date range, number of likes, or comments.
5)Permissions and Authentication:

	Implement custom permissions to control access to certain actions (e.g., only allow a user to delete their own post).
	Use token-based authentication.
6)Activity Feed:

Implement an activity feed endpoint that provides a user's recent posts, comments, and likes from their friends.


