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


import glob  # noqa: E402

from make_docx import png_size  # noqa: E402

SHOTS = "/root/labs/tools/build/data/shots"


def _ref(numbers):
    if len(numbers) == 1:
        return f"рисунке {numbers[0]}"
    if len(numbers) == 2:
        return f"рисунках {numbers[0]} и {numbers[1]}"
    return f"рисунках {numbers[0]}-{numbers[-1]}"


class Figures:
    """Сквозная нумерация рисунков в отчёте; снимки кода из VS Code лежат в data/shots."""

    def __init__(self):
        self.n = 0

    def add(self, path, caption, width=None):
        self.n += 1
        if width is None:
            width = min(16.5, png_size(path)[0] / 60)
        return ("image", path, width, f"Рисунок {self.n} - {caption}")

    def code(self, key, caption):
        files = sorted(glob.glob(f"{SHOTS}/{key}_*.png"))
        blocks, numbers = [], []
        for i, path in enumerate(files, 1):
            blocks.append(self.add(path, caption + (f" (часть {i})" if len(files) > 1 else "")))
            numbers.append(self.n)
        return blocks, _ref(numbers)
