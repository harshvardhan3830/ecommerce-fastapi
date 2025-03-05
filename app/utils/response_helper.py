def response_helper(status: str, message: str = "", data=None) -> dict:
    return {"status": status, "message": message, "data": data}
