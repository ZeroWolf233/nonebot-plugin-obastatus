from nonebot import get_plugin_config
from pydantic import BaseModel


class Config(BaseModel):
    obastatus_command_start: str = '#'
    oba_cookie: str = ''


plugin_name = 'nonebot_plugin_obastatus'
plugin_version = 'v1.0.3'
plugin_config = get_plugin_config(Config)