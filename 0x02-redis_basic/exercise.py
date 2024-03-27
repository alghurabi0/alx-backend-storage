#!/usr/bin/env python3
""" creating a Cache class for practicing redis"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """Cache class using redis"""
    def __init__(self):
        """Cache instance initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key using uuid,
        sotres the input data in Redis using the
        random key and return the key (string)"""
        key = uuid.uuid4()
        self._redis.set(str(key), data)
        return str(key)

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """The Callabale will be useed to convert
        the data back to the desired format"""
        if fn is not None:
            res = self._redis.get(key)
            return fn(res)
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """ get type str"""
        res = self.get(key)
        return res.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ get type int"""
        return self.get(key, int)
