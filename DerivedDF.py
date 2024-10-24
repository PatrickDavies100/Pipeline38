import pandas as pd

from SQLFunctions import f_list

# This is the list that will contain a new table that I can export.
output_data = []

# Each function returns a string that tells the user what it did

def add_row(Table: str, Column1 :str, Column2: str, Measure: str, Argument: str, Value: str) -> str:
    output_data.append({'Table': Table,
                        'Column1': Column1,
                        'Column2': Column2,
                        'Measure': Measure,
                        'Argument': Argument,
                        'Value': Value})
    return 'One row added to dataframe'

def view_stored_data() -> str:
    df = pd.DataFrame(output_data)
    print(df)
    return 'End of data \n'

def export_data(filename: str) -> str:
    df = pd.DataFrame(output_data)
    df.to_csv(f"{filename}.csv", index=False)
    return (f"CSV file created as {filename}.csv")

def h() -> str:
    """Prints a list of the available commands for the user."""
    for j in range (len(df_command_list)-1):
        print(list(df_command_list)[j+1])
    for i in range(len(f_list)):
        print (list(f_list)[i])
    return 'For more information on what each function does, \
please use the documentation. \n \n '

df_command_list = {
    'h': h,
    'add_row': add_row,
    'view_stored_data': view_stored_data,
    'export_data': export_data
}
