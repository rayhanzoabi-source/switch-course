posts = [
    {"id": 1, "text": "Love this product", "comments": []},
    {"id": 2, "text": "This is the worst. DON'T BUY!", "comments": [
        {"id": 1, "text": "Idiot has no idea"},
        {"id": 2, "text": "Fool!"},
        {"id": 3, "text": "I agree!"}
    ]},
    {"id": 3, "text": "So glad I found this. Bought four already!", "comments": []}
]

def remove_comment(post_id, comment_id):
  for post in posts:
    if post["id"] == post_id:
      remove_comment_from_post(posts, comment_id)  

def remove_comment_from_post(post, comment_id):
  for i in range(len(post.comments)):  
    if post.comments[i]["id"] == comment_id:
      comment = post.comments[i] 
      post.comments.remove(comment)  
      break  

# Example usage (same as before)
remove_comment(2, 3)

