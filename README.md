# Project Management System

## Installation
1. Create virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install Flask
   ```
2. Run the app:
   ```bash
   python app.py
   ```

## Usage
- Add task: `POST /add` with form: `title` only.
- Delete task: `GET /delete/<index>`
- Archive task: `POST /archive/<index>`
- Change color: `POST /change_color/<index>`