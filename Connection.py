import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, Result
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.testing.util import total_size
from sqlalchemy_utils import database_exists, create_database

from LocalSettings import postgresql as settings

import DerivedDF as D
import SQLFunctions as F
import QueryDF as Q

full_list = [D.df_command_list, F.f_list, Q.q_list]

def get_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine

engine = get_engine(settings['pguser'],
                    settings['pgpasswd'],
                    settings['pghost'],
                    settings['pgport'],
                    settings['pgdb'])


def get_engine_from_settings():
    keys = ['pguser', 'pgpasswd', 'pghost', 'pgport', 'pgdb' ]
    if not all (key in keys for key in settings.keys()):
        raise Exception ('Bad config file')
    return get_engine(settings['pguser'],
                    settings['pgpasswd'],
                    settings['pghost'],
                    settings['pgport'],
                    settings['pgdb'])


def get_session():
    engine = get_engine_from_settings()
    session = sessionmaker (bind = engine)()
    return session

def command_to_string(command: Result) -> str:
    """Turns the result of a SQL command into a useful string format

    This isn't for the user to access.
    """
    result = ""
    f = command
    for row in f:
        result += str(row)
        result += "\n"
    return result

# This is where everything runs:

metadata = sqlalchemy.MetaData()

session = get_session()

def execute_query(command: str, args_list: list) -> str:
    """Executes SQL queries and adds data to Derived DF where necessary"""
    args = map(eval, args_list)
    query_tuple = command(*args)
    result = command_to_string(session.execute(text(query_tuple[0])))
    if query_tuple[1] == True:
        print(result)
        print(D.add_row(query_tuple[0] ,result, query_tuple[2]) + '\n')
    return result

def command_run(i_list: list) -> str:
    """Checks for errors when executing queries.
    """
    func_name = i_list[0]
    func = F.f_list[func_name]
    try:
        result = execute_query(func, i_list[1:])
        return f"Result: {result}"
    except Exception as e:
        print(f"Error calling function: {e}")
    return "\n"


def main():
    """The main function running the program"""
    user_quit = False

    while not user_quit:
        user_input = input("Enter the function you want to run (followed by arguments). \n"
                           "Enter 'h' to see the function list, or 'q' to quit: ")
        if user_input == 'q':
             break

        i_list = user_input.split()
        func_name = i_list[0]
        if func_name in F.f_list:
            command_run(i_list)
        elif func_name in D.df_command_list:
            func = D.df_command_list[func_name]
            try:
                args = map(eval, i_list[1:])
                result = func(*args)
                return result
            except Exception as e:
                return (f"Error calling function: {e}")
        elif func_name in Q.q_list:
            func = Q.q_list[func_name]
            try:
                args = map(eval, i_list[1:])
                result = func(*args)
                return result
            except Exception as e:
                print(f"Error calling function: {e}")
        else:
            print("Function not found.")


if __name__ == '__main__':
    main()