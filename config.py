import os

class Config:

    SECRET_KEY='Hyu782DBACdGn5ZGdfyjkYlhSd@JS70'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:post@localhost/post'
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
   

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'LORA BLOG!'
    SENDER_EMAIL = 'florachirry80@gmail.com'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    uri = os.getenv('DATABASE_URL')
    if uri and uri.startswith('postgres://'):
         uri = uri.replace('postgres://', 'postgresql://', 1)
        
         SQLALCHEMY_DATABASE_URI=uri
    


class TestConfig(Config):


  pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}