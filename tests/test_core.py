import unittest

import analytical


class CoreTests(unittest.TestCase):
    def test_init(self):
        ga = analytical.Provider("googleanalytics", "UA-XXXXXX-Y")

    def test_bad_init(self):
        with self.assertRaises(ValueError):
            analytical.Provider("unknown", "")
