# Project Management System

A Flask-based project management system for managing tasks with color labeling and archiving capabilities.

## Features

- ✅ Add tasks with optional color labels
- ✅ Delete tasks
- ✅ Archive tasks for later reference
- ✅ Update task colors
- ✅ View archived tasks
- ✅ Simple web interface

## Installation

### Prerequisites
- Python 3.7 or higher

### Setup Instructions

#### For Windows (PowerShell)
```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

#### For Windows (CMD)
```cmd
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt
```

#### For Linux/macOS
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Alternative: Using setup script
```bash
bash setup.sh
```

## Running the Application

1. Ensure your virtual environment is activated
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. Open your browser and navigate to: `http://127.0.0.1:5000/`

## API Documentation

### Available Endpoints

#### 1. View All Tasks
- **URL**: `/`
- **Method**: `GET`
- **Description**: Displays the main page with all active tasks and archived tasks
- **Response**: HTML page with task list

#### 2. Add a New Task
- **URL**: `/add`
- **Method**: `POST`
- **Description**: Creates a new task with optional color
- **Form Parameters**:
  - `title` (required): The title/description of the task
  - `color` (optional): Color for the task background (default: 'white')
- **Example**:
  ```bash
  curl -X POST http://127.0.0.1:5000/add \
    -d "title=Complete documentation" \
    -d "color=lightblue"
  ```
- **Valid Colors**: Any valid CSS color name (e.g., 'red', 'blue', 'lightgreen') or hex code (e.g., '#FF5733')

#### 3. Delete a Task
- **URL**: `/delete/<index>`
- **Method**: `GET`
- **Description**: Permanently deletes a task at the specified index
- **Parameters**:
  - `index` (required): Zero-based index of the task to delete
- **Example**:
  ```bash
  curl http://127.0.0.1:5000/delete/0
  ```
- **Note**: If the index is invalid, the operation is silently ignored

#### 4. Archive a Task
- **URL**: `/archive/<index>`
- **Method**: `GET`
- **Description**: Moves a task from active list to archived list
- **Parameters**:
  - `index` (required): Zero-based index of the task to archive
- **Example**:
  ```bash
  curl http://127.0.0.1:5000/archive/1
  ```
- **Note**: 
  - Archived tasks are displayed in a separate "Archived Tasks" section
  - Currently, archived tasks cannot be unarchived
  - If the index is invalid, the operation is silently ignored

#### 5. Update Task Color
- **URL**: `/update_color/<index>`
- **Method**: `POST`
- **Description**: Changes the background color of an existing task
- **Parameters**:
  - `index` (required): Zero-based index of the task to update
- **Form Parameters**:
  - `color` (required): New color value for the task
- **Example**:
  ```bash
  curl -X POST http://127.0.0.1:5000/update_color/0 \
    -d "color=yellow"
  ```
- **Note**: If the index is invalid, the operation is silently ignored

## Usage Examples

### Web Interface Usage

1. **Adding a Task**:
   - Enter task title in the "Title" field
   - (Optional) Enter a color name in the "Color" field
   - Click "Add" button
   - Task appears in the task list with the specified color background

2. **Deleting a Task**:
   - Click the "Delete" link next to any task
   - Task is permanently removed from the list

3. **Archiving a Task**:
   - Click the "Archive" link next to any task
   - Task moves to the "Archived Tasks" section at the bottom of the page

4. **Viewing Archived Tasks**:
   - Scroll down to the "Archived Tasks" section
   - All archived tasks are listed there (without delete/archive options)

### Command-Line Examples (using curl)

#### Add a task with color
```bash
curl -X POST http://127.0.0.1:5000/add -d "title=Review pull requests" -d "color=lightyellow"
```

#### Add a task without color (defaults to white)
```bash
curl -X POST http://127.0.0.1:5000/add -d "title=Write unit tests"
```

#### Delete the first task (index 0)
```bash
curl http://127.0.0.1:5000/delete/0
```

#### Archive the second task (index 1)
```bash
curl http://127.0.0.1:5000/archive/1
```

#### Change color of first task
```bash
curl -X POST http://127.0.0.1:5000/update_color/0 -d "color=lightgreen"
```

## Data Structure

### Task Object
Each task is stored as a dictionary with the following structure:
```python
{
    'title': 'Task description',
    'color': 'background color'
}
```

### Important Notes
- Tasks are identified by their **zero-based index** in the list (not by unique IDs)
- When a task is deleted or archived, all subsequent tasks shift down by one index
- No persistent storage - all data is lost when the application stops

## Task Order
- Tasks are displayed in chronological order (first added at the top)
- Currently, there is no functionality to reorder tasks
- Task order changes only when tasks are deleted or archived

## Limitations and Known Behaviors

1. **No Persistence**: Tasks and archived tasks are stored in memory and lost on restart
2. **No Input Validation**: 
   - Empty titles are accepted (creates a task with `None` title)
   - Any string is accepted as a color value
3. **Silent Failures**: Invalid indices are ignored without error messages
4. **No Undo**: Deleted tasks cannot be recovered
5. **Archive is One-Way**: Archived tasks cannot be moved back to active tasks
6. **No User Management**: Despite the project description mentioning users, there is no user authentication or user-specific task lists

## Testing

### Run All Tests
```bash
bash run_tests.sh
```

### Run Specific Test Files
```bash
# Test main application functionality
python -m pytest test_files/test_app.py -v

# Test integration workflows
python -m pytest test_files/test_integration.py -v
```

### Run Tests with Coverage
```bash
python -m pytest test_files/ --cov=app --cov-report=html
```

## Troubleshooting

### Virtual Environment Activation Issues
- **Windows PowerShell**: If you get an execution policy error, run:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
- **Linux/macOS**: If `source` command fails, ensure you're using bash or zsh

### Port Already in Use
If port 5000 is already in use, modify `app.py` and change:
```python
app.run(debug=True, port=5001)  # Use different port
```

### Flask Not Found
Ensure virtual environment is activated and Flask is installed:
```bash
pip install Flask>=2.3
```

## Project Structure
```
.
├── app.py                    # Main Flask application
├── templates/
│   └── index.html           # Web interface template
├── test_files/
│   ├── test_app.py          # Unit tests for endpoints
│   └── test_integration.py  # Integration tests
├── requirements.txt         # Python dependencies
├── setup.sh                # Setup script for Linux/macOS
├── run_tests.sh            # Test execution script
├── README.md               # This file
└── .venv/                  # Virtual environment (created during setup)
```

## Contributing

When contributing, please:
1. Follow the existing code style
2. Add tests for new features
3. Update documentation to reflect changes
4. Test on multiple platforms if possible

## License

This is a demonstration project for educational purposes.
