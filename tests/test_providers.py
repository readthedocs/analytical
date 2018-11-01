import unittest

from analytical.providers import googleanalytics


class GoogleAnalyticsTests(unittest.TestCase):
    def setUp(self):
        self.property_id = "UA-XXXXX-Y"
        self.ga = googleanalytics.Provider(self.property_id)

        def fake_send(params):
            return params

        # Monkeypatch this fake send so we can trigger pageviews and events without sending
        self.ga._send = fake_send

    def test_send_event(self):
        params = {
            "ua": "user-agent",
            "uip": "12.34.56.78",
            "ec": "event-category",
            "ea": "event-action",
            "el": "event-label",
            "ev": "event-value",
        }
        result = self.ga.event(params)

        expected = {"v": "1", "tid": self.property_id, "t": "event"}
        expected.update(params)
        self.assertEqual(result, expected)

    def test_send_pageview(self):
        params = {
            "ua": "user-agent",
            "uip": "12.34.56.78",
            "dl": "https://example.com",
            "dt": "page title",
        }
        result = self.ga.pageview(params)

        expected = {"v": "1", "tid": self.property_id, "t": "pageview"}
        expected.update(params)
        self.assertEqual(result, expected)

    def test_generate_client_id(self):
        # The same secret should get the same client_id
        secret = "my-secret$1"
        client1 = googleanalytics.generate_client_id(secret)
        client2 = googleanalytics.generate_client_id(secret)
        self.assertEqual(client1, client2)

        # A null secret should always generate different client IDs
        secret = None
        client1 = googleanalytics.generate_client_id(secret)
        client2 = googleanalytics.generate_client_id(secret)
        self.assertNotEqual(client1, client2)
