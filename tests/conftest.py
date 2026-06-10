import copy

import pytest
from fastapi.testclient import TestClient
from src import app as app_module

original_activities = copy.deepcopy(app_module.activities)


def reset_activities():
    app_module.activities = copy.deepcopy(original_activities)


@pytest.fixture
def client():
    reset_activities()
    client = TestClient(app_module.app)
    yield client
    reset_activities()
