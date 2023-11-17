# Store Monitoring System

The Store Monitoring System is a Django-based web application that provides monitoring and reporting features for store activities. It includes functionality for generating reports, tracking store uptime, and exporting data in CSV format.

## Table of Contents

- [Store Monitoring System](#store-monitoring-system)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
    - [Configuration](#configuration)
    - [Triggering a Report](#triggering-a-report)
    - [Checking Report Status](#checking-report-status)
  - [Setup Script](#setup-script)

## Getting Started

### Prerequisites

Make sure you have the following installed on your system:

- [Python](https://www.python.org/) (version 3.6 or higher)
- [Django](https://www.djangoproject.com/) (install using `pip install Django`)
- [Django Rest Framework](https://www.django-rest-framework.org/) (install using `pip install djangorestframework`)
- [Other dependencies as specified in requirements.txt]

### Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:jrijul1201/Store-Monitoring-System.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Store-Monitoring-System
   ```

3. Set up your `.env` file with the following format:

   ```env
   DEBUG=False
   SECRET_KEY=""
   DATABASE_URL=sqlite:///db.sqlite3
   STORES_CSV_PATH="/path/to/your/Stores.csv"
   BUSINESS_HOURS_CSV_PATH="/path/to/your/BusinessHours.csv"
   TIMEZONES_CSV_PATH="/path/to/your/TimeZones.csv"
   ```

4. Run the setup script:

   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

4. Run the app:

   ```bash
   python manage.py runserver --noreload
   ```

The application should now be accessible at [http://localhost:8000/](http://localhost:8000/).

## Usage

### Configuration

Before running the application, make sure to configure your `.env` file with the appropriate settings. Adjust the values according to your environment.

### Triggering a Report

To trigger the generation of a new report, make a POST request to the following endpoint:

```http
POST /trigger-report/
```

Example using [curl](https://curl.se/):

```bash
curl -X POST http://localhost:8000/trigger-report/
```

### Checking Report Status

To check the status of a report and retrieve its associated CSV path, make a GET request to the following endpoint:

```http
GET /get-report/{report_id}/
```

Replace `{report_id}` with the actual ID of the report.

Example using [curl](https://curl.se/):

```bash
curl http://localhost:8000/get-report/1/
```

## Setup Script

For easier setup, you can use the provided `setup.sh` script. This script creates a virtual environment, installs project requirements, and applies database migrations.

```bash
chmod +x setup.sh
./setup.sh
```

Adjust the script as needed for your environment.


Make sure to replace `/path/to/your/` with the actual paths to your CSV files in the `.env` file. Additionally, update any other paths or configurations based on your project structure.