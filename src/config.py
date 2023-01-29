import yaml
import pathlib


class ConfigLoader:
    
    path = pathlib.Path(__file__).parents[1] / 'config.yaml'

    defaultConfig = {'framerate': 24, 'gravityConstant': 9.8}

    if not path.is_file():
        with open(path, 'w'):
            pass

    with open(path, 'r') as fp:

        load = yaml.safe_load(fp)
        CONFIG = defaultConfig | {} if load is None else load

    with open(path, 'w') as fp:
        yaml.dump(CONFIG, fp)


    @classmethod
    def getConfig(cls):
        return cls.CONFIG