# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:30:04 2026

@author: AA
"""
class Task:
    def __init__(self, id, title, assignee, priority, status):
        self.id = id
        self.title = title
        self.assignee = assignee
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Assignee: {self.assignee}, Priority: {self.priority}, Status: {self.status}"
