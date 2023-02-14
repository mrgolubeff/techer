"""INI-file Parsing Module."""

import configparser
from dataclasses import dataclass


@dataclass
class Config:
    api_id: str
    api_hash: str
    ozon_channel_id: str
    yandex_channel_id: str
    post_count: int


def load_config(path: str):
    parser = configparser.ConfigParser()
    parser.read(path)

    config = parser['config']

    return Config(
        api_id=config['api_id'],
        api_hash=config['api_hash'],
        ozon_channel_id=config['ozon_channel_id'],
        yandex_channel_id=config['yandex_channel_id'],
        post_count=int(config['post_count'])
    )
