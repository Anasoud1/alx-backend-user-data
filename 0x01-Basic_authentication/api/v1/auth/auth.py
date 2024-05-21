#!/usr/bin/env python3
""" Auth class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Define class Auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False - path"""
        if path:
            return False
        return path

    def authorization_header(self, request=None) -> str:
        """returns None - request"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request"""
        return request
