from flask import url_for
import pytest
from selenium.webdriver.common.by import By
from pytest_selenium import selenium



def test_index(selenium, live_server):

    selenium.get(url_for("index", _external=True))

    heading = selenium.find_element(By.TAG_NAME, "h1")

    assert "Hello world!" in heading.text