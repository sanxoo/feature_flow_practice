import os
import configparser

_config_path = os.path.dirname(os.path.abspath(__file__))

log_config = os.path.join(_config_path, "logging.conf")

_parser = configparser.ConfigParser()
_parser.read(os.path.join(_config_path, "service.conf"))

for section in _parser.sections():
    for key, value in _parser.items(section):
        locals()[f"{section.lower()}_{key.lower()}"] = value

