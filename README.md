# Task Manager

A command-line task management application built in Python to practice
object-oriented design, persistent data storage, and event-driven programming.

## Features

- Create, remove, and complete tasks
- Store task descriptions and due dates
- Track completed, remaining, and failed tasks
- Save application state between sessions using JSON
- Maintain task history
- Custom event system for task creation, completion, and removal

## Architecture

The application is separated into several components:

- `Task` — represents individual tasks and their state
- `TaskManager` — manages tasks and application statistics
- `EventManager` — implements an event-driven publish/subscribe system
- Main program — handles user commands and persistent storage

## Technologies

- Python
- JSON
- pathlib
- Object-Oriented Programming
- Event-driven programming

## Running the Program

1. Clone or download the repository.
2. Make sure Python is installed.
3. Run the main Python file:

python main.py

## Commands

- `add` / `a` — Add a task
- `remove` / `r` — Remove a task
- `complete` / `c` — Complete a task
- `list` / `l` — List tasks
- `stats` / `s` — Display task statistics
- `quit` / `q` — Save and exit

## What I Learned

This project helped me practice structuring a program across multiple classes
and modules rather than writing all application logic in one file. I also
implemented a custom event system and JSON serialization so application state
can persist between sessions.
