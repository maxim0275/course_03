from linecache import cache

from config.settings import CACHE_ENABLED
from message.models import Message


def get_messages_from_cache():
    """ Получает данные из кеша. Если нужны данных нет в кеше, то сообщения берутся из базы данных"""
    if not CACHE_ENABLED:
        return Message.objects.all()
    key = "message_list"
    messages = cache.get(key)
    if messages is not None:
        return messages
    products = Message.objects.all()
    cache.set(key, products)
    return products
