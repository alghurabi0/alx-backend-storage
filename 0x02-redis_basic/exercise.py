#!/usr/bin/env python3
""" creating a Cache class for practicing redis"""
import redis
import uuid
from typing import Union


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
