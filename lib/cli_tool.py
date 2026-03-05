
#!/usr/bin/env python3
import argparse
from .models import Task, User

# Global dictionary to store users and their tasks
users = {}

def add_task(args):
    # Check if the user exists, if not, create one
    if args.user not in users:
        users[args.user] = User(args.user)
    # Create a new Task with the given title
    task = Task(args.title)
    # Add the task to the user's task list
    users[args.user].add_task(task)
    
def complete_task(args):
    # Look up the user by name
    user = users.get(args.user)
    if not user:
        print(f"❌ User '{args.user}' not found")
        return
    # Look up the task by title
    task = user.get_task_by_title(args.title)
    if task:
        # Mark the task as complete
        task.complete()
    # Print appropriate error messages if not found
    else:
        print(f"❌ Task '{args.title}' not found for user '{args.user}'.")

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    # Subparser for adding tasks
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user", help="Username")
    add_parser.add_argument("title", help="Task title")
    add_parser.set_defaults(func=add_task)

    # Subparser for completing tasks
    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user", help="Username")
    complete_parser.add_argument("title", help="Task title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
