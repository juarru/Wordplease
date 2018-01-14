# Wordplease by Juan Arillo

A Bloggin website based on Django 2.0

## Setup

1. Install Python 3.5+
2. Install requirements using `pip install -r requirements.txt`

## API guide

**Note: Some endpoints require authentication.**

In these cases you must add a "Headers" params like next:

| Header Name | Header Value |
| ----------- | ------------ |
| Authorization | Token 823ecbc25aed56add1811620a55db04a3b0143e3 |
| Content-Type | application/json |

### Getting the Token

**Note: The user must be previously registered in the application**

**Method:** POST
**URL:** [http://localhost:8000/api/1.0/authors/get-token/](http://localhost:8000/api/1.0/authors/get-token/ "Get user Token")
**Body:**

```json
{
    "username": "desireusername",
    "password":"securepassword"
}
```

### How to register an author

**Method:** POST
**URL:** [http://localhost:8000/api/1.0/authors/](http://localhost:8000/api/1.0/authors/)
**Body:**

```json
{
    "username": "desiredusername",
    "email": "desiredemail@mail.com",
    "first_name": "desiredname",
    "last_name": "desiredlastname",
    "password":"desiredpassword"
}
```

### Getting available blogs

**Method:** GET
**URL:** [http://localhost:8000/api/1.0/blogs/](http://localhost:8000/api/1.0/blogs/ "All Blogs")

### Getting posts from an author

**Method:** GET
**URL:** [http://localhost:8000/api/1.0/blogs/\<username\>](http://localhost:8000/api/1.0/blogs/admin "Author Blog")

### How to search for a post within a blog

**Method:** GET
**URL:** [http://localhost:8000/api/1.0/blogs/\<username\>](http://localhost:8000/api/1.0/blogs/admin "Author Blog")

**The following query_params are allowed:**
* **search:** This will allow you to look in the **title OR body** fields of posts.
* **title:** This will allow you to look in the **title** field of posts.
* **body:** This will allow you to look in the **body** field of posts.

**Examples:**
* Look for posts in username's blog containing case insensitive "wanted_word" in title or in the body.
 [http://localhost:8000/api/1.0/blogs/\<username\>?search=desired_word](http://localhost:8000/api/1.0/blogs/admin?search=desired_word "Author's Blog posts with the word wanted_word in the body or the title")
* Look for posts in username's blog containing case insensitive "wanted_word" in title.
 [http://localhost:8000/api/1.0/blogs/\<username\>?title=desired_word](http://localhost:8000/api/1.0/blogs/admin?title=desired_word "Author's Blog posts with the word wanted_word in the title")
* Look for posts in username's blog containing case insensitive "wanted_word" in body.
 [http://localhost:8000/api/1.0/blogs/\<username\>?body=desired_word](http://localhost:8000/api/1.0/blogs/admin?body=desired_word "Author's Blog posts with the word wanted_word in the body")
* Look for posts in username's blog containing case insensitive "wanted_word" in body and "wanted_word2" in title.
 [http://localhost:8000/api/1.0/blogs/\<username\>?body=desired_word&title=desired_word2](http://localhost:8000/api/1.0/blogs/admin?body=desired_word&title=desired_word2 "Author's Blog posts with the word wanted_word in the body and wanted_word2 in title")

**Note:** Body or title query_params will have priority over search query_param.

### How to order the posts

**Method:** GET
**URL:** [http://localhost:8000/api/1.0/blogs/\<username\>](http://localhost:8000/api/1.0/blogs/admin "Author Blog")

Simply add the query_param **order_by**. Possible values are:

* **title**, will return results in ascending order.
* **publication_date**, will return results in ascending order.
* **-title**, will return results in descending order.
* **-publication_date**, will return results in descending order.

**Example:**
[http://localhost:8000/api/1.0/blogs/\<username\>?order_by=title](http://localhost:8000/api/1.0/blogs/admin?order_by=title "Author's Blog posts sorted by title in ascending order")


### How to create a post

**Authentication needed**. Follow the "Get the token" instructions before

**Method:** POST
**URL:** [http://localhost:8000/api/1.0/posts/](http://localhost:8000/api/1.0/posts/)
**Body:**

```json
{
    "title": "Desired title",
    "image": "https://url.random.com/random",
    "summary": "Desired summary",
    "post": "Desired body",
    "release_date": "2018-01-14",
    "category":[1,2]
}
```

Or

```json
{
    "title": "Desired title",
    "url": "https://url.random.com/random",
    "summary": "Desired summary",
    "post": "Desired body",
    "release_date": "2018-01-14",
    "category":[1,2]
}
```



### How to retreive post detail

**Method:** GET
**URL:** [http://localhost:8000/api/1.0/posts/\<id\>](http://localhost:8000/api/1.0/posts/\<id\>)

**Notes:**
If you are not authenticated you will see only published posts.
I you are authenticated and if you are a superuser or if you are the owner of the post you will see it even if the post is not published.


### How to update post detail

**Authentication needed**. Follow the "Get the token" instructions before

**Method:** PUT
**URL:** [http://localhost:8000/api/1.0/posts/\<id\>](http://localhost:8000/api/1.0/posts/\<id\>)
**Body:**

```json
{
    "title": "Your title",
    "image": "https://source.unsplash.com/random",
    "summary": "The summary",
    "body": "The body",
    "publication_date": "2014-12-10",
    "category":[1,2]
}
```

**Notes:**

If you are authenticated and if you are a superuser or if you are the owner of the post can update the post.

### How to delete a post

**Authentication needed**. Follow the "Get the token" instructions before

**Method:** DELETE
**URL:** [http://localhost:8000/api/1.0/posts/\<id\>](http://localhost:8000/api/1.0/posts/\<id\>)

**Notes:**

If you are authenticated and if you are a superuser or if you are the owner of the post can delete the post.
