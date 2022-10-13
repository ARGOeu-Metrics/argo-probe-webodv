import json
import unittest
from unittest import mock

import requests
from argo_probe_webodv.exceptions import CriticalException, WarningException
from argo_probe_webodv.response import Analyse


class MockResponse:
    def __init__(self, data, status_code):
        self.status_code = status_code
        self.data = data

    def raise_for_status(self):
        if not str(self.status_code).startswith("2"):
            raise requests.exceptions.RequestException(
                "Something has gone wrong"
            )

    def json(self):
        return self.data


def mock_response_ok(*args, **kwargs):
    return MockResponse(
        {
            "export_success": True,
            "output_file_url": "https://some.mock-url.com/download/file.zip"
        }, 200
    )


def mock_response_with_exception(*args, **kwargs):
    return MockResponse(None, 500)


def mock_response_unsuccessful_export(*args, **kwargs):
    return MockResponse(
        {
            "export_success": False,
            "output_file_url": "https://some.mock-url.com/download/file.zip"
        }, 200
    )


class ResponseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.analysis = Analyse(
            url="https://some.mock-url.com/api/test",
            data={"key1": "value", "key2": "value"}
        )

    @mock.patch("requests.post")
    def test_analysis(self, mock_post):
        mock_post.side_effect = mock_response_ok
        self.analysis.analyse()

        mock_post.assert_called_once_with(
            "https://some.mock-url.com/api/test",
            data=json.dumps({"key1": "value", "key2": "value"}),
            headers={"Content-Type": "application/json"}
        )

    @mock.patch("requests.post")
    def test_analysis_with_request_exception(self, mock_post):
        mock_post.side_effect = mock_response_with_exception
        with self.assertRaises(CriticalException) as context:
            self.analysis.analyse()

        self.assertEqual(
            context.exception.__str__(), "Something has gone wrong"
        )

    @mock.patch("requests.post")
    def test_analysis_with_unsuccessful_export(self, mock_post):
        mock_post.side_effect = mock_response_unsuccessful_export
        with self.assertRaises(WarningException) as context:
            self.analysis.analyse()

        self.assertEqual(context.exception.__str__(), "Export not successful")
