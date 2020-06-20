from selenium import webdriver


def test_basic():
    browser = webdriver.Chrome()
    site = "http://127.0.0.1:8000"
    browser.get(site)
    counters = browser.find_elements_by_id('counter')
    for counter in counters:
        assert 'Current counter: 4' == counter.text
