from selenium import webdriver
import pytest


@pytest.fixture
def decrement_href():
    return 'http://127.0.0.1:8000/decrement/'


def test_basic(decrement_href):
    browser = webdriver.Chrome()
    site = "http://127.0.0.1:8000/decrement/"
    browser.get(site)
    counters = browser.find_elements_by_id('counter')
    for counter in counters:
        assert 'Current counter: 4' == counter.text
    Decrement = browser.find_element_by_link_text('Decrement')
    assert Decrement.text == 'Decrement'
    href = Decrement.get_attribute('href')
    assert href == decrement_href
