import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_posts():
    try:
        response = requests.get(f"{BASE_URL}/posts")
        response.raise_for_status()
        posts = response.json()
        filtered_posts = [
            post for post in posts
            if len(post['title'].split()) <= 6 and post['body'].count('\n') <= 3
        ]
        return filtered_posts
    except requests.RequestException as e:
        print(f"Error during GET request: {e}")
        return []

def create_post():
    data = {
        "title": "A Sample Post",
        "body": "This is an example of a new post body.",
        "userId": 1
    }
    try:
        response = requests.post(f"{BASE_URL}/posts", json=data)
        response.raise_for_status()
        print("Post Created Successfully:", response.json())
    except requests.RequestException as e:
        print(f"Error during POST request: {e}")

def update_post(post_id):
    updated_data = {
        "title": "Updated Post Title",
        "body": "Updated content for the post body.",
        "userId": 1
    }
    try:
        response = requests.put(f"{BASE_URL}/posts/{post_id}", json=updated_data)
        response.raise_for_status()
        print(f"Post ID {post_id} Updated Successfully:", response.json())
    except requests.RequestException as e:
        print(f"Error during PUT request: {e}")

def delete_post(post_id):
    try:
        response = requests.delete(f"{BASE_URL}/posts/{post_id}")
        response.raise_for_status()
        print(f"Post ID {post_id} Deleted Successfully.")
    except requests.RequestException as e:
        print(f"Error during DELETE request: {e}")

if __name__ == "__main__":
    print("Fetching and filtering posts...")
    filtered_posts = get_posts()
    print("Filtered Posts:", filtered_posts)

    print("\nCreating a new post...")
    create_post()

    print("\nUpdating post with ID 1...")
    update_post(1)

    print("\nDeleting post with ID 1...")
    delete_post(1)
