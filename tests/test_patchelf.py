import os
import subprocess

from importlib_metadata import files


def which(exe):
    path = os.getenv("PATH")
    for folder in path.split(os.path.pathsep):
        candidate = os.path.join(folder, exe)
        if os.path.exists(candidate) and os.access(candidate, os.X_OK):
            return os.path.abspath(candidate)
    return None


def get_script():
    for file in files("patchelf"):
        if not file.stem == "patchelf":
            continue
        if file.parent.name != "bin":
            continue
        return str(file.locate().resolve(strict=True))
    raise LookupError("Can't find patchelf script")


def test_patchelf_script():
    script = get_script()
    subprocess.check_call([script, "--version"])
    assert script == which("patchelf")
