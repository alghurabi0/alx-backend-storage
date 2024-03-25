#!/usr/bin/env python3


def update_topics(mongo_collection, name, topics):
    q = {"name": name}
    n = {$set: {"topics": topics}}
    mongo_collection.update_many(q, n)
