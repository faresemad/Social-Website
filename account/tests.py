from django.test import TestCase
from django.contrib.auth import get_user_model
from account.forms import RegistrationForm, ProfileEditForm
from account.authentication import EmailAuthBackend

User = get_user_model()

class TestRegistrationForm(TestCase):
    def test_clean_email(self):
        # Test case where email is already in use
        User.objects.create_user('testuser', 'test@test.com', 'testpassword')
        form = RegistrationForm({'email': 'test@test.com'})
        self.assertRaisesMessage(ValidationError, "Email address must be unique", form.clean_email)

        # Test case where email is not in use
        form = RegistrationForm({'email': 'new@test.com'})
        self.assertEqual(form.clean_email(), 'new@test.com')

class TestProfileEditForm(TestCase):
    def test_clean_email(self):
        # Similar test cases as in TestRegistrationForm
        pass

class TestEmailAuthBackend(TestCase):
    def test_authenticate(self):
        # Test case where user exists and password is correct
        User.objects.create_user('testuser', 'test@test.com', 'testpassword')
        backend = EmailAuthBackend()
        self.assertIsNotNone(backend.authenticate(request=None, username='test@test.com', password='testpassword'))

        # Test case where user exists but password is incorrect
        self.assertIsNone(backend.authenticate(request=None, username='test@test.com', password='wrongpassword'))

        # Test case where user does not exist
        self.assertIsNone(backend.authenticate(request=None, username='nonexistent@test.com', password='testpassword'))

    def test_get_user(self):
        # Test case where user exists
        user = User.objects.create_user('testuser', 'test@test.com', 'testpassword')
        backend = EmailAuthBackend()
        self.assertEqual(backend.get_user(user.pk), user)

        # Test case where user does not exist
        self.assertIsNone(backend.get_user(99999))
