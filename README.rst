.. This file is included automatically by docs/index

Analytical - Server Side Analytics
==================================

Analytical is a Python library for sending pageviews and events to analytics platforms
like Google Analytics except from Python rather than JavaScript so it can be done server side.
This has a number of advantages such as working regardless of whether clients block analytics scripts,
privacy sensitive information can be anonymized or removed before sending,
and it allows sending data only known by the server.


Feature support
---------------

* Convenient utilities for anonymizing sensitive information like IP addresses
* Pluggable provider backends for different analytics platforms (currently just Google)

Supports Python 2.7, Python 3.5+, and PyPy.


Example
-------

.. code-block:: python

    import analytical

    analytical.Provider('googleanalytics', 'UA-XXXXXXX-1')
    analytical.pageview({
        'dl': 'https://example.com',
        'dt': 'My Page Title',
        'ua': 'user-agent',             # User agent
        'uip: '12.34.56.78',            # User IP address
    })


Resources
---------

* GitHub: https://github.com/rtfd/analytical
* Documentation: https://analytical.readthedocs.io
* IRC: #readthedocs on freenode
