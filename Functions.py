import sqlalchemy
from sqlalchemy import create_engine, Result
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.testing.util import total_size
from sqlalchemy_utils import database_exists, create_database


# def command_to_string(command: Result) -> str:
#     """Turns the result of a SQL command into a useful string format
#
#     This isn't for the user to access.
#     """
#     result = ""
#     f = command
#     for row in f:
#         result += str(row)
#         result += "\n"
#     return result
#
# # User accessed functions:
#
# def display_column_names() -> str:
#     display_column_names_command = session.execute(text("SELECT column_name, data_type \
#          FROM information_schema.columns \
#          WHERE table_name = 'food_coded'  \
#          ;"))
#     result = command_to_string(display_column_names_command)
#     return result
#
#
# def int_to_boolean(table:str, column: str):
#     """Checks if a column is suitable for conversion to a boolean and converts it if it is.
#
#     This is not yet functional! IT needs to check the result of the command and if the first number is zero,
#     do the conversion."""
#
#     find_not_boolean = session.execute(text(f"SELECT count(*), {column} \
#              FROM {table} \
#     		 WHERE {column} NOT IN ( 0, 1 ) \
#     		 GROUP BY {column};"))
#     return command_to_string(find_not_boolean)
#
#
# def nullify_invalid_entries(table:str, column: str,  lower: str, upper: str) -> str:
#     """Converts values outside given range to null."""
#
#     find_outside = session.execute(text(f"SELECT count(*), {column} \
#                  FROM {table} \
#         		 WHERE {column} NOT BETWEEN {lower} AND {upper} \
#         		 GROUP BY {column};"))
#
#     command = session.execute(text(
#         f"UPDATE {table} \
#             SET {column} = NULL \
#             WHERE {column} NOT IN ( {lower}, {upper} ); "
#     ))
#     return "Changed values: " + command_to_string(find_outside)
#
#
# def not_boolean_proportion(table:str, column: str) -> str:
#     """Finds how much of a given column is not a 0 or 1"""
#
#     find_not_boolean = session.execute(text(f"SELECT count(*) \
#              FROM {table} \
#              WHERE {column} NOT IN ( 0, 1 );"))
#     total = session.execute(text(f"SELECT count(*) \
#              FROM {table};"))
#
#     f = (find_not_boolean.mappings().first())
#     t = (total.mappings().first())
#     result = f.get('count')/t.get('count')
#     return result
#
#
def find_substring(table:str, column: str, substring: str) -> str:
    """Returns a string with the substring and number of occurrences"""
    result = session.execute(text(f"SELECT {column} \
                     FROM {table} \
            		 ;"))
    result = command_to_string(result)
    rlist = result.split('\n')
    counter = 0
    for line in rlist:
        if substring in line:
            counter += 1
    return DF.add_row(table, column, "", "Substring occurrences", substring, str(counter))

def test_query() -> str:
    """Just a test"""
    return "Success"


def h() -> str:
    """Prints a list of the available commands for the user."""
    for i in range(len(f_list)-1):
        print (list(f_list)[i+1])
    return 'For more information on what each function does, \
please use the documentation. \n \n '

f_list = {
    'h': h,
    'test_query': test_query,
    # 'display_column_names': display_column_names,
    # 'int_to_boolean': int_to_boolean,
    # 'nullify_invalid_entries': nullify_invalid_entries,
    # 'not_boolean_proportion': not_boolean_proportion,
    # 'find_substring': find_substring,
    # 'view_stored_data': DF.view_stored_data,
    # 'export_data': DF.export_data
}

