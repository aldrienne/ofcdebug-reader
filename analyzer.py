import pandas as pd


def count_unique_index(df, by):
    return df.groupby(by).size().reset_index().rename(columns={0: 'count'})


# Step 1 Load Data
main_df = pd.read_excel('ofcdebug.xlsx')
writer = pd.ExcelWriter('ofcdebug_result.xlsx', engine='xlsxwriter')


# A: Get Number of unique process
unique_process_name = main_df["process_name"].unique()
list_unique_process_name = []

for process_name in unique_process_name:
    temp_list = []
    temp_len = main_df.loc[(main_df["process_name"] == process_name)]
    temp_list.append(process_name)
    temp_list.append(len(temp_len))
    list_unique_process_name.append(temp_list)

df_unique_process_number = pd.DataFrame(list_unique_process_name, columns=['process_name', 'num_of_appearance'])
df_unique_process_number.sort_values('num_of_appearance', ascending=False, inplace=True)
df_unique_process_number.to_excel(writer, sheet_name="unique_processes")

# B: Get Number of unique_pid_tid

list_unique_pid = []

list_of_unique_process_id = main_df[['pid', 'tid', 'process_name', 'sub_process_name', 'debug_level']].drop_duplicates(['pid', 'tid'], inplace=False)

for index, row in list_of_unique_process_id.iterrows():
    temp_len = main_df.loc[(main_df['pid'] == row['pid']) & (main_df['tid'] == row['tid'])]
    temp_err = main_df.loc[(main_df['pid'] == row['pid']) & (main_df['tid'] == row['tid']) & (main_df['debug_level'] == '(E)')]
    temp_list = [row['process_name'], row['sub_process_name'], row['pid'], row['tid'], len(temp_len), len(temp_err)]
    list_unique_pid.append(temp_list)

df_unique_pid = pd.DataFrame(list_unique_pid, columns=['process_name', 'sub_process_name', 'pid', 'tid', 'num_appearance', 'num_err'])
df_unique_pid.sort_values('num_appearance', ascending=False, inplace=True)

df_unique_pid.to_excel(writer, sheet_name="unique_pid")

# C: Number of occurence per line
list_unique_line = []
list_of_unique_line = main_df[['pid', 'tid', 'process_name', 'sub_process_name', 'action', 'result']].drop_duplicates(['action', 'result'], inplace=False)

for index, row in list_of_unique_line.iterrows():
    temp_len = main_df.loc[(main_df['result'] == row['result'])]
    temp_list = [len(temp_len), row['pid'], row['tid'], row['process_name'], row['sub_process_name'], row['action'],
                 row['result']]
    list_unique_line.append(temp_list)


df_unique_pid = pd.DataFrame(list_unique_line, columns=['num_appearance', 'pid', 'tid', 'process_name', 'sub_process_name', 'action', 'result'])
df_unique_pid.sort_values('num_appearance', ascending=False, inplace=True)
df_unique_pid.to_excel(writer, sheet_name="unique_lines")

# D: Unique subprocess name
list_unique_subprocess = []
list_of_unique_subprocess = main_df[['process_name', 'sub_process_name']].drop_duplicates(['process_name', 'sub_process_name'], inplace=False)

for index, row in list_of_unique_subprocess.iterrows():
    temp_len = main_df.loc[(main_df['process_name'] == row['process_name']) & (main_df['sub_process_name'] == row['sub_process_name'])]
    temp_list = [len(temp_len), row['process_name'], row['sub_process_name']]
    list_unique_subprocess.append(temp_list)

print("=========Encoding unique lines============")
df_unique_pid = pd.DataFrame(list_unique_subprocess, columns=['num_appearance', 'process_name', 'sub_process_name'])
df_unique_pid.sort_values('num_appearance', ascending=False, inplace=True)
df_unique_pid.to_excel(writer, sheet_name="unique_subprocesses")

writer.save()
writer.close()
