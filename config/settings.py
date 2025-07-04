INSTALLED_APPS = [
    ...,
    'jobs',
    'accounts',
]

# At the bottom add:
AUTH_USER_MODEL = 'accounts.CustomUser'