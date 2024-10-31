import pandas as pd
import datetime

queries = []

def add_q(query: str) -> None:
    row = (query, datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S"))
    queries.append(row)

def view_stored_queries() -> str:
    df = pd.DataFrame(queries)
    print(df)
    return 'End of commands. \n'

q_list = {
    'add_q': add_q,
    'view_stored_queries': view_stored_queries,
}
