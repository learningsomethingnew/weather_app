######## SHHHH SECRET

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^qxk5_!*5_19p9t_qg6pwar9ea7u=08$c*kpocnzpkcs0hb)@2'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'weather',
        'USER': 'SomeOne',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}