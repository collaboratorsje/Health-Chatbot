# Health-Chatbot
Principles of Data Science (CS5530) - Project Repository 

Team Members: Seth Emery, Shreyan Reddy Gangwar, Lavanya Ghanathey, Ankitha Srirama Reddy

 
### Requirements
- Python 3.x

### Windows

Pull Repository

    git clone https://github.com/collaboratorsje/Health-Chatbot.git

Virtual Environment Setup

    python -m venv venv 

Activate Virtual Environment (Must do every time you launch, you'll see (venv) in your terminal) 

    .\venv\Scripts\Activate.ps1 # If using Powershell

or 

    .\venv\Scripts\activate.bat # If using Command Prompt

Install Requirements

    python -m pip install -r .\requirements.txt

Launch with 

    python app.py 
    or 
    flask run --port 5050 (You may have to set the flask environment variable for this)
Open in browser at http://127.0.0.1:5050

### Mac
Note: The Mac setup is similar to the Windows setup, but with slight command differences.

Virtual Environment Setup

    python3 -m virtualenv venv 

Activate Virtual Environment (Must do every time you launch, you'll see (venv) in your terminal) 

    source ./venv/bin/activate

Install Requirements

    python3 -m pip install -r ./requirements.txt

Launch with 

    python3 app.py 
    or 
    flask run --port 5050 (You may have to set the flask environment variable for this)
Open in browser at http://127.0.0.1:5050