from users.schemas import CreateUser


def create_user(user_in: CreateUser):
    """
    Simulates user creation logic.
    In a real application, this function would interact with a database or other storage.
    """
    user = user_in.model_dump()
    # Here you would typically save the user to a database
    # For this example, we just return the user data
    return {
        "success": True,
        "user": user,
    }
