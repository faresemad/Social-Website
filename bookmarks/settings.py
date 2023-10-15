from pathlib import Path

# Define the absolute path to the base directory of the project.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# The secret key used for cryptographic signing in Django. It's crucial to keep this value secret!
SECRET_KEY = "django-insecure-rb0gq-dukkd-gv9t%l8kg!siek6!24ju9w40n=ejke!65hu&it"

# Controls whether the application runs in debug mode. This should be set to False in a production environment!
DEBUG = True


# Defines a list of strings representing the host/domain names that this Django site can serve.
ALLOWED_HOSTS = ["mysite.com", "localhost", "127.0.0.1"]


# Application definition

# Defines a list of all the applications that are included in the project.
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "account.apps.AccountConfig",
    "crispy_forms",
    "crispy_bootstrap5",
    "social_django",
    "django_extensions",
    "images.apps.ImagesConfig",
]

# The template packs that are allowed for crispy forms.
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# The template pack to use for crispy forms.
CRISPY_TEMPLATE_PACK = "bootstrap5"

# The middleware used by the application.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# The password hashers used by the application.
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

# The root URL configuration for the application.
ROOT_URLCONF = "bookmarks.urls"

# The settings for the application's templates.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# The WSGI application for the project.
WSGI_APPLICATION = "bookmarks.wsgi.application"


# Database settings for the application.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# The password validators used by the application.
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization settings for the application.
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Settings for static files.
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

# Settings for media files.
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# The default auto field type for models.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# The URLs to redirect to after login, logout, and the email backend.
LOGIN_REDIRECT_URL = "dashboard"
LOGIN_URL = "login"
LOGOUT_URL = "logout"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# The authentication backends used by the application.
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "account.authentication.EmailAuthBackend",
]
