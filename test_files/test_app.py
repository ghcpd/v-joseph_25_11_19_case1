import pytest
from app import app, tasks, archived_tasks

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Reset the in-memory lists before each test
    tasks.clear()
    archived_tasks.clear()
    yield

def test_add_task(client):
    res = client.post('/add', data={'title': 'Task1', 'color': 'yellow'})
    assert res.status_code == 302
    assert len(tasks) == 1
    assert tasks[0]['title'] == 'Task1'
    assert tasks[0]['color'] == 'yellow'

def test_delete_task(client):
    tasks.append({'title':'a','color':'white'})
    res = client.get('/delete/0')
    assert res.status_code == 302
    assert len(tasks) == 0

def test_archive_task(client):
    tasks.append({'title':'a','color':'white'})
    res = client.get('/archive/0')
    assert res.status_code == 302
    assert len(tasks) == 0
    assert len(archived_tasks) == 1

def test_update_color(client):
    tasks.append({'title':'x','color':'white'})
    res = client.post('/update_color/0', data={'color':'green'})
    assert res.status_code == 302
    assert tasks[0]['color'] == 'green'

@pytest.fixture
def client():
    with app.test_client() as c:
        yield c
