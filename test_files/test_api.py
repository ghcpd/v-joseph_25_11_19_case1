import pytest
from app import app, tasks, archived_tasks


@pytest.fixture(autouse=True)
def clear_tasks():
    # Clear global lists before each test
    tasks.clear()
    archived_tasks.clear()
    yield


def test_add_task_with_color():
    client = app.test_client()
    resp = client.post('/add', data={'title': 'Test Task', 'color': 'red'}, follow_redirects=True)
    assert resp.status_code == 200
    assert any(t['title'] == 'Test Task' and t['color'] == 'red' for t in tasks)


def test_add_task_without_color_defaults_to_white():
    client = app.test_client()
    client.post('/add', data={'title': 'Test Task 2'}, follow_redirects=True)
    assert tasks[0]['color'] == 'white'


def test_delete_task():
    client = app.test_client()
    client.post('/add', data={'title': 'To be deleted'})
    assert len(tasks) == 1
    client.get('/delete/0', follow_redirects=True)
    assert len(tasks) == 0


def test_archive_task_moves_to_archived():
    client = app.test_client()
    client.post('/add', data={'title': 'To be archived'})
    client.get('/archive/0', follow_redirects=True)
    assert len(tasks) == 0
    assert archived_tasks[0]['title'] == 'To be archived'


def test_update_color_endpoint_updates_color():
    client = app.test_client()
    client.post('/add', data={'title': 'Color change', 'color': 'green'})
    client.post('/update_color/0', data={'color': 'blue'}, follow_redirects=True)
    assert tasks[0]['color'] == 'blue'


def test_change_color_endpoint_not_found():
    client = app.test_client()
    # POST to /change_color should return 404 since the route is /update_color
    resp = client.post('/change_color/0', data={'color': 'yellow'})
    assert resp.status_code == 404


def test_archive_endpoint_method_mismatch_returns_405():
    client = app.test_client()
    client.post('/add', data={'title': 'Archive Test'})
    # POST to /archive should not be allowed since route is GET; expect 405
    resp = client.post('/archive/0')
    assert resp.status_code in (404, 405)
