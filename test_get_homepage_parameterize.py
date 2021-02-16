import pytest
import requests

def pytest_html_report_title(report):
    report.title = "Home Page Parameterize"

def setup_module(module):
     print("----setup----")

def teardown_module(module):
    print("----teardown----")

urls = ["https://www.google.co.in", "https://www.youtube.com", "https://www.facebook.com"]
@pytest.mark.parametrize('url', urls)
def test_get_google_check_status_code_equals_200(url):
     response = requests.get(url)
     assert response.status_code == 200

