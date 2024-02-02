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

- **Book Management:** Add, edit, and delete books from the library inventory

🎥
  ![bookCRUD](https://github.com/faisalepty/library/assets/129375971/1319ed69-a328-4de0-b0d4-bec283317682)
- **Member Management:** Add, edit, and delete member details.

🎥
  ![memberCRUD1](https://github.com/faisalepty/library/assets/129375971/6374e36d-0733-417d-a089-78c214016d76)

- **Book Issuance:** Issue books to members with return date tracking.

🎥
![ISSUANCE](https://github.com/faisalepty/library/assets/129375971/a47f4765-1d46-4f82-9f09-bbc48c2da2d9)
 - **Search Functionality:** Search for books or members based on various criteria.

 🎥
   ![searchfuntionality1](https://github.com/faisalepty/library/assets/129375971/05e3f11d-3b3b-4dbb-a16d-ad1c1ac2f295)
- **Transaction History:** View the history of book transactions.

🎥
  ![transactionHIST](https://github.com/faisalepty/library/assets/129375971/71a71b4d-d13b-4d50-9503-358b43b327b5)
- **Fine Calculation:** Automated fine calculation for late book returns.


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

