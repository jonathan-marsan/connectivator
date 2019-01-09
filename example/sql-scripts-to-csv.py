"""
How to take SQL scripts and write to local folder in CSV format
"""

from connectivator import postgres, transfer

db_conx = postgres.get_engine('events')

transfer.sqls_to_csv(filepath='example/folder_with_sql_files', db_conn=db_conx,
                     output_folder='local_folder_path')
