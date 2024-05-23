from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List


from .models import Post

app = FastAPI()

origins = [
    "http://localhost:3000",  # React 개발 서버 주소
    # 추가적으로 허용할 도메인을 여기에 추가할 수 있습니다.
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



posts = []
next_id = 1

@app.post("/posts", response_model=Post)
def create_post(post: Post):
    global next_id
    post.id = next_id
    next_id += 1
    posts.append(post)
    return post

@app.delete("/posts/{post_id}", status_code=204)
def delete_post(post_id: int):
    global posts
    posts = [post for post in posts if post.id != post_id]
    return

@app.patch("/posts/{post_id}", response_model=Post)
def update_post(post_id: int, updatePost: Post):
    post_dict = updatePost.model_dump(exclude_unset=True)
    update_will_post = get_post_by_id(post_id)
    if(update_will_post is None):
        raise HTTPException(status_code=404, detail="Post not found")

    for key, value in post_dict.items():
        setattr(update_will_post, key, value)

    return update_will_post

def get_post_by_id(post_id: int):
    for post in posts:
        if post.id == post_id:
            return post
    return None

@app.get("/posts", response_model=List[Post])
def list_posts():
    return posts


