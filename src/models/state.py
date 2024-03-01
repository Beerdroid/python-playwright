from enum import StrEnum


class Role(StrEnum):
    MAIN_USER = "MAIN_USER"
    PROBLEM_USER = "PROBLEM_USER"


class Login(StrEnum):
    MAIN_USER = "USER_LOGIN"
    PROBLEM_USER = "USER_LOGIN_2"


class State(StrEnum):
    MAIN_USER = 'main_user.json'
    PROBLEM_USER = 'problem_user.json'
