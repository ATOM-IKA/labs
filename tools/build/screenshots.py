"""Снимки кода в VS Code (запускается в виртуальном дисплее :98, окно 1280x1000, боковая панель скрыта).

Файл открывается в редакторе и листается кусками по 36 строк, каждый кусок сохраняется как отдельный png.
"""
import os
import subprocess
import sys
import time

DISPLAY = ":98"
VSC = "/tmp/claude-0/-root-labs/d06b09d6-39b9-4938-825c-92c2e1945a06/scratchpad/vsc"
OUT = "/root/labs/tools/build/data/shots"
LINES = 35
TOP, LINE_H = 62, 25

TARGETS = {
    "lab6": "/root/labs/labs/lab6/room_area.py",
    "lab7_py": "/root/labs/labs/lab7/lab07.py",
    "lab7_c": "/root/labs/tools/build/data/lab7/demo.c",
    "lab8_server": "/root/labs/labs/lab8/server.py",
    "lab36": "/root/labs/labs/lab36/lab36.py",
    "lab38_39": "/root/labs/labs/lab38_39/lab38_39.py",
    "lab40_function": "/root/labs/labs/lab40_41/function.py",
    "lab40_derivative": "/root/labs/labs/lab40_41/derivative.py",
    "lab40_logarithm": "/root/labs/labs/lab40_41/logarithm.py",
    "lab40_natural": "/root/labs/labs/lab40_41/natural_logarithm.py",
    "lab40_main": "/root/labs/labs/lab40_41/main.py",
    "lab42_43": "/root/labs/labs/lab42_43/lab42_43.py",
    "pr2_stats": "/root/labs/labs/op09/pr2/stats.py",
    "pr2_halstead": "/root/labs/labs/op09/pr2/halstead.py",
    "pr3_primes": "/root/labs/labs/op09/pr3/primes.py",
}

env = dict(os.environ, DISPLAY=DISPLAY)


def xdo(*args):
    subprocess.run(["xdotool", *args], env=env, check=True)


def open_file(path):
    clean = {"HOME": "/root", "PATH": "/usr/bin:/bin", "DISPLAY": DISPLAY, "LANG": "C.UTF-8"}
    subprocess.run(["/usr/share/code/bin/code", "-r", "--no-sandbox", "--user-data-dir", f"{VSC}/ud", "--extensions-dir", f"{VSC}/ext", path],
                   env=clean, capture_output=True)


def shoot(key, path):
    xdo("key", "ctrl+k")
    xdo("key", "ctrl+w")
    time.sleep(0.5)
    open_file(path)
    time.sleep(3)
    xdo("mousemove", "700", "500", "click", "1")
    xdo("key", "ctrl+Home")
    time.sleep(0.5)
    text = open(path, encoding="utf8").read().split("\n")
    count = len(text) - 1 if text[-1] == "" else len(text)
    longest = max(len(line.replace("\t", "    ")) for line in text)
    width = min(1280, int(132 + longest * 10.25 + 60))
    chunks = (count + LINES - 1) // LINES
    size = (count + chunks - 1) // chunks
    for i in range(chunks):
        if i:
            xdo("key", "--repeat", str(size), "--delay", "15", "ctrl+Down")
            time.sleep(0.6)
        shown = min(size, count - i * size)
        bottom = min(960, TOP + shown * LINE_H + 3)
        raw = f"{OUT}/_raw.png"
        subprocess.run(["import", "-window", "root", raw], env=env, check=True)
        name = f"{OUT}/{key}_{i + 1}.png"
        subprocess.run(["convert", raw, "-crop", f"{width}x{bottom - 34}+0+34", "+repage", name], check=True)
    os.remove(f"{OUT}/_raw.png")
    return chunks


if __name__ == "__main__":
    keys = sys.argv[1:] or list(TARGETS)
    for key in keys:
        print(key, shoot(key, TARGETS[key]), flush=True)
