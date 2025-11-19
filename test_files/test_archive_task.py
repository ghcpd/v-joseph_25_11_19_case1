from app import tasks, archived_tasks


def test_archive_task_moves_to_archived(client):
    client.post('/add', data={'title': 'Task1'})
    client.post('/add', data={'title': 'Task2'})

    resp = client.get('/archive/1')
    assert resp.status_code == 302
    assert tasks == [{'title': 'Task1', 'color': 'white'}]
    assert archived_tasks == [{'title': 'Task2', 'color': 'white'}]


def test_archive_invalid_index_noop(client):
    client.post('/add', data={'title': 'Task1'})
    resp = client.get('/archive/5')
    assert resp.status_code == 302
    assert tasks == [{'title': 'Task1', 'color': 'white'}]
    assert archived_tasks == []
