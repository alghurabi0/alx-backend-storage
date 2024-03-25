#!/usr/bin/env python3
""" change value of a doc or docs """


def update_topics(mongo_collection, name, topics):
    """ change value of a doc of docs """
    q = {"name": name}
    n = {$set: {"topics": topics}}
    mongo_collection.update_many(q, n)
