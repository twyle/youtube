"""This module declares application exceptions."""


class QuotasExceededException(Exception):
    """Raised when you use up all quotas for the day."""
    
class AuthenticationException(Exception):
    """Raised when you use the API without authenticating."""
