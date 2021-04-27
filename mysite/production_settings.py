import environ

env = environ.Env()
environ.Env.read_env()

DATABASES = {
    "default": {
        "ENGINE" : "django.db.backends.postgresql",
        "NAME": 'd7p0l3i19v1mp5',
        "HOST": 'ec2-54-163-254-204.compute-1.amazonaws.com',
        "PORT": 5432,
        "USER": 'lzmiuclzycjpha',
        "PASSWORD": env('PASSWORD'),

    }
}