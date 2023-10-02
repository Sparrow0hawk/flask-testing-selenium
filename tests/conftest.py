import sys
import multiprocessing

import pytest
from flask_testing_selenium import create_app

@pytest.fixture(scope="session", autouse=True)
def configure_live_server_fixture() -> None:
    if sys.platform == "darwin":
        multiprocessing.set_start_method("fork")

@pytest.fixture(scope="session")
def app():
    return create_app()

