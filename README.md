# Library Management System

A web-based Library Management System for managing book transactions, member details, and book inventory.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Library Management System is designed to streamline library operations, including book issuance, member management, and book inventory tracking. It provides a user-friendly interface for librarians to manage the library efficiently.

## Features

- **Book Management:** Add, edit, and delete books from the library inventory.
- **Member Management:** Add, edit, and delete member details.
- **Book Issuance:** Issue books to members with return date tracking.
- **Transaction History:** View the history of book transactions.
- **Fine Calculation:** Automated fine calculation for late book returns.
- **Search Functionality:** Search for books or members based on various criteria.

## Requirements

- Python 3.x
- Django (version specified in requirements.txt)
- Other dependencies (specified in requirements.txt)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/faisalepty/library.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser for admin access:

    ```bash
    python manage.py createsuperuser
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the admin panel at http://localhost:8000/admin/ and log in with the superuser credentials.

## Usage

- Access the application at http://localhost:8000/.
- Use the admin panel for administrative tasks.
- Perform book issuances, manage members, and track transactions through the web interface.

