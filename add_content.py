import argparse
import re
import sys

from getpass import getpass
from sqlalchemy.orm import Session
from backend.app.db import eng
from backend.app.models.resource import Resource
from backend.app.models.user import User
from backend.app.passwords import hash_password


USER_PATTERN = re.compile(
    r"^(?P<login>[A-Za-z0-9_.-]{3,32}) "
    r"(?P<clearance>public|internal|confidential|secret)$"
)


RESOURCE_PATTERN = re.compile(
    r"^(?P<title>[A-Za-z][A-Za-z0-9_]{2,31})"
    r" (?P<classification>public|internal|confidential|secret)"
    r" (?P<content>\S[^\r\n]*)$"
)

def get_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-U", "--User", type = str, help = "Строка пользователя, порядок согласно шаблону")
    group.add_argument("-R", "--Resource", type = str, help = "Строка ресурса, порядок согласно шаблону")
    args = parser.parse_args()
    return args

def parse_str(args):
    if args.User is not None:
        m = USER_PATTERN.fullmatch(args.User)
        if m:
            pwd = getpass("Пароль пользователя: ")
            return [m.group("login"), m.group("clearance"), pwd]
    elif args.Resource is not None:
        m = RESOURCE_PATTERN.fullmatch(args.Resource)
        if m:
            return [m.group("title"), m.group("classification"), m.group("content")]
    sys.exit(f"Ошибка: ввод не соответствует шаблону")

def write_table(args, table_string):
    if args.User is not None:
        login = table_string[0]
        clearance = table_string[1]
        pwd = table_string[2]
        user = User(login=login, clearance=clearance, password_hash=hash_password(pwd))

        with Session(eng) as session:
            session.add(user)
            session.commit()

    if args.Resource is not None:
        title = table_string[0]
        classification = table_string[1]
        content = table_string[2]
        resource = Resource(title=title, classification=classification, content=content)

        with Session(eng) as session:
            session.add(resource)
            session.commit()

def main():
    args = get_args()
    table_string = parse_str(args)
    write_table(args, table_string)


if __name__ == "__main__":
    main()
