"""Мелкие помощники для сборки отчётов: чтение листингов и запуск программ с перехватом вывода."""
import subprocess
import sys


def read(path):
    with open(path, encoding="utf8") as f:
        return f.read().rstrip("\n")


def run(args, cwd, stdin=None):
    """Запускает программу и возвращает её вывод (stdout и stderr вместе)."""
    done = subprocess.run([sys.executable] + args, cwd=cwd, input=stdin, capture_output=True, text=True)
    return (done.stdout + done.stderr).rstrip("\n")


def unittest_summary(cwd):
    """Две последние строки вывода unittest: число тестов и итог."""
    out = run(["-m", "unittest"], cwd)
    lines = [line for line in out.splitlines() if line.strip()]
    return "\n".join(lines[-2:])
