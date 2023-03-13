#!/usr/bin/python3
"""init."""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

__all__ = ['storage']

