#!/usr/bin/env python3
""" return list of docs for a query """


def schools_by_topic(mongo_collection, topic):
    """ return list of docs for a query """
    docs = mongo_collection.find({"topics":topic})
    return docs
