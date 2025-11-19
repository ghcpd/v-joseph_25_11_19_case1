# Project Management System (Flask)

## 🚀 Quick Start

1. **Create & activate a virtualenv**
   ```bash
   python -m venv .venv
   # macOS/Linux
   source .venv/bin/activate
   # Windows PowerShell
   .venv\Scripts\Activate.ps1
   # Windows CMD
   .venv\Scripts\activate
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**
   ```bash
   python app.py
   ```
   Visit http://127.0.0.1:5000/

> **Note:** Data is stored in-memory (`tasks`, `archived_tasks`). Restarting the app clears all tasks.

---

## 📚 API & UI Usage

### 1) List tasks and archived tasks
- **Endpoint:** `GET /`
- **Behavior:** Renders HTML showing current tasks (with colors) and archived tasks.

### 2) Add a task
- **Endpoint:** `POST /add`
- **Form fields:**
  - `title` (required)
  - `color` (optional, defaults to `white`)
- **HTML form:** Available on `/`
- **cURL example:**
  ```bash
  curl -X POST http://127.0.0.1:5000/add \
       -d "title=My Task" \
       -d "color=red" \
       -i -L
  ```

### 3) Delete a task
- **Endpoint:** `GET /delete/<index>`
- **Indexing:** 0-based (use the order shown on the page)
- **cURL example:**
  ```bash
  curl -X GET http://127.0.0.1:5000/delete/0 -i -L
  ```

### 4) Archive a task
- **Endpoint:** `GET /archive/<index>`
- **Indexing:** 0-based
- **Effect:** Moves the task from active list to archived list.
- **cURL example:**
  ```bash
  curl -X GET http://127.0.0.1:5000/archive/0 -i -L
  ```

### 5) Update task color
- **Endpoint:** `POST /update_color/<index>`
- **Form fields:** `color`
- **cURL example:**
  ```bash
  curl -X POST http://127.0.0.1:5000/update_color/0 \
       -d "color=blue" \
       -i -L
  ```

---

## 🔍 Notes & Limitations
- **Ordering:** There is **no reorder endpoint**; tasks render in insertion order.
- **Validation:** Invalid indices are ignored (redirects back to `/`).
- **Persistence:** No database; in-memory only.

---

## 🧪 Testing
- Run all tests:
  ```bash
  ./run_tests.sh         # macOS/Linux
  bash run_tests.sh      # Windows (Git Bash)
  ```
- Tests live in `test_files/` and use `pytest`.

---

## 📦 Project Structure
```
app.py
corrected_readme.md
README.md
requirements.txt
run_tests.sh
setup.sh
templates/
    index.html
test_files/
```
