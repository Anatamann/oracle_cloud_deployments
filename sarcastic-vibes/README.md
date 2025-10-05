# Sarcastic Quotes for you

A simple web application that displays a smirking emoji and provides random sarcastic complements at the click of the shuffle button.

## Running the Application

There are two ways to run the application: directly using Python or with Docker.

### Method 1: Running with Python

**Prerequisites:**
- Python 3

1.  **Set up the environment:**
    - Create and activate a virtual environment:
      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```
      *(On Windows, use `.venv\Scripts\activate`)*

    - Install the required packages:
      ```bash
      pip install -r requirements.txt
      ```

2.  **Initialize the database:**
    - If you are running the application for the first time, you need to create the database:
      ```bash
      python init_db.py
      ```

3.  **Run the application:**
    ```bash
    flask run
    ```

4.  **Access the application:**
    - Open your web browser and navigate to `http://127.0.0.1:5000`.

### Method 2: Running with Docker

**Prerequisites:**
- Docker

1.  **Build the Docker image:**
    ```bash
    docker build -t sarcastic-chandler .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 sarcastic-chandler
    ```

3.  **Access the application:**
    - Open your web browser and navigate to `http://localhost:5000`.
