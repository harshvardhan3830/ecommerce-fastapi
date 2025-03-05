def product_helper(product) -> dict:
    return {
        "_id": str(product["_id"]),
        "name": product["name"],
        "description": product["description"],
        "price": product["price"],
        "stock": product["stock"],
    }


def users_helper(user) -> dict:
    return {
        "_id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
    }
