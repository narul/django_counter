from selenium import webdriver


def test_basic():
    browser = webdriver.Chrome()
    site = "http://127.0.0.1:8000/increment/"
    browser.get(site)
    counter = browser.find_element_by_id('counter')
    assert 'Current counter: 5' == counter.text
