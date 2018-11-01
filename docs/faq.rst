Frequently Asked Questions
==========================

Why track events on the server rather than with JavaScript?
    One big advantage is that privacy sensitive information such as IP addresses
    can be anonymized before they are sent to Google or other providers.
    This also allows tracking events that are only known to the server
    such as sales data or server side errors.

If I anonymize IP addresses, won't I lose precision in location data?
    Anonymizing IP addresses will definitely lose precision for IP geolocation.
    However, by zeroing the last 2 bytes as this library does,
    IP geolocation should still work to a major city or metro area.

How is this different from other packages like pyga_, django-analytical_, etc.?
    Libraries like django-analytical ease the creation of JavaScript tracking tags
    and don't do server side analytics like this library.
    Pyga uses the old ``gajs`` Google Analytics tracking rather than the more modern,
    documented, and supported `measurement protocol`_.

.. _pyga: https://github.com/kra3/py-ga-mob
.. _django-analytical: https://github.com/jcassee/django-analytical
.. _measurement protocol: https://developers.google.com/analytics/devguides/collection/protocol/v1/
