# Employee Access Simulator  

A simple simulation tool for HR/security teams to test employee access requests against room rules (access levels, open/close times, cooldowns).  

---

## Overview  
This project simulates whether employees can access secure rooms in a building.  

- **Input**: JSON list of employee requests (`employees.json`)  
- **Logic**: Room rules (minimum access level, open/close window, cooldown)  
- **Output**: Access Granted or Denied with reasons  

---

## Tech Stack  
- **Backend**: Python 3, Flask  
- **Frontend**: HTML, CSS, JavaScript (with Fetch API)  
- **Data**: JSON file (static input)  

---

## Setup Instructions  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/tahir-A-ai/employee-access-simulator.git
   cd employee-access-simulator
   ```

2. **Switch to the dev branch** (project code lives there)  
   ```bash
   git checkout dev
   ```

3. **Create a virtual environment (recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

4. **Install dependencies**  
   ```bash
   pip install flask
   ```

5. **Run the application**  
   ```bash
   python app.py
   ```

6. **Open in browser**  
   ```
   http://127.0.0.1:5000
   ```

---

## Project Structure (dev branch)  

```
employee-access-simulator/
│── app.py             # Flask entry point
│── rules.py           # Business logic (access checks)
│── employees.json     # Input data (employee requests)
│── templates/
│     └── index.html   # Frontend UI
│── static/
      └── style.css    # Styling
```

---

## Example Input (employees.json)  
```json
[
  { "id": "EMP001", "access_level": 2, "request_time": "09:15", "room": "ServerRoom" },
  { "id": "EMP002", "access_level": 1, "request_time": "09:30", "room": "Vault" }
]
```

---

## Example Output (Simulation Results)  
- EMP001 → Granted: Access granted to ServerRoom  
- EMP002 → Denied: Below required access level  

---

## Branching Policy  
- **main branch** → only `README.md`  
- **dev branch** → full project code  
- At least **5 meaningful commits** with concise messages  

---

## Notes  
- This project is part of the **Innovaxel Fall ’25 Software Engineer Intern hiring assessment**.  
- All code is written for demonstration purposes and can be extended further.  
