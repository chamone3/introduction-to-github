import math 
import mailbox

from sklearn.tree import export_text
export_text
def save_counts(table_counts):
    file_name = os.path.join(FILES_PATH, "counts_all_prd_tint" + today_str + ".xlsx")
    start = datetime.now()
    #print(start, "start saving file from", file_name)
    
    table_counts.to_excel(file_name, index=False)
    
    end = datetime.now()
    #print(end, "File saved - time spent:", end-start)
    
    counts = table_counts.groupby(['ENV', 'table_name']).agg({'id_file': 'count', 'records':'sum'}).reset_index()
    counts = pd.merge(counts[counts['ENV'] == 'PROD'], 
                      counts[counts['ENV'] == 'TINT'],
                      how='outer',
                      on=['table_name'],
                      indicator=True,
                      suffixes=('_PROD', '_TINT')
                     )
    counts = counts[['table_name', 'id_file_PROD', 'id_file_TINT', 'records_PROD', 'records_TINT']]
    counts['id_file_diff'] = counts['id_file_PROD'] - counts['id_file_TINT']
    counts['records_diff'] = counts['records_PROD'] - counts['records_TINT']
    
    file_name = os.path.join(FILES_PATH, "counts_prd_tint" + today_str + ".xlsx")
    start = datetime.now()
    #print(start, "start saving file from", file_name)
                             
    counts.to_excel(file_name, index=False)
    
    end = datetime.now()
    #print(end, "File saved - time spent:", end-start)
    return counts

<<<<<<< HEAD
=======

>>>>>>> feature/oneflow
