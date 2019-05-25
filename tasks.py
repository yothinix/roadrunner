from halo import Halo
from invoke import task


def echo(command):
    spinner = Halo(text=command, text_color="green", spinner="dots")
    spinner.start()
    return spinner


@task
def black(c):
    command = "python -m black --target-version py36 --line-length 99 ."
    spinner = echo(command)
    c.run(command)
    spinner.stop()


@task
def isort(c):
    command = "python -m isort --apply --line-width 99"
    spinner = echo(command)
    c.run(command)
    spinner.stop()


@task
def flake8(c):
    command = "python -m flake8 --max-line-length=99"
    spinner = echo(command)
    c.run(command)
    spinner.stop()


@task
def pytest(c):
    command = "pytest --color=yes"
    spinner = echo(command)
    c.run(command)
    spinner.stop()


@task(pre=[black, isort, flake8, pytest])
def build(c):
    pass
