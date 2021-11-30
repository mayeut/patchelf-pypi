# -*- coding: utf-8 -*-
import os
import subprocess
import sys


def which(exe):
    path = os.getenv("PATH")
    for folder in path.split(os.path.pathsep):
        candidate = os.path.join(folder, exe)
        if os.path.exists(candidate) and os.access(candidate, os.X_OK):
            return os.path.abspath(candidate)
    return None


def test_patchelf_entrypoint():
    subprocess.check_call(["patchelf", "--version"])
    assert os.path.join(sys.prefix, "bin", "patchelf") == which("patchelf")


def test_patchelf_package():
    subprocess.check_call([sys.executable, "-m", "patchelf", "--version"])
