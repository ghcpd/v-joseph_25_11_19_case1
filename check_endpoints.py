import requests

endpoints = [
    ('POST', 'http://127.0.0.1:5000/change_color/0', {'color':'yellow'}),
    ('POST', 'http://127.0.0.1:5000/archive/0', {}),
    ('GET', 'http://127.0.0.1:5000/archive/0', {}),
]

for method, url, data in endpoints:
    try:
        if method == 'POST':
            r = requests.post(url, data=data, allow_redirects=False)
        else:
            r = requests.get(url, allow_redirects=False)
        print(f"{method} {url} -> {r.status_code}")
    except Exception as e:
        print(f"{method} {url} -> error: {e}")
