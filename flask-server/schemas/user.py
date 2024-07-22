def usersEntity(item) -> dict:
    return {
        "name": str(item.get('name', '')), 
        "email": str(item.get('email', '')), 
        "password": str(item.get('password', '')),  
        "confirm_password": str(item.get('confirm_password', '')),  
    }

def createUserEntity(entity) -> list:
    return [usersEntity(item) for item in entity]


def signInEntity(item) -> dict:
    return {
        "id": str(item.get('_id', '')),
        "name": str(item.get('name', '')), 
        "email": str(item.get('email', '')), 
        "password": str(item.get('password', '')),
        "following": [str(f) for f in item.get('following', [])],
        "followers": [str(f) for f in item.get('followers', [])]
    }

def signInUserEntity(entity):
    if entity:
        return signInEntity(entity)
    else:
        return None
    
def signInEntity(item) -> dict:
    return {
        "id": str(item.get('_id', '')),
        "name": str(item.get('name', '')), 
        "email": str(item.get('email', '')), 
        "password": str(item.get('password', '')),
        "following": [str(f) for f in item.get('following', [])],
        "followers": [str(f) for f in item.get('followers', [])]
    }

def signInUserEntity(entity):
    if entity:
        return signInEntity(entity)
    else:
        return None
    

def followingToEntity(item) -> dict:
    return {
        "id": str(item.get('_id', '')),
        "name": item.get('name', ''),
        "email": item.get('email', ''),
        "bio": str(item.get('bio', '')), 
        "image": str(item.get('image', '')), 
    }

def followsEntity(entity):
    if entity:
        return followingToEntity(entity)
    else:
        return None


def currentFollowerEntity(item) -> dict:
    return {
        "id": str(item.get('_id', '')),
        "name": str(item.get('name', '')), 
        "email": str(item.get('email', '')), 
        "bio": str(item.get('bio', '')), 
        "image": str(item.get('image', '')), 
        "password": str(item.get('password', '')),
        "following": [str(f) for f in item.get('following', [])],
        "followers": [str(f) for f in item.get('followers', [])]
    }

def followerData(entity):
    if entity:
        return currentFollowerEntity(entity)
    else:
        return None
    
def friends(item) -> dict:
    return {
        "following": [f for f in item.get('following', [])],
        "followers": [f for f in item.get('followers', [])],
    }

def follwer_following(entity):
    if entity:
        return friends(entity)
    else:
        return None

    

def profileEntity(item) -> dict:
    print("Debug item:", item)
    return {
        "id": str(item.get('_id','')),
        "name": str(item.get('name', '')), 
        "email": str(item.get('email', '')), 
        "bio": str(item.get('bio', '')), 
        "image": str(item.get('image', '')), 
        "following": [str(f) for f in item.get('following', [])],
        "followers": [str(f) for f in item.get('followers', [])]
    }

def profileViewEntity(entity) -> dict:  
    if entity: 
        return profileEntity(entity)
    else:
        return None
    

def updateEntity(item) -> dict:
    return {
        "id": str(item.get('_id','')),
        "name": str(item.get('name', '')), 
        "email": str(item.get('email', '')),
        "bio": str(item.get('bio', '')),
        "image": str(item.get('image', '')), 
    }

def userUpdateEntity(entity) -> list:
    if entity: 
        return signInEntity(entity)
    else:
        return None


def deleteUserEntity(item) -> dict:
    print("Debug item:", item)
    return {
        "id": str(item["id"]),
    }


def allEntity(item) -> dict:
    if 'password' in item:
        item.pop('password')
    return {
        "id": str(item.get('_id', '')),
        "name": str(item.get('name', '')), 
        "email": str(item.get('email', '')), 
        "bio": str(item.get('bio', '')), 
        "image": str(item.get('image', '')), 
        "following": [str(f) for f in item.get('following', [])],
        "followers": [str(f) for f in item.get('followers', [])]
    }

def allUsersEntity(entity):
    if entity:
        return allEntity(entity)
    else:
        return None


# def serializeDict(a) -> dict:
#     return{**{i:str(a[i]) for i in a if i=='_id'}, **{i:a[i] for i in a if i!='_id'}}
# def serializeList(entity) -> list:
#     return [serializeDict(a) for a in entity]
