Google Analytics
================

The Google Analytics provider sends data to Google using the `Measurement Protocol`_.

.. _Measurement Protocol: https://developers.google.com/analytics/devguides/collection/protocol/v1/


Tracking pageviews
------------------

.. code-block:: python

    import analytical
    from analytical.providers.googleanalytics import generate_client_id

    ga = analytical.Provider('googleanalytics', 'UA-XXXXXX-Y')
    ga.pageview({
        "ua": "user-agent",             # User agent
        "uip": "12.34.56.78",           # User IP address
        "dl": "https://example.com",    # URL of the pageview (required)
        "dt": "page title",             # Title of the page
    })

For the complete list of parameters, see the reference_.

.. _reference: https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters


Tracking events
---------------

.. code-block:: python

    import analytical

    ga = analytical.Provider('googleanalytics', 'UA-XXXXXX-Y')
    ga.event({
        "ua": "user-agent",
        "uip": "12.34.56.78",
        "ec": "event-category",         # Event category (required)
        "ea": "event-action",           # Event action (required)
        "el": "event-label",            # Event label (optional)
        "ev": 0,                        # Event value (optional, integer)
    })

See the `event parameter reference`_ for more details.

.. _event parameter reference: https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters#events


Utility functions
-----------------

.. autofunction:: analytical.providers.googleanalytics.generate_client_id
