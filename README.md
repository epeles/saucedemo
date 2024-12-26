# SauceDemo Automation

## Overview

This repository contains automated tests for the SauceDemo e-commerce web application using Selenium with Python. The tests are written using the Pytest framework and include integration with a CI/CD pipeline and Allure for detailed test reporting.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Continuous Integration](#continuous-integration)
- [Allure Reports](#allure-reports)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/saucedemo.git
    cd saucedemo
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running Tests

To run the tests locally, use the following command:
```sh
pytest tests/main.py --alluredir=allure-results