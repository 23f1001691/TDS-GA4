# uvicorn main:app --reload --port 9000

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
import re

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pre-defined functions 
def get_ticket_status(ticket_id: int):
    return f"Status of ticket {ticket_id}"

def schedule_meeting(date: str, time: str, meeting_room: str):
    return f"Meeting scheduled on {date} at {time} in {meeting_room}"

def get_expense_balance(employee_id: int):
    return f"Expense balance for employee {employee_id}"

def calculate_performance_bonus(employee_id: int, current_year: int):
    return f"Performance bonus for employee {employee_id} for {current_year}"

def report_office_issue(issue_code: int, department: str):
    return f"Issue {issue_code} reported for {department}"


@app.get("/execute")
def execute(q: str = Query(...)):
    q = q.strip()

    # Ticket status
    ticket_match = re.search(r"ticket (\d+)", q, re.IGNORECASE)
    if ticket_match:
        ticket_id = int(ticket_match.group(1))
        return {
            "name": "get_ticket_status",
            "arguments": json.dumps({"ticket_id": ticket_id})  # ✅ stringified JSON
        }

    # Meeting scheduling
    meeting_match = re.search(
        r"on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)\.", q, re.IGNORECASE
    )
    if meeting_match:
        date, time, room = meeting_match.groups()
        return {
            "name": "schedule_meeting",
            "arguments": json.dumps({"date": date, "time": time, "meeting_room": room})
        }

    # Expense balance
    expense_match = re.search(r"employee (\d+).*expense balance", q, re.IGNORECASE)
    if expense_match:
        employee_id = int(expense_match.group(1))
        return {
            "name": "get_expense_balance",
            "arguments": json.dumps({"employee_id": employee_id})
        }

    # Performance bonus
    bonus_match = re.search(
        r"performance bonus.*employee (\d+).*?(\d{4})", q, re.IGNORECASE
    )
    if bonus_match:
        employee_id, year = bonus_match.groups()
        return {
            "name": "calculate_performance_bonus",
            "arguments": json.dumps({"employee_id": int(employee_id), "current_year": int(year)})
        }

    # Office issue reporting
    issue_match = re.search(
        r"issue (\d+).*department (\w+)", q, re.IGNORECASE
    )
    if issue_match:
        issue_code, department = issue_match.groups()
        return {
            "name": "report_office_issue",
            "arguments": json.dumps({"issue_code": int(issue_code), "department": department})
        }

    # Always return valid JSON
    return {"error": "Query did not match any known function"}
