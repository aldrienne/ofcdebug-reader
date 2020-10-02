#Pandas
import pandas as pd


def count_unique_index(df, by):
    return df.groupby(by).size().reset_index().rename(columns={0:'count'})


# Step 1 Load Data
main_df = pd.read_excel('ofcdebug.xlsx')
writer = pd.ExcelWriter('ofcdebug_result.xlsx', engine='xlsxwriter')


# A: Get Number of unique process
print("=========Unique processes============")
unique_process_name = main_df["process_name"].unique()
list_unique_process_name = []

for process_name in unique_process_name:
    temp_list = []
    temp_len = main_df.loc[(main_df["process_name"] == process_name)]
    temp_list.append(process_name)
    temp_list.append(len(temp_len))
    list_unique_process_name.append(temp_list)

df_unique_process_number = pd.DataFrame(list_unique_process_name, columns=['process_name', 'num_of_appearance'])
df_unique_process_number.sort_values('num_of_appearance',ascending=False, inplace=True)
df_unique_process_number.to_excel(writer, sheet_name="unique_processes")

# B: Get Number of unique_pid_tid
print("=========Unique PID/TID============")

list_unique_pid = []

list_of_unique_process_id = main_df[['pid', 'tid', 'process_name', 'sub_process_name', 'debug_level']].drop_duplicates(['pid', 'tid'], inplace=False)

for index, row in list_of_unique_process_id.iterrows():
    temp_len = main_df.loc[(main_df['pid'] == row['pid']) & (main_df['tid'] == row['tid'])]
    temp_err = main_df.loc[(main_df['pid'] == row['pid']) & (main_df['tid'] == row['tid']) & (main_df['debug_level'] == '(E)')]
    temp_list = []
    temp_list.append(row['process_name'])
    temp_list.append(row['sub_process_name'])
    temp_list.append(row['pid'])
    temp_list.append(row['tid'])
    temp_list.append(len(temp_len))
    temp_list.append(len(temp_err))
    list_unique_pid.append(temp_list)

df_unique_pid = pd.DataFrame(list_unique_pid, columns=['process_name', 'sub_process_name', 'pid', 'tid', 'num_appearance', 'num_err'])
df_unique_pid.sort_values('num_appearance', ascending=False, inplace=True)

df_unique_pid.to_excel(writer, sheet_name="unique_pid")

# C: Number of occurence per line
print("=========Occurence Per Line============")
list_unique_line = []
list_of_unique_line = main_df[['pid', 'tid', 'process_name', 'sub_process_name', 'action', 'result']].drop_duplicates(['action', 'result'], inplace=False)

for index, row in list_of_unique_line.iterrows():
    temp_len = main_df.loc[(main_df['result'] == row['result'])]
    temp_list = []
    temp_list.append(len(temp_len))
    temp_list.append(row['pid'])
    temp_list.append(row['tid'])
    temp_list.append(row['process_name'])
    temp_list.append(row['sub_process_name'])
    temp_list.append(row['action'])
    temp_list.append(row['result'])
    list_unique_line.append(temp_list)

print("=========Encoding unique lines============")
df_unique_pid = pd.DataFrame(list_unique_line, columns=['num_appearance', 'pid', 'tid', 'process_name', 'sub_process_name','action', 'result'])
df_unique_pid.sort_values('num_appearance', ascending=False, inplace=True)
df_unique_pid.to_excel(writer, sheet_name="unique_lines")

writer.save()
writer.close()
# A: Error
# df_num_of_error = main_df.loc[(main_df['debug_level'] == "(E)")]

# A.1 Error per process
#Show total number of errors and errors per process_name
# unique_process_name = df_num_of_error["process_name"].unique()
#
# list_unique_process_name = []
#
# for process_name in unique_process_name:
#     temp_list = []
#     temp_len = df_num_of_error.loc[(df_num_of_error["process_name"] == process_name)]
#     temp_list.append(process_name)
#     temp_list.append(len(temp_len))
#     list_unique_process_name.append(temp_list)
#
# df_unique_process_number = pd.DataFrame(list_unique_process_name, columns=['process_name', 'num_errors'])
# df_unique_process_number.sort_values('num_errors',ascending=False, inplace=True)
# df_unique_process_number.to_excel(writer, sheet_name="unique_process")
#
# # A.2 Error per pid and tid
# list_unique_pid = []
#
# list_of_unique_process_id = df_num_of_error[['pid', 'tid']].drop_duplicates(['pid', 'tid'], inplace=False)
#
# for index, row in list_of_unique_process_id.iterrows():
#     temp_len = df_num_of_error.loc[(df_num_of_error['pid'] == row['pid']) & (df_num_of_error['tid'] == row['tid'])]
#     temp_list = []
#     temp_list.append(row['pid'])
#     temp_list.append(row['tid'])
#     temp_list.append(len(temp_len))
#     list_unique_pid.append(temp_list)
#
# print(list_unique_pid[0])
#
# df_unique_pid = pd.DataFrame(list_unique_pid, columns=['pid', 'tid', 'num_errors'])
# df_unique_pid.sort_values('num_errors', ascending=False, inplace=True)
# print(df_unique_pid)
# df_unique_pid.to_excel(writer ,sheet_name="unique_pid")
# writer.save()
# writer.close()


# for row in list_of_unique_process_id.iterrows():
#     print(row['pid'])

# for pid, tid in list_of_unique_process_id:
#     print('pid'+ type(pid))`
#     temp_len = num_of_error.loc[num_of_error['pid'] == pid & num_of_error['tid']]

# for process_id in list_of_unique_process_id:
#     temp_len = num_of_error.loc[num_of_error['pid'] == pro]
#     # print(process_id + ': ' + str(len(temp_len)))
#
# #A.3
#
# print(uniqueValues)
