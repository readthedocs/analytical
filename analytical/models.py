"""Core objects and methods for the analytical package"""
from .providers import googleanalytics


PROVIDER_MAPPING = {"googleanalytics": googleanalytics.Provider}


class Provider(object):
    def __init__(self, provider_name, provider_data, **kwargs):
        """
        Initialize an analytics provider

        :param str provider_name: the name of the provider (eg. ``googleanalytics``)
        :param obj provider_data: required data passed directly to the provider's constructor
        :param obj kwargs: optional parameters passed to the provider's constructor
        """
        if provider_name not in PROVIDER_MAPPING:
            raise ValueError("Unknown provider {}".format(provider_name))

        self._provider = PROVIDER_MAPPING[provider_name](provider_data, **kwargs)

    def pageview(self, data):
        self._provider.pageview(data)

    def event(self, data):
        self._provider.event(data)
