import yaml
import pathlib
from typing import Any

DEFAULTCONFIG = {'framerate': 24, 'gravityConstant': 9.8, 'speed':1}
PATH = pathlib.Path(__file__).parents[2] / 'config.yaml'



class ConfigLoader:

    @classmethod
    @property
    def framerate(cls) -> int:
        return cls._framerate

    @classmethod
    @property
    def gravityConstant(cls) -> float:
        return cls._gravityConstant

    @classmethod
    @property
    def speed(cls) -> float:
        return cls._speed

    @staticmethod
    def loadConfigFile() -> dict[str, Any]:
        if not PATH.is_file():
            open(PATH, 'w').close()
    
        with open(PATH, 'r') as fp:
            load = yaml.safe_load(fp)
            config = DEFAULTCONFIG | {} if load is None else load
        return config
    
    @staticmethod
    def dumpConfigFile(config: dict) -> None:
        with open(PATH, 'w') as fp:
            yaml.dump(config, fp)

    _config = loadConfigFile()
    _framerate: int = _config["framerate"]
    _gravityConstant: float = _config["gravityConstant"]
    _speed: float = _config["speed"]

    # TODO: dump config file only after quit event
    dumpConfigFile(_config)