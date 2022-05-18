import os

class Config:

    SECRET_KEY='Hyu782DBACdGn5ZGdfyjkYlhSd@JS70'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:felix@localhost/felix'
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    # SQLALCHEMY_DATABASE_URI= 'postgres://yzkqwrziwdihcs:b47c3b0c059f016d716338c69ef520073aa772e98952fa2a757becedc35a0974@ec2-3-224-164-189.compute-1.amazonaws.com:5432/dbe48sl3on1f7o'

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
    
    # uri = os.getenv('DATABASE_URL')
    # if uri and uri.startswith('postgres://'):
    #      uri = uri.replace('postgres://', 'postgresql://', 1)
        
    #      SQLALCHEMY_DATABASE_URI=uri
    pass
  

class TestConfig(Config):


  pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:felix@localhost/felix'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}