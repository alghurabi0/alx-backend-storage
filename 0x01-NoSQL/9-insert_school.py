#!/usr/bin/env python3
""" insert a docs with python using kwargs """


def insert_school(mongo_collection, **kwargs):
    """ documentation same as above """
    return mongo_collection.insert(kwargs)
