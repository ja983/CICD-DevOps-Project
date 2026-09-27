# CI/CD DevOps Project

A Python application with an automated CI pipeline built using GitHub Actions — created as part of the DecodeLabs DevOps Internship (Project 3), building on the Git fundamentals from Project 2.

## What this project demonstrates
- A GitHub Actions workflow that automatically builds and tests code on every push and Pull Request
- Unit testing with `pytest`
- Input validation and error handling in application logic
- A full branch → commit → push → Pull Request → CI check → merge cycle

## Installation

```bash
git clone https://github.com/your-username/CICD-DevOps-Project.git
cd CICD-DevOps-Project
pip install -r requirements.txt
```

## Usage

```bash
python src/app.py
```

## Running Tests

```bash
python -m pytest tests/ -v
```

## CI Pipeline

Every push or Pull Request targeting `main` automatically triggers the workflow defined in [`.github/workflows/ci.yml`](.github/workflows/ci.yml), which:
1. Checks out the code
2. Sets up Python
3. Installs dependencies
4. Runs the test suite

Check the **Actions** tab on GitHub to see pipeline runs and results.

## Project Structure

CICD-DevOps-Project/
├── .github/
│ └── workflows/
│ └── ci.yml # CI pipeline definition
├── src/
│ ├── init.py
│ └── app.py # Core application logic
├── tests/
│ ├── init.py
│ └── test_app.py # Unit tests
├── pytest.ini
├── requirements.txt
└── README.md


## Skills Practiced
CI/CD concepts, GitHub Actions, automated testing, YAML pipeline configuration, quality gates, branch/PR-based development.
