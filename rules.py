# imports
from datetime import datetime, timedelta

# Room rules
ROOMS = {
    "ServerRoom": {"min_level": 2, "open": "09:00", "close": "11:00", "cooldown": 15},
    "Vault": {"min_level": 3, "open": "09:00", "close": "10:00", "cooldown": 30},
    "R&D Lab": {"min_level": 1, "open": "08:00", "close": "12:00", "cooldown": 10}
}

# Track last access times
last_access = {}

# Check access function
def check_access(emp):
    room = ROOMS[emp["room"]]
    emp_time = datetime.strptime(emp["request_time"], "%H:%M")
    open_time = datetime.strptime(room["open"], "%H:%M")
    close_time = datetime.strptime(room["close"], "%H:%M")

    # Verifying all the three conditions

    # 1. Check access level
    if emp["access_level"] < room["min_level"]:
        return "Denied: Below required access level"

    # 2. Check time window
    if not (open_time <= emp_time <= close_time):
        return "Denied: Room closed at this time"

    # 3. Check cooldown
    last = last_access.get((emp["id"], emp["room"]))
    if last and emp_time < last + timedelta(minutes=room["cooldown"]):
        return "Denied: Cooldown active"

    # Grant access
    last_access[(emp["id"], emp["room"])] = emp_time
    return f"Granted: Access granted to {emp['room']}"
