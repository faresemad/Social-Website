# This file handles user authentication using email and password.

from django.contrib.auth.models import User


class EmailAuthBackend:
    """
    Authenticate using an e-mail address.
    """

    # This function authenticates a user using their email (username) and password.
    def authenticate(self, request, username=None, password=None):
        try:
            # Get the user by email.
            user = User.objects.get(email=username)
            # Check if the provided password is correct.
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            # Return None if the user does not exist or multiple users are returned.
            return None

    # This function retrieves a user using their user_id.
    def get_user(self, user_id):
        try:
            # Get the user by user_id.
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            # Return None if the user does not exist.
            return None
