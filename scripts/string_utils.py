"""Simple string processing utilities for practice.

Functions:
    normalize_whitespace(text: str) -> str
    word_frequencies(text: str) -> dict[str, int]
    is_palindrome(text: str) -> bool
"""
from __future__ import annotations
from collections import Counter
import re

__all__ = [
    "normalize_whitespace",
    "word_frequencies",
    "is_palindrome",
]

_whitespace_re = re.compile(r"\s+")
_word_re = re.compile(r"[\w']+")


def normalize_whitespace(text: str) -> str:
    """Collapse consecutive whitespace into a single space and strip ends."""
    return _whitespace_re.sub(" ", text).strip()


def word_frequencies(text: str) -> dict[str, int]:
    """Return case-insensitive word frequency dictionary.

    Rules:
    - Case-insensitive
    - Simple token regex including apostrophes
    - Possessive endings like "apple's" or "students'" are normalized by removing a trailing "'s" or single terminal apostrophe.
    """
    raw_words = _word_re.findall(text)
    norm_words: list[str] = []
    for w in raw_words:
        lw = w.lower()
        # strip possessive: dog's -> dog, dogs' -> dogs
        if lw.endswith("'s"):
            lw = lw[:-2]
        elif lw.endswith("'"):
            lw = lw[:-1]
        if lw:
            norm_words.append(lw)
    return dict(Counter(norm_words))


def is_palindrome(text: str) -> bool:
    """Return True if text is a palindrome ignoring case and non-alphanumerics."""
    filtered = ''.join(ch.lower() for ch in text if ch.isalnum())
    return filtered == filtered[::-1]


if __name__ == "__main__":  # simple demo
    sample = "Madam, I'm Adam.  Adam I'm,   madam!"
    print("Normalized:", normalize_whitespace(sample))
    print("Frequencies:", word_frequencies(sample))
    print("Palindrome?", is_palindrome(sample))
