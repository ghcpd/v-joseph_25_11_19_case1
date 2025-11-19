# Project Management System (Corrected Guide)

This Flask mini-app allows you to create simple task cards, archive them, and adjust their colors. The implementation keeps everything in memory, so restarting the server clears the entire board.

## Requirements

- Python 3.11 (or later 3.x)
- `bash` for the helper scripts

## Environment Setup

```bash
./setup.sh
```

The script provisions `.venv/`, ensures `pip` is available inside the environment, and installs the dependencies from `requirements.txt` (Flask + pytest for the automated tests).

## Running the Flask App

```bash
.venv/bin/python app.py
```

Visit `http://127.0.0.1:5000/` to use the HTML UI. Press `Ctrl+C` in the terminal to stop the server.

## API / Feature Reference

All indices are zero-based and match the rendering order on the board.

### 1. Add a Task (with optional color)

```
POST /add
form fields: title (required), color (optional, defaults to "white")
```

Example:

```bash
curl -X POST -F "title=Wireframes" -F "color=#d1f0ff" http://127.0.0.1:5000/add
```

### 2. Delete a Task

```
GET /delete/<index>
```

Example:

```bash
curl http://127.0.0.1:5000/delete/0
```

### 3. Archive a Task

```
GET /archive/<index>
```

Archiving removes the task from the active board and places it into the archived list rendered at the bottom of the page.

### 4. Update an Existing Task's Color

```
POST /update_color/<index>
form fields: color (required)
```

Example:

```bash
curl -X POST -F "color=#ffc857" http://127.0.0.1:5000/update_color/0
```

### 5. Task Ordering

Reordering is **not implemented** in `app.py`. Tasks are displayed strictly in the order they were created, so moving cards around requires editing the code (e.g., by adding drag-and-drop support). This limitation is now documented to avoid confusion.

## Automated Tests

```bash
./run_tests.sh
```

The script reuses `setup.sh` to ensure the environment is ready and then executes the Pytest suite in `test_files/`, which verifies adding, deleting, archiving, and changing task colors.
