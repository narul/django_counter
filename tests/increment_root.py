from selenium import webdriver
import pytest


@pytest.fixture
def increment_href():
    return 'http://127.0.0.1:8000/increment/'


def test_basic(increment_href):
    browser = webdriver.Chrome()
    site = "http://127.0.0.1:8000/increment/"
    browser.get(site)
    counters = browser.find_elements_by_id('counter')
    for counter in counters:
        assert 'Current counter: 5' == counter.text
    Increment = browser.find_element_by_link_text('Increment')
    assert Increment.text == 'Increment'
    href = Increment.get_attribute('href')
    assert href == increment_href
