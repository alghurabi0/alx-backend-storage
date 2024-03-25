#!/usr/bin/env python3
""" insert a docs with python using kwargs """


def insert_school(mongo_collection, **kwargs):
    return mongo_collection.insert(kwargs)
