"""Celery tasks for executing asynchronously"""
import logging

import requests
from celery import shared_task


DEFAULT_TIMEOUT = 3  # seconds

log = logging.getLogger(__name__)  # noqa


@shared_task
def send_analytics_data(
    url,
    params=None,
    data=None,
    method="POST",
    timeout=DEFAULT_TIMEOUT,
    fail_silently=True,
):  # pylint: disable=too-many-arguments
    """
    A celery task for sending data to analytics providers asynchronously

    :param str url: the URL to send to
    :param obj params: a dict of query params to send (for GET requests)
    :param obj data: a dict of data to send (for POST, PUT requests)
    :param str method: the HTTP method (eg. GET, POST, PUT, etc.)
    :param int timeout: timeout for the request in seconds
    :param bool fail_silently: whether the task should raise an exception or fail silently
    :returns bool: ``True`` on success or ``False`` on error
    :raises: only if ``fail_silently`` is ``False`` and an error occurs
    """
    log.debug("Sending data to analytics (%s), %s", url, params)
    kwargs = {
        "url": url,
        "method": method,
        "data": data,
        "params": params,
        "timeout": timeout,
    }
    try:
        resp = requests.request(**kwargs)
    except requests.Timeout:
        log.warning("Timeout sending data")
        if not fail_silently:
            raise
        return False

    if resp and not resp.ok:
        log.warning("Unknown error sending analytics data")
        if not fail_silently:
            resp.raise_for_status()
        return False
    return True
