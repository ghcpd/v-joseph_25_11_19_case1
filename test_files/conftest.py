import pytest
from app import app, tasks, archived_tasks


@pytest.fixture(autouse=True)
def clear_state():
    tasks.clear()
    archived_tasks.clear()
    yield
    tasks.clear()
    archived_tasks.clear()


@pytest.fixture()
def client():
    return app.test_client()
