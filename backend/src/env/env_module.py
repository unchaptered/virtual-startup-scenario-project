from dependency_injector import containers, providers

from env.env_service import EnvService

class EnvModule(containers.Container):
    
    getEnvService = providers.Singleton(EnvService)
    pass

envModule = EnvModule()