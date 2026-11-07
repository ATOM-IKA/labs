import subprocess
import sys

sys.path.insert(0, "/root/labs/tools")
from make_docx import build  # noqa: E402,F401


def read(path):
    with open(path, encoding="utf8") as f:
        return f.read().rstrip("\n")


def run(path, stdin=None, timeout=600):
    """Запускает программу из её папки и возвращает вывод."""
    folder, name = path.rsplit("/", 1)
    done = subprocess.run([sys.executable, name], cwd=folder, input=stdin, capture_output=True, text=True, timeout=timeout)
    return (done.stdout + done.stderr).rstrip("\n")


def echo_run(path, answers):
    """Запуск программы с вводом: введённые ответы выводятся вместе с приглашением, как на экране."""
    folder, name = path.rsplit("/", 1)
    driver = (
        "import builtins, runpy\n"
        f"answers = iter({list(answers)!r})\n"
        "def fake_input(prompt=''):\n"
        "    value = next(answers)\n"
        "    print(prompt + value)\n"
        "    return value\n"
        "builtins.input = fake_input\n"
        f"runpy.run_path({name!r}, run_name='__main__')\n"
    )
    done = subprocess.run([sys.executable, "-c", driver], cwd=folder, capture_output=True, text=True)
    return (done.stdout + done.stderr).rstrip("\n")
