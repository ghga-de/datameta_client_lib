"""
    DataMeta

    DataMeta  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: leon.kuchenbecker@uni-tuebingen.de
    Generated by: https://openapi-generator.tech
"""


import unittest

import datameta_client_lib
from datameta_client_lib.api.settings_api import SettingsApi  # noqa: E501


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    def setUp(self):
        self.api = SettingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_app_settings(self):
        """Test case for app_settings

        GET all AppSettings  # noqa: E501
        """
        pass

    def test_update_app_settings(self):
        """Test case for update_app_settings

        Update a specific appsetting. This is an administrative Endpoint that is not accessible for regular users.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
