#!/usr/bin/python3
""" creating a Cache class for practicing redis"""
import redis
import uuid


class Cache:
    def __init__(self):
        """Cache instance initialization"""
        self._redis = redis.Redis()
        # flushdb to flush the instance
        self._redis.flushdb

    def store(self, data: any) -> str:
        """Generates a random key using uuid,
        sotres the input data in Redis using the
        random key and return the key (string)"""
        key = uuid.uuid4()
        self._redis.set(str(key), data)
        return str(key)
