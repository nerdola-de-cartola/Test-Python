# Prerequisites

Install python  
```sudo apt install python3.10.13```

Install sqlite  
```sudo apt install sqlite```

Install pipenv  
```pip install --user pipenv```

# Initialization

Install dependencies    
```pipenv install```

Initialize database  
```python database/init.py```

# Run

Run in develop mode  
```pipenv run flask --app app run```

Open browser  
```firefox localhost:5000```