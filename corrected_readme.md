# Project Management System — Corrected README

## Overview
This small Flask project manages tasks and archived tasks. Each task has a title and an optional color. The web UI shows active tasks and archived tasks.

## Installation
- Linux / macOS
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```
- Windows (PowerShell)
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  ```

## Running the app
- Run with Python directly:
  ```bash
  python app.py
  ```
- The app is available at http://127.0.0.1:5000/

## Endpoints
- GET `/` — Render web UI with lists of active and archived tasks.
- POST `/add` — Add a task via form fields: `title` (required), `color` (optional, defaults to `white`). Returns a redirect to index.
- GET `/delete/<index>` — Delete the task at `index` (0-based). Returns a redirect to index.
- GET `/archive/<index>` — Move the task at `index` to the archived tasks list (0-based). Returns a redirect to index.
- POST `/update_color/<index>` — Update color for the task at `index` with `color` field. Returns a redirect to index.

> Note: `index` is 0-based and reflects the current ordering of tasks in the active list.

## Missing features / Notes
- There is no API to reorder tasks or to restore tasks from the archive by default.
- There is no endpoint to delete a task from the archived list.

## Example curl commands
- Add a task with color:
  ```bash
  curl -X POST -F "title=Task 1" -F "color=red" http://127.0.0.1:5000/add
  ```
- Add a task without color:
  ```bash
  curl -X POST -F "title=Task 2" http://127.0.0.1:5000/add
  ```
- Delete a task by index (0-based):
  ```bash
  curl http://127.0.0.1:5000/delete/0
  ```
- Archive a task by index (0-based):
  ```bash
  curl http://127.0.0.1:5000/archive/0
  ```
- Update color:
  ```bash
  curl -X POST -F "color=blue" http://127.0.0.1:5000/update_color/0
  ```

## Running tests
- Use pytest. Install the dev requirements then run:
  ```bash
  pip install -r requirements.txt
  pip install pytest
  pytest
  ```

## Contributions / Fixes
- If you want to add reorder or restore features, add endpoints for `POST /reorder` or `POST /restore/<index>` and update UI accordingly.
