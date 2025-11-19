#!/bin/bash
set -e
source .venv/bin/activate

echo "Testing Flask Project Management System"

# Start app in background
python app.py &
APP_PID=$!
sleep 2

# Test adding tasks
curl -X POST -F "title=Task 1" -F "color=red" http://127.0.0.1:5000/add
curl -X POST -F "title=Task 2" http://127.0.0.1:5000/add

# Test archive
curl http://127.0.0.1:5000/archive/0

# Test delete
curl http://127.0.0.1:5000/delete/0

# Test update color
curl -X POST -F "color=blue" http://127.0.0.1:5000/update_color/0

kill $APP_PID
echo "All tests executed."