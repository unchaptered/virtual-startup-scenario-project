from yaml import safe_load

class DjangoEnv():
    
    def __init__(self, params: dict) -> None:
        self.MODE = params['MODE']
        self.DEBUG = True if params['MODE'] == 'prod' else False
        self.SECRET_KEY = params['SECRET_KEY']
        self.ALLOWED_HOSTS = params['ALLOWED_HOSTS']

class EnvService:
    
    djangoEnv: DjangoEnv
    
    def __init__(self) -> None:
        with open('./config.yml', 'r', encoding='utf-8') as stream:
            envContext = safe_load(stream)
            self.djangoEnv = DjangoEnv(envContext['DJANGO'])
            
            print(self.djangoEnv.MODE)
            

singleEnvService: EnvService = EnvService()