from invoke import task


@task
def black(c):
    command = "python -m black --target-version py36 --line-length 99 ."
    print(command)
    c.run(command)


@task
def isort(c):
    command = "python -m isort --apply --line-width 99"
    print(command)
    c.run(command)


@task
def flake8(c):
    command = "python -m flake8 --max-line-length=99"
    print(command)
    c.run(command)


@task
def pytest(c):
    command = "pytest"
    print(command)
    c.run(command)


@task(pre=[black, isort, flake8, pytest])
def test(c):
    print("---finishing build---")
