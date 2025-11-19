from app import tasks


def test_update_color_valid_index(client):
    client.post('/add', data={'title': 'Task1', 'color': 'red'})
    resp = client.post('/update_color/0', data={'color': 'blue'})
    assert resp.status_code == 302
    assert tasks == [{'title': 'Task1', 'color': 'blue'}]


def test_update_color_invalid_index_noop(client):
    client.post('/add', data={'title': 'Task1', 'color': 'red'})
    resp = client.post('/update_color/5', data={'color': 'green'})
    assert resp.status_code == 302
    assert tasks == [{'title': 'Task1', 'color': 'red'}]
