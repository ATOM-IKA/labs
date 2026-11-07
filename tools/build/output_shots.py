"""Снимки вывода программ в терминале VS Code (виртуальный дисплей :98 размером 1280x2000, терминал развёрнут на всю панель).

Команда и ввод набираются в терминале, весь вывод снимается одним кадром и нарезается на части по строкам.
"""
import os
import subprocess
import sys
import time

DISPLAY = ":98"
OUT = "/root/labs/tools/build/data/shots"
TEXTS = "/root/labs/tools/build/data/outputs"
ROW_H, FIRST_ROW = 23, 77
MAX_ROWS = 32

LAB42 = ["1", "2", "Вторник", "3", "Вторник", "2", "Физика", "2", "Вторник", "3", "Среда", "1", "Химия", "0"]
LAB6 = ["abc", "4", "5", "3", "2", "2", ""]

TARGETS = {
    "lab6_out": ("/root/labs/labs/lab6", "python3 room_area.py", LAB6),
    "lab7_out": ("/root/labs/labs/lab7", "python3 lab07.py", None),
    "lab7_flaw": ("/root/labs/tools/build/data/lab7", "flawfinder --minlevel=1 demo.c", None),
    "lab36_out": ("/root/labs/labs/lab36", "python3 lab36.py", None),
    "lab38_39_out": ("/root/labs/labs/lab38_39", "python3 lab38_39.py", None),
    "lab40_out": ("/root/labs/labs/lab40_41", "python3 main.py", None),
    "lab42_43_out": ("/root/labs/labs/lab42_43", "python3 lab42_43.py", LAB42),
    "pr2_out": ("/root/labs/labs/op09/pr2", "python3 halstead.py", None),
    "pr3_out": ("/root/labs/labs/op09/pr3", "python3 primes.py", None),
}

env = dict(os.environ, DISPLAY=DISPLAY)


def xdo(*args):
    subprocess.run(["xdotool", *args], env=env, check=True)


def type_line(text, delay=25):
    xdo("type", "--delay", str(delay), "--clearmodifiers", text)
    xdo("key", "Return")


def session_text(folder, command, inputs):
    """Как будет выглядеть сеанс на экране: приглашения с введёнными значениями."""
    shell = f"{os.path.basename(folder)}$ {command}"
    if inputs is None:
        done = subprocess.run(command.split(), cwd=folder, capture_output=True, text=True)
        body = (done.stdout + done.stderr).rstrip("\n").split("\n")
    else:
        driver = (
            "import builtins, runpy\n"
            f"answers = iter({inputs!r})\n"
            "def fake_input(prompt=''):\n"
            "    value = next(answers)\n"
            "    print(prompt + value)\n"
            "    return value\n"
            "builtins.input = fake_input\n"
            f"runpy.run_path({command.split()[1]!r}, run_name='__main__')\n"
        )
        done = subprocess.run([sys.executable, "-c", driver], cwd=folder, capture_output=True, text=True)
        body = (done.stdout + done.stderr).rstrip("\n").split("\n")
    return [shell] + body + [f"{os.path.basename(folder)}$ "]


def shoot(key):
    folder, command, inputs = TARGETS[key]
    lines = session_text(folder, command, inputs)
    rows = len(lines)
    longest = max(len(line) for line in lines)
    width = max(520, min(1280, int(48 + 25 + longest * 9.7 + 60)))

    xdo("mousemove", "800", "500", "click", "1")
    type_line(f"cd {folder} && clear")
    time.sleep(1)
    if key == "pr3_out":
        os.makedirs(TEXTS, exist_ok=True)
        type_line(f"python3() {{ command python3 \"$@\" | tee {TEXTS}/pr3.txt; }}")
        type_line("clear")
        time.sleep(0.5)
    type_line(command)
    if inputs is not None:
        time.sleep(1.5)
        for answer in inputs:
            if answer:
                type_line(answer, delay=40)
            else:
                xdo("key", "Return")
            time.sleep(0.6)
    time.sleep(25 if key == "pr3_out" else 3)

    raw = f"{OUT}/_raw.png"
    subprocess.run(["import", "-window", "root", raw], env=env, check=True)
    chunks = (rows + MAX_ROWS - 1) // MAX_ROWS
    size = (rows + chunks - 1) // chunks
    for i in range(chunks):
        shown = min(size, rows - i * size)
        top = 34 if i == 0 else FIRST_ROW + i * size * ROW_H - 2
        bottom = FIRST_ROW + (i * size + shown) * ROW_H + 6
        name = f"{OUT}/{key}_{i + 1}.png"
        subprocess.run(["convert", raw, "-crop", f"{width}x{bottom - top}+0+{top}", "+repage", name], check=True)
    os.remove(raw)
    if key == "pr3_out":
        type_line("unset -f python3")
    type_line("clear")
    return chunks, rows


if __name__ == "__main__":
    for key in (sys.argv[1:] or list(TARGETS)):
        print(key, shoot(key), flush=True)
