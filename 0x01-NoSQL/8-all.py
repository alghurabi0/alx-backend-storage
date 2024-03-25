#!/usr/bin/env python3
""" list all docs in a collection with python """


def list_all(mongo_collection):
    """ list all docs in a coll with python """
    docs = mongo_collection.find()
    if docs.count() == 0:
        return []
    return docs
