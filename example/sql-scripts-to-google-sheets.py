"""
How to take SQL scripts and write to a Google Sheet
"""

from connectivator import postgres, transfer, gsheets

db_conx = postgres.get_engine('events')
gs_conx = gsheets.get_gs_con()

transfer.sqls_to_gs(filepath='example/folder_with_sql_files', db_conn=db_conx,
                    gs_con=gs_conx, output_gs_id='goosheet_sheet_id')
