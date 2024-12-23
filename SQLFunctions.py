import DerivedDF as D
import QueryDF as Q


# Each function returns a tuple with three parts:
# [0] An SQL query as a string
# [1] A boolean of whether to add it to DerivedDF
# [2] A description of what the value represents

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


def find_substring(table:str, column: str, substring: str) -> str:
    """Finds the number of occurrences for a substring in a column"""
    description = "Number of rows containing substring"
    result1 = (f"SELECT COUNT(*) \
                    FROM {table} \
                    WHERE {column} \
                    LIKE '%{substring}%' \
                    ;")
    Q.add_q(result1)
    result = (result1, True, description)
    return result

def test_SQL_query(table: str, column: str) -> str:
    """Just a test"""
    description = "Measures something in the table"
    result1 = (f"SELECT {column} \
                FROM {table} \
                ;")
    Q.add_q(result1)
    result = (result1, True, description)
    return result

def test_SQL_query_2(table: str, column: str, rando) -> str:
    """Just a test"""
    description = "Measures something in the table"
    result1 = (f"SELECT {column} \
                FROM {table} \
                ;")
    Q.add_q(result1)
    result = (result1, True, description)
    return result


f_list = {
    'test_SQL_query': test_SQL_query,
    'test_SQL_query_2': test_SQL_query_2,
    # 'display_column_names': display_column_names,
    # 'int_to_boolean': int_to_boolean,
    # 'nullify_invalid_entries': nullify_invalid_entries,
    # 'not_boolean_proportion': not_boolean_proportion,
    'find_substring': find_substring,
}

