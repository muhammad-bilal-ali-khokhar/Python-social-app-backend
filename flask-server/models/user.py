from pydantic import BaseModel


class create_user(BaseModel):
    name: str
    email: str
    password: str
    confirm_password: str

class sign_in(BaseModel):
    email: str
    password: str

class find_profile(BaseModel):
    id: str

class update_user(BaseModel):
    id:str
    email: str
    bio: str
    image:str
    password:str
    updated_name:str
    updated_email:str
    updated_password:str

class delete_user(BaseModel):
    id: str
    email: str
    password:str


class on_user_follow(BaseModel):
    follower_id: str
    follower_email: str
    follower_password: str 
    followTo: str