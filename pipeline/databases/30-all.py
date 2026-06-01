#!/usr/bin/env python3
"""
Module that provides a function to list all documents in a collection
"""


def list_all(mongo_collection):
    """
    List all documents in a collection

    Args:
        mongo_collection: pymongo collection object
    Returns:
        list: List of all documents in the collection, empty list if none
    """
    documents = list(mongo_collection.find())
    return documents
