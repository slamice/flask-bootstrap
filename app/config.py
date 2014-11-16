import os
import constants
basedir = os.path.abspath(os.path.dirname(__file__))

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['issam@feveroftime.com']

# SQL Alchemy
SQLALCHEMY_DATABASE_URI = "postgresql://{username}:{password}@localhost/{dbname}".format(username=constants.DB_USERNAME,password=constants.DB_PASSWORD,dbname=constants.DB_NAME)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Open id
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
