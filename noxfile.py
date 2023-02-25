from pathlib import Path

import nox

nox.options.sessions = ["lint", "build", "tests"]

built = ""


@nox.session
def build(session: nox.Session) -> str:
    """
    Make an SDist and a wheel. Only runs once.
    """
    global built
    if not built:
        session.log(
            "The files produced locally by this job are not intended to be "
            "redistributable"
        )
        session.install("build")
        tmpdir = session.create_tmp()
        session.run("python", "-m", "build", "--outdir", tmpdir)
        (wheel_path,) = Path(tmpdir).glob("*.whl")
        (sdist_path,) = Path(tmpdir).glob("*.tar.gz")
        Path("dist").mkdir(exist_ok=True)
        wheel_path.rename(f"dist/{wheel_path.name}")
        sdist_path.rename(f"dist/{sdist_path.name}")
        built = wheel_path.name
    return built


@nox.session
def lint(session: nox.Session) -> str:
    """
    Run linters on the codebase.
    """
    session.install("pre-commit")
    session.run("pre-commit", "run", "-a")


@nox.session
def tests(session: nox.Session) -> str:
    """
    Run the tests.
    """
    wheel = build(session)
    session.install(f"./dist/{wheel}[test]")
    session.run("pytest", *session.posargs)
