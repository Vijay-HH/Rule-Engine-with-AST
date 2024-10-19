# Rule Engine with AST

## Overview

This project is a 3-tier rule engine application that evaluates user eligibility based on various attributes such as age, department, salary, experience, etc. It uses an Abstract Syntax Tree (AST) to represent conditional rules and provides a user interface for dynamic creation and modification of rules.

### Key Features
- **AST-based rule creation**: Dynamically create, combine, and evaluate rules using an Abstract Syntax Tree.
- **Simple UI**: Web interface built using HTML/CSS with modern, sleek design elements.
- **REST API**: Create and evaluate rules using a Flask-based API.
- **MySQL Database**: Store rules and related metadata in a MySQL database.
- **Dockerized setup**: Containerized application with Docker and Docker Compose for easy deployment.

---

## Prerequisites

### Required Software:
1. **Docker**: Make sure Docker and Docker Compose are installed. You can download Docker from [here](https://www.docker.com/products/docker-desktop).
2. **Postman**: To test the APIs, download Postman from [here](https://www.postman.com/downloads/).

### Dependencies:
The application requires the following Python libraries, which will be installed inside the Docker container:

- Flask
- Flask-SQLAlchemy
- PyMySQL
- SQLAlchemy

These dependencies are listed in the `requirements.txt` file.

---

## Installation Instructions

Follow these steps to set up and run the application using Docker.

### 1. Clone the Repository

First, clone the repository from your version control system:

```bash
git clone https://github.com/your-username/rule-engine-ast.git
cd rule-engine-ast
