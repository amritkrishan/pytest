import pytest
import requests

def pytest_html_report_title(report):
    report.title = "Home Page Fixture"

@pytest.fixture(scope='module')
def url():
     print("----setup----")
     url = ["https://www.google.co.in", "https://www.youtube.com", "https://www.facebook.com"]
     yield url
     print("----teardown----")

def test_get_google_check_status_code_equals_200(url):
     response = requests.get(url[0])
     assert response.status_code == 200

def test_get_youtube_check_status_code_equals_200(url):
     response = requests.get(url[1])
     assert response.status_code == 200

def test_get_fb_check_status_code_equals_200(url):
     response = requests.get(url[2])
     assert response.status_code == 200