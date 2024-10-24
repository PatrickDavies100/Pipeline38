import pandas as pd

queries = []

def add_q(query: str) -> None:
    queries.append(query)

def view_stored_queries() -> str:
    df = pd.DataFrame(queries)
    print(df)
    return 'End of commands \n'

q_list = {
    'add_q': add_q,
    'view_stored_queries': view_stored_queries,
}
