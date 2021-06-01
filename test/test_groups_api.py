"""
    DataMeta

    DataMeta  # noqa: E501

    The version of the OpenAPI document: 0.27.0
    Contact: leon.kuchenbecker@uni-tuebingen.de
    Generated by: https://openapi-generator.tech
"""


import unittest

import datameta_client_lib
from datameta_client_lib.api.groups_api import GroupsApi  # noqa: E501


class TestGroupsApi(unittest.TestCase):
    """GroupsApi unit test stubs"""

    def setUp(self):
        self.api = GroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_group_name(self):
        """Test case for change_group_name

        Change the name of a group.  # noqa: E501
        """
        pass

    def test_get_group_submissions(self):
        """Test case for get_group_submissions

        Get A List of All Submissions of A Group.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
