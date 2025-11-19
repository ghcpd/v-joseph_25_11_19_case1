from app import tasks


def test_delete_task_valid_index(client):
    client.post('/add', data={'title': 'Task1'})
    client.post('/add', data={'title': 'Task2'})

    resp = client.get('/delete/0')
    assert resp.status_code == 302
    assert tasks == [{'title': 'Task2', 'color': 'white'}]


def test_delete_task_invalid_index_noop(client):
    client.post('/add', data={'title': 'Task1'})
    resp = client.get('/delete/10')
    assert resp.status_code == 302
    assert tasks == [{'title': 'Task1', 'color': 'white'}]
