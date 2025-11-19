import pytest

from app import app, archived_tasks, tasks


@pytest.fixture(autouse=True)
def reset_state():
    tasks.clear()
    archived_tasks.clear()
    yield
    tasks.clear()
    archived_tasks.clear()


@pytest.fixture
def client():
    return app.test_client()


def test_add_task_with_explicit_color(client):
    response = client.post("/add", data={"title": "Scoped task", "color": "green"}, follow_redirects=True)
    assert response.status_code == 200
    assert tasks[-1] == {"title": "Scoped task", "color": "green"}


def test_add_task_defaults_to_white(client):
    client.post("/add", data={"title": "Untinted"}, follow_redirects=True)
    assert tasks[-1]["color"] == "white"


def test_delete_task_removes_correct_index(client):
    client.post("/add", data={"title": "First"}, follow_redirects=True)
    client.post("/add", data={"title": "Second"}, follow_redirects=True)
    response = client.get("/delete/0", follow_redirects=True)
    assert response.status_code == 200
    assert len(tasks) == 1 and tasks[0]["title"] == "Second"


def test_archive_task_moves_entry_into_archive_list(client):
    client.post("/add", data={"title": "Archive me"}, follow_redirects=True)
    response = client.get("/archive/0", follow_redirects=True)
    assert response.status_code == 200
    assert len(tasks) == 0
    assert archived_tasks[-1]["title"] == "Archive me"


def test_update_color_endpoint_changes_existing_task_color(client):
    client.post("/add", data={"title": "Palette"}, follow_redirects=True)
    response = client.post("/update_color/0", data={"color": "#FF00FF"}, follow_redirects=True)
    assert response.status_code == 200
    assert tasks[0]["color"] == "#FF00FF"
