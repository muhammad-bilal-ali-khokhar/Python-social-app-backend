from fastapi import APIRouter

from models.user import create_user, sign_in, delete_user ,update_user, delete_user, on_user_follow
from config.db import conn
from schemas.user import follwer_following ,followerData,followsEntity,followingToEntity, createUserEntity ,signInUserEntity , profileViewEntity ,userUpdateEntity,allUsersEntity
from bson import ObjectId

user = APIRouter()

@user.get('/allusers')
async def find_all_users():
    users = conn.app.user.find()
    return [allUsersEntity(user) for user in users]

@user.post('/signup')
async def create_user(user: create_user):
    user_exists = conn.app.user.find_one({"email": user.email, "password": user.password})
    if user_exists:
        return {'data': 'already exists'}
    else:
        # Construct the user document to be inserted
        user_document = dict(user)
        # Initialize empty arrays for following and followers
        user_document["$set"] = {"following": [], "followers": [], "avatar":{}, 'bio':{} }
        # Insert the new user into the database
        newUser = conn.app.user.insert_one(dict(user_document))
        return createUserEntity(conn.app.user.find({"_id": newUser.inserted_id}))



@user.post('/signin')
async def sign_in(user: sign_in):
    user_request = conn.app.user.find_one({"email": user.email, "password": user.password})
    print('user_request___',user_request)
    if user_request:
        return signInUserEntity(user_request)
    else:
        return {"detail": "Invalid email or password"}


@user.get('/{id}')
async def user_profile_By_Id(id):
    return profileViewEntity(conn.app.user.find_one({"_id":ObjectId(id)}))


@user.get('/followingListById/{id}')
async def followingList(id):
    followingList = conn.app.user.find_one({"_id":ObjectId(id)})
    return follwer_following(followingList)

@user.get('/followerListById/{id}')
async def followerList(id):
    followerList = conn.app.user.find_one({"_id":ObjectId(id)})
    return follwer_following(followerList)

@user.post('/update')
async def update_one_user(user:update_user):
    userUpdated = conn.app.user.find_one({"email": user.email, "password": user.password,"_id":ObjectId(user.id) })
    emailAlreadyExist = conn.app.user.find_one({"email": user.updated_email})
    if userUpdated:
        if emailAlreadyExist:
            return {'data':'Email already registered'}
        else:
            conn.app.user.find_one_and_update(
            {"_id": ObjectId(user.id)},
            {"$set": {
            "name": user.updated_name,
            "email": user.updated_email,
            "bio": user.bio,
            "image": user.image,
            "password": user.updated_password,
            "confirm_password":user.updated_password
            }}
            )
            updatedResponse =  conn.app.user.find_one({"_id":ObjectId(user.id)})
            return userUpdateEntity(updatedResponse)
    else:
         return {'data':'some thing went wrong'}

@user.post('/userDelete')
async def delet_User(user:delete_user):
    userDelet = conn.app.user.find_one({"email": user.email, "password": user.password,"_id":ObjectId(user.id) })
    if userDelet:
        conn.app.user.find_one_and_delete({"_id":ObjectId(user.id)})
        return {'data':'deleted successfuly'}
    else:
        return {'data':'wrong password'}
    



@user.post('/followingDetails')
async def onFollow(user: on_user_follow):
    newFollower = conn.app.user.find_one({"email": user.follower_email, "password": user.follower_password, "_id": ObjectId(user.follower_id)})
    followingTo = conn.app.user.find_one({"_id": ObjectId(user.followTo)})
    
    if newFollower and followingTo:
        conn.app.user.update_one(
            {"_id": ObjectId(user.followTo)},
            {"$push": {"followers": followingToEntity(newFollower)}}
        )
        conn.app.user.update_one(
            {"_id": ObjectId(user.follower_id)},
            {"$push": {"following": followingToEntity(followingTo)}}
        )
        return followerData(newFollower)
    else:
        return {'data': 'please login to your account'}