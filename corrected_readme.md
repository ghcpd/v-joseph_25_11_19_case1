# Project Management System (Corrected Documentation)

## Installation
1. Create virtual environment and activate (Windows PowerShell):
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1  # PowerShell
   # or
   .venv\Scripts\activate      # cmd.exe
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Running the app
```powershell
python app.py
```
The app runs on http://127.0.0.1:5000 by default.

## API Endpoints (server-side)
- Add task: POST /add
  - Form fields: `title` (required), `color` (optional, default: 'white')
  - Example (curl):
    ```bash
    curl -X POST -F "title=Fix bug" -F "color=lightblue" http://127.0.0.1:5000/add
    ```
- Delete task: GET /delete/<index>
  - Example: `GET /delete/0`
- Archive task: GET /archive/<index>
  - Example: `GET /archive/1`
- Update color: POST /update_color/<index>
  - Body: form field `color` e.g. `color=red`
  - Example (curl):
    ```bash
    curl -X POST -F "color=red" http://127.0.0.1:5000/update_color/0
    ```

## Notes and limitations
- This app uses simple in-memory lists and does NOT persist tasks across restarts.
- There is no built-in API for re-ordering tasks or restoring archived tasks; those would require additional routes and UI changes.

## Using in the UI
- The template provides an Add Task form that accepts `title` and `color` (optional).
- Archived tasks are displayed below the active list; there is currently no "restore" button.

## Development
- To add routes for reordering or restore, implement endpoints and update `templates/index.html` and `app.py`.
