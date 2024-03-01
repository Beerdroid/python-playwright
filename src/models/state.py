from enum import Enum


class Role(Enum):
    MAIN_USER = "MAIN_USER"
    PROBLEM_USER = "PROBLEM_USER"


class Login(Enum):
    MAIN_USER = "USER_LOGIN"
    PROBLEM_USER = "USER_LOGIN_2"


class State(Enum):
    MAIN_USER = 'main_user.json'
    PROBLEM_USER = 'problem_user.json'
