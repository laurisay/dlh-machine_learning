#!/usr/bin/env python3
"""
Module that provides stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def log_stats():
    """
    Display statistics about Nginx logs including top 10 IPs
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({ "method": method })
        print(f"\tmethod {method}: {count}")

    # Status check (method=GET and path=/status)
    status_check = collection.count_documents({ "method": "GET", "path": "/status" })
    print(f"{status_check} status check")

    # Top 10 IPs
    print("IPs:")
    pipeline = [
        { "$group": { "_id": "$ip", "count": { "$sum": 1 } } },
        { "$sort": { "count": -1 } },
        { "$limit": 10 }
    ]
    top_ips = list(collection.aggregate(pipeline))
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
