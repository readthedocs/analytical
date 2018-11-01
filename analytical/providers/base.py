"""A base class for other providers"""


class BaseProvider(object):

    """A base class for other providers"""

    def __init__(
        self, initial_data, fail_silently=True, **kwargs
    ):  # pylint: disable=unused-argument
        """Handle initialization for the provider"""
        self.fail_silently = fail_silently

    def pageview(self, params):
        raise NotImplementedError

    def event(self, params):
        raise NotImplementedError
