# Date and Time Calculator

A web application built using Flask that calculates a new date and time by adding a specified number of hours to a given date and time.

## Features
- Input a date (`DD-MM-YYYY`) and time (`HH:MM:SS`).
- Add a specified number of hours.
- Display the resulting new date and time.

## Project Structure
/date_time_calculator
├── app.py               # Main Flask application file
├── requirements.txt     # List of dependencies
├── Procfile             # Command to run the application
├── templates/           # HTML templates
│   └── index.html       # Main web page
├── static/              # Static files (CSS, JS, images)
└── style.css            # Optional separate CSS file

## Run Locally
1. Clone the repo:  
   `git clone https://github.com/your-username/date-time-calculator.git`  
   `cd date-time-calculator`
2. Create and activate a virtual environment:  
   `python -m venv venv`  
   `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
3. Install dependencies:  
   `pip install -r requirements.txt`
4. Run the app:  
   `python app.py`  
   Visit `http://127.0.0.1:5000`.

## Deployment on Render
1. Push the project to GitHub.
2. On Render, create a new web service, link it to the repo, and configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
3. Access the deployed app via the Render URL.

## Example Usage
1. Input a date (`01-01-2025`), time (`12:30:00`), and hours to add (`5`).
2. Click "Calculate" to see the new date and time.

## Requirements
- Python 3.7+
- Flask, Gunicorn

## License
MIT License

## Author
[Suraj Kumar Verma](https://github.com/your-username)
