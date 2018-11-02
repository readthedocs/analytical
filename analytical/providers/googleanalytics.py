"""
Google Analytics Measurement Protocol provider

https://developers.google.com/analytics/devguides/collection/protocol/v1/
"""
import hashlib
import logging
import uuid

from ..tasks import send_analytics_data
from ..utils import force_bytes
from .base import BaseProvider


log = logging.getLogger(__name__)  # noqa


class Provider(BaseProvider):

    """
    A provider for sending data to Google Analytics using the Measurement Protocol

    https://developers.google.com/analytics/devguides/collection/protocol/v1/devguide
    """

    ANALYTICS_API_URL = "https://www.google-analytics.com/collect"
    DEFAULT_TIMEOUT = 3
    DEFAULT_DATA = {"v": "1"}  # analytics version (always 1)

    def __init__(
        self,
        initial_data,
        timeout=DEFAULT_TIMEOUT,
        fail_silently=True,
        asynchronously=False,
        **kwargs
    ):
        """
        Initialize the Google Analytics provider

        :param str initial_data: for this provider, this should be the property ID (eg. UA-XXXXX-Y)
        :param int timeout: the timeout in seconds when sending
        :param bool fail_silently: whether to fail silently (warnings are logged)
        :param bool asynchronously: whether to send data asynchronously with celery
        """
        super(Provider, self).__init__(initial_data, **kwargs)
        self.timeout = timeout
        self.fail_silently = fail_silently
        self.property_id = initial_data
        self.asynchronously = asynchronously

    def _send(self, params):
        kwargs = {
            "url": self.ANALYTICS_API_URL,
            "data": params,
            "method": "POST",
            "timeout": self.timeout,
            "fail_silently": self.fail_silently,
        }
        if self.asynchronously:
            return send_analytics_data.delay(**kwargs)

        return send_analytics_data.run(**kwargs)

    def pageview(self, params):
        """Tracks a pageview hit with passed ``params``"""
        return self.track_hit("pageview", params)

    def event(self, params):
        """Tracks an event hit with passed ``params``"""
        return self.track_hit("event", params)

    def track_hit(self, hit_type, params):
        """
        Tracks a hit of the specified type with passed ``params``

        See the Google development guide for a complete list of 
        `available params <https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters>`
        """
        data_to_send = {}
        data_to_send.update(self.DEFAULT_DATA)
        data_to_send["tid"] = self.property_id
        data_to_send["t"] = hit_type
        data_to_send.update(params)

        if "cid" not in data_to_send and "uid" not in data_to_send:
            data_to_send["cid"] = generate_client_id()

        return self._send(data_to_send)


def generate_client_id(user_secret=None):
    """
    Generate a Google Analytics client ID (the ``cid`` parameter)

    GA treats users with the same client ID as the same user for analytics purposes.
    This function helps generate a client ID that can be used to track
    new vs. returning visitors without cookies.

    .. code-block:: python

        # Use the User Agent and IP Address
        # The downside to this is if the IP or UA changes, it's considered a new user
        # The upside is it doesn't require anything from a database, cookies or elsewhere
        secret = '{}${}${}'.format('my-secret', ip_address, user_agent)
        client_id = generate_client_id(secret)

        # Use a user ID value from a database or elsewhere
        secret = '{}${}'.format('my-secret', user.id)
        client_id = generate_client_id(secret)

    :param str user_secret: a secret that shouldn't change for a given user.
        If ``None``, treat all pageviews and events as new/unique.
    :returns str: a client ID suitable for using with Google Analytics
    """
    salt = b"analytical-googleanalytics-client"

    hash_id = hashlib.sha256()
    hash_id.update(salt)
    if user_secret:
        hash_id.update(force_bytes(user_secret))
    else:
        hash_id.update(uuid.uuid4().bytes)

    return hash_id.hexdigest()
