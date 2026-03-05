
import subprocess
import sys
import os

def run_cli_command(command):
    """Helper to run CLI command and capture output using current Python interpreter"""
    return subprocess.run([sys.executable] + command[1:], capture_output=True, text=True)


def test_add_task():
    result = run_cli_command([
        sys.executable, "-m", "lib.cli_tool", "add-task", "Alice", "Submit report"
    ])
    assert "📌 Task 'Submit report' added to Alice." in result.stdout


def test_complete_task_with_script(tmp_path):
    """Runs everything in one subprocess so state is shared."""

    project_root = os.getcwd().replace("\\", "/")
    script_path = tmp_path / "script.py"

    script_content = f"""
import sys
sys.path.insert(0, "{project_root}")

from lib.models import Task, User

users = {{}}
user = User("Bob")
users["Bob"] = user
task = Task("Finish lab")
user.add_task(task)
task.complete()
"""

    script_path.write_text(script_content)

    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True
    )

    assert "✅ Task 'Finish lab' completed." in result.stdout