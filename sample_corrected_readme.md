# Project Management System — Flask

A simple Flask web app to manage tasks with optional color labeling and archived tasks. Tasks are stored in-memory and do not persist across restarts.

---

## 🚀 Installation

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Windows (CMD)

```cmd
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

---

## 🏃 Running the App

```bash
python app.py
```

Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)

> Note: Tasks are stored in memory. Restarting the app clears all tasks.

---

## 📌 Features & API

### 1. View Tasks

* **Endpoint:** `GET /`
* **Description:** Displays active tasks and archived tasks in the web UI.

### 2. Add Task

* **Endpoint:** `POST /add`
* **Form Fields:**

  * `title` (required)
  * `color` (optional, defaults to `'white'`)
* **Example (cURL):**

```bash
curl -X POST -F "title=My Task" -F "color=red" http://127.0.0.1:5000/add
```

### 3. Delete Task

* **Endpoint:** `GET /delete/<index>`
* **Indexing:** 0-based
* **Example (cURL):**

```bash
curl http://127.0.0.1:5000/delete/0
```

### 4. Archive Task

* **Endpoint:** `GET /archive/<index>`
* **Indexing:** 0-based
* **Example (cURL):**

```bash
curl http://127.0.0.1:5000/archive/0
```

### 5. Update Task Color

* **Endpoint:** `POST /update_color/<index>`
* **Form Field:** `color`
* **Example (cURL):**

```bash
curl -X POST -F "color=blue" http://127.0.0.1:5000/update_color/0
```

---

## ⚠️ Notes & Limitations

* No persistent database; tasks are in-memory only.
* No endpoints for reordering tasks or restoring archived tasks.
* Indices are 0-based.
* Invalid indices are ignored silently.

---

## 🧪 Testing

* Install pytest:

```bash
pip install pytest
```

* Run tests:

```bash
pytest test_files/
```

---

## 📂 Project Structure

```
app.py
README.md
requirements.txt
templates/
    index.html
test_files/
```
