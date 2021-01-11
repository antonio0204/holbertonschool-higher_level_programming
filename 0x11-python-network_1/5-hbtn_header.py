#!/usr/bin/python3
"""
sends a request to the URL
"""
import sys
import requests as rq


if __name__ == "__main__":
    r = rq.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
