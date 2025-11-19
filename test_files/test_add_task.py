from app import tasks


def test_add_task_with_color(client):
    resp = client.post('/add', data={'title': 'Task A', 'color': 'red'})
    assert resp.status_code == 302
    assert tasks == [{'title': 'Task A', 'color': 'red'}]


def test_add_task_without_color_defaults_white(client):
    resp = client.post('/add', data={'title': 'Task B'})
    assert resp.status_code == 302
    assert tasks == [{'title': 'Task B', 'color': 'white'}]
