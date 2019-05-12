from invoke import task


def echo(command):
    print("--------------")
    print(command)
    print("--------------")


@task
def black(c):
    command = "python -m black --target-version py36 --line-length 99 ."
    echo(command)
    c.run(command)


@task
def isort(c):
    command = "python -m isort --apply --line-width 99"
    echo(command)
    c.run(command)


@task
def flake8(c):
    command = "python -m flake8 --max-line-length=99"
    echo(command)
    c.run(command)


@task
def pytest(c):
    command = "pytest"
    echo(command)
    c.run(command)


@task(pre=[black, isort, flake8, pytest])
def build(c):
    print("---finishing build---")
