# Task: Flask Project Management System Documentation Verification

You are provided with a Flask-based project management system library. The project is designed to manage tasks, users, and project boards.  

Your job is to verify that the `README.md` documentation is accurate and up-to-date. Specifically, check the following **sub-types of documentation defects**:

1. **Missing docs** – Missing instructions for major features such as task archiving or color labeling.
2. **Outdated docs** – Example commands that do not match the current API or Flask routes.
3. **Incorrect docs** – Wrong parameter names, value ranges, or return values.

Your tasks:

- Set up a Python `.venv` environment, It already installed the flask.
- Follow all instructions in `README.md` to run the Flask app, add/delete tasks, move tasks to archive, and adjust task color and order.
- Identify any mismatch between documentation and actual implementation.
- Generate a `corrected_readme.md` with accurate instructions and working examples.
- Output all discovered defects to `defects.txt` with error traces and descriptions.

## Expected Deliverables

1. `defects.txt` – Detailed list of all documentation defects found (at least 5).
2. `corrected_readme.md` – Fixed version of the README with working instructions.
3. `requirements.txt` – Libraries required for the Flask project.
4. `setup.sh` – Bash script to set up the environment.
5. `test_files/` – Python test files to verify each feature.
6. `run_tests.sh` – Bash script to run all test cases.
