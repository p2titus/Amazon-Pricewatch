"""
this will only work for amazon at the moment
"""
import requests


def purchase(link: str) -> bool:
    r = requests.get(link)
    pass
