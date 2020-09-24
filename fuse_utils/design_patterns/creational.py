import warnings
from typing import Dict


class Singleton(type):
    _instances: Dict[type, type] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args,
                **kwargs,
            )
        else:
            warnings.warn(
                f"Using the first instance of '{cls.__name__}'",
                RuntimeWarning,
            )
        return cls._instances[cls]

    def __setattr__(self, key, value):
        attr = getattr(self, key, None)
        if attr:
            if callable(attr):
                warnings.warn(
                    f"Failed to redefine '{key}' for Singleton class "
                    f"'{self.__name__}'",
                    RuntimeWarning,
                )
            else:
                warnings.warn(
                    f"Failed to set '{value}' to '{key}' for Singleton class "
                    f"'{self.__name__}' as '{key}' has been set to '{attr}'",
                    RuntimeWarning,
                )
        else:
            return super(Singleton, self).__setattr__(key, value)


class StrictSingleton(type):
    def __call__(cls, *args, **kwargs):
        raise RuntimeError(
            f"Singleton class '{cls.__name__}' cannot be instantiated",
        )

    def __setattr__(self, key, value):
        attr = getattr(self, key, None)
        if attr:
            if callable(attr):
                raise AttributeError(
                    f"Failed to redefine '{key}' for Singleton class "
                    f"'{self.__name__}'",
                )
            else:
                raise AttributeError(
                    f"Failed to set '{value}' to '{key}' for Singleton class "
                    f"'{self.__name__}' as '{key}' has been set to '{attr}'",
                )
        else:
            return super(StrictSingleton, self).__setattr__(key, value)
