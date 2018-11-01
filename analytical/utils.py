"""Helpful utilities for sending data to analytics that aren't specific to a backend"""
import six
from user_agents import parse

try:
    # Python 3.3+ only
    import ipaddress
except ImportError:
    from .vendor import ipaddress


def force_bytes(s):
    """Force to a bytes type (not unicode)"""
    if issubclass(type(s), six.binary_type):
        return s
    if issubclass(type(s), six.text_type):
        return s.encode("utf-8")

    return ValueError(s)


def force_text(s, encoding="utf-8", errors="strict"):
    """Force to a string type (not bytes)"""
    if issubclass(type(s), six.text_type):
        return s
    if issubclass(type(s), six.binary_type):
        return six.text_type(s, encoding, errors)

    return ValueError(s)


def anonymize_ip_address(ip_address):
    """
    Anonymizes an IP address by zeroing the last 2 bytes

    Zeroing the last two bytes is sufficient to make a user reasonably anonymous
    while still allowing decent geolocation accuracy.
    One byte is insufficient for the DoNotTrack standard.

    .. code-block:: python

        anonymize_ip_address('12.34.56.78')  # '12.34.0.0'

    :param str ip_address: the IP address of the user
    :returns str: an anonymized IP address
    """
    ip_mask = int("0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000", 16)

    try:
        ip_obj = ipaddress.ip_address(force_text(ip_address))
    except ValueError:
        return None

    anonymized_ip = ipaddress.ip_address(int(ip_obj) & ip_mask)
    return anonymized_ip.compressed


def anonymize_user_agent(user_agent):
    """
    Anonymizes rare user agents

    Currently, this function is pretty naive.
    Only if the browser or OS family are not recognized, it is considered "rare".

    :param str user_agent: the browser user agent for the user
    :returns str: the same user agent or the string "Rare user agent" if ``user_agent`` is "rare"
    """
    parsed_ua = parse(user_agent)
    if parsed_ua.browser.family == "Other" or parsed_ua.os.family == "Other":
        return "Rare user agent"

    return user_agent
