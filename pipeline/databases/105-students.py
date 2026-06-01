#!/usr/bin/env python3
"""
Module that provides a function to get top students by average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score

    Args:
        mongo_collection: pymongo collection object
    Returns:
        list: List of students sorted by average score (highest first)
    """
    pipeline = [
        {
            "$addFields": {
                "averageScore": { "$avg": "$topics.score" }
            }
        },
        {
            "$sort": { "averageScore": -1 }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
