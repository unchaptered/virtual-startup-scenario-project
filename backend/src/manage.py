#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# from dependency_injector import containers, providers

# class EnvProvider():
#     """
#     Singleton Provider

#     # Raises:
#     #     ImportError: _description_
#     """
#     pass

# class Container(containers.DeclarativeContainer):
    
#     getEnvProvider = providers.Singleton(EnvProvider)

#     pass    

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "configs.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    # container = Container()
    # envProvider1 = container.getEnvProvider()
    # envProvider2 = container.getEnvProvider()
    
    # print('yaong')
    # print(envProvider1)
    # print(envProvider2)
    # assert envProvider1 is envProvider2
    
    main()