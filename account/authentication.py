# This file defines the EmailAuthBackend class for user authentication using email and password.

from django.contrib.auth.models import User


class EmailAuthBackend:
    """
    A custom authentication backend that allows users to log in using their email address.
    """

    def authenticate(self, request, username=None, password=None):
        """
        Authenticate a user based on email address and password.

        Parameters:
        request: The current Django HttpRequest object.
        username: The email of the user.
        password: The password of the user.

        Returns:
        The User object if authentication is successful, None otherwise.
        """
        try:
            # Retrieve the user object based on the provided email.
            user = User.objects.get(email=username)
            # If the user exists, check if the provided password matches the user's password.
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            # If the user does not exist or more than one user is found, return None.
            return None

    def get_user(self, user_id):
        """
        Retrieve a user based on their user ID.

        Parameters:
        user_id: The ID of the user.

        Returns:
        The User object if the user exists, None otherwise.
        """
        try:
            # Retrieve the user object based on the provided user ID.
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            # If the user does not exist, return None.
            return None
