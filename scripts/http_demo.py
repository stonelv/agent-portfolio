"""Simple network request demo using requests.

Fetches JSON placeholder TODO item and prints selected fields.
"""
from __future__ import annotations # This import from the __future__ module allows the use of type annotations in a way that is compatible with future versions of Python. It enables postponed evaluation of annotations, meaning that the annotations are stored as string literals and not evaluated until necessary. This can help avoid issues with forward references and improve performance in some cases.
import requests

API_URL = "https://jsonplaceholder.typicode.com/todos/3"


def fetch_todo() -> dict:
    resp = requests.get(API_URL, timeout=10)
    resp.raise_for_status()
    return resp.json()


def main():
    todo = fetch_todo()
    print("Fetched TODO:")
    print(f" id: {todo['id']}")
    print(f" title: {todo['title']}")
    print(f" completed: {todo['completed']}")


if __name__ == "__main__":
    main()
