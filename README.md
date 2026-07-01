# Student Management and Performance Analytics System

A teacher-centric **Command Line Interface (CLI)** application for managing student records, analyzing academic performance, and visualizing insights using **Python**, **Pandas**, and **Matplotlib**.

---

## Overview

The **Student Management and Performance Analytics System** is a modular Python application designed to help teachers efficiently manage student records, analyze academic performance, and generate meaningful visualizations from student data.

The project follows a clean modular architecture where the user interface is separated from the application's core business logic, making the backend reusable for future desktop or web-based applications.

---

## Features

### Student Management

* Add new student records
* Update existing student information
* Delete student records
* View student dataset

### Dataset Management

* Load dataset
* Process and validate data
* Save changes
* Maintain processed and raw datasets

### Performance Analysis

* Student Records
* Study Hours Analysis
* Attendance Analysis
* Internet Access Analysis
* Extra Activities Analysis
* Subject Performance Analysis
* Average Score Analysis
* Grade Analysis

### Data Visualization

* Pie Charts
* Bar Charts
* Scatter Plots
* Histograms

### Input Validation

* Student ID validation
* Name validation
* Age validation
* Attendance validation
* Study Hours validation
* Subject Score validation
* Internet Access validation
* Extra Activities validation

---

## Project Architecture

The project follows a modular architecture with clear separation of responsibilities.

```text
main.py
│
├── config.py
├── validation.py
├── data_processing.py
├── process.py
├── analysis.py
└── charts.py
```

### Module Responsibilities

| Module               | Responsibility                             |
| -------------------- | ------------------------------------------ |
| `main.py`            | Controls menus and user interaction        |
| `config.py`          | Stores project configuration and constants |
| `validation.py`      | Handles input validation                   |
| `data_processing.py` | Loads, saves, and processes datasets       |
| `process.py`         | Performs student record operations         |
| `analysis.py`        | Generates analytical reports               |
| `charts.py`          | Creates data visualizations                |

---

## Project Structure

```text
Student-Management-and-Analytics-System/
│
├── data/
│   ├── processed/
│   └── raw/
│
├── src/
│   ├── main.py
│   ├── config.py
│   ├── validation.py
│   ├── data_processing.py
│   ├── process.py
│   ├── analysis.py
│   └── charts.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── venv/
```

---

## Technologies Used

| Technology | Purpose                                |
| ---------- | -------------------------------------- |
| Python     | Core programming language              |
| Pandas     | Data loading, processing, and analysis |
| Matplotlib | Data visualization                     |

---

## Installation

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project directory.

```bash
cd Student-Management-and-Analytics-System
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

4. Run the application.

```bash
python src/main.py
```

---

## Example Workflow

```text
Start Application
        │
        ▼
Load Dataset
        │
        ▼
Manage Student Records
        │
        ▼
Perform Analysis
        │
        ▼
Generate Charts
        │
        ▼
Save Dataset
        │
        ▼
Exit
```

---

## Dataset

The application stores student records using CSV files.

The dataset is validated before analysis to ensure consistent and reliable results.

Project data is organized into:

* `data/raw` – Original dataset
* `data/processed` – Processed dataset

---

## Design Principles

* Modular architecture
* Separation of concerns
* Beginner-friendly implementation
* Reusable backend modules
* Maintainable code structure
* Validation-driven data management

---

## Development Tools & AI Assistance

Development Tools
 - Git
 - Visual Studio Code (VS Code)

AI Assistance

 - AI was utilized as a development assistant for syntax clarification, debugging, documentation, and conceptual guidance throughout the development process. The project's software architecture, implementation, business logic, validation, data processing, analytics, and overall development decisions were designed and implemented by the author.

---

## License

This project is intended for educational and portfolio purposes.

---

## Author

**Nikhil M**

BCA (Artificial Intelligence & Machine Learning)

Passionate about building modular Python applications, data analytics tools, and AI/ML projects.
