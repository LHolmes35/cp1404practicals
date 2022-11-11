"""
Prac 07 - Project Class
"""

import datetime


class Project:

    def __init__(self, name, start_date, priority, cost_estimate, percentage_complete):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y').date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percentage_complete = percentage_complete

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.percentage_complete}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.percentage_complete == 100
