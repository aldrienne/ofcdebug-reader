"""
Author: Aldrienne Janne G. Maniti
"""

import re
from datetime import datetime
from Line import ProcessedLine
import xlsxwriter

raw_lines = []
processed_lines = []

def convert_raw_line(line):
    """
    Helper function to extract values from ofcdebug
    Param:
        line:(str) Contains 1 line value from ofcdebug
    """
    # Step 2 Extract Date and time
    date_raw = line[0:10]
    time_raw = line[11:19]
    # Convert date and time from STRING
    date_time_raw = date_raw[8:10] + '/' + date_raw[5:7] + '/' + date_raw[2:4] + ' ' + time_raw
    date = datetime.strptime(date_time_raw, '%d/%m/%y %H:%M:%S')


    # Extracting process and thread
    re_process_subprocess = re.search('\[.{4} : .{4}]',line)
    process_thread = re_process_subprocess.group().replace('[','').replace(']','').split(':')
    # Step 3 Extract Process_id
    process_id = process_thread[0]
    # Step 4 Extract Thread_id
    thread_id = process_thread[1]

    # Step 5 Debug Level
    re.debug_level = re.search('\([A-Z]\)',line)
    debug_level = re.debug_level.group()

    # Step 6 Extract Process_name
    re_process = re.search('\[[a-zA-Z]*(.exe|.EXE)\]',line)
    process_name = re_process.group()

    # Step 6 Extract Sub Process_name
    re_subprocess = re.search('\[[^:]*?\]',line)
    sub_process_name = re_subprocess.group()

    #Step 7 Extract Action
    if '.exe]' in line:
        parent_action = line.split('.exe]')
    elif '.EXE]'in line:
        parent_action = line.split('.EXE]')

    sub_parent = parent_action[1].split(' - ')
    action = sub_parent[0]

    #Step 8 Extract result
    result = ''
    for i in range(1,len(sub_parent)):
        result += sub_parent[i]


    #Step 9 Create a class
    processed_line = ProcessedLine(
        date_time=date,
        process_id=process_id,
        thread_id=thread_id,
        debug_level=debug_level,
        process_name=process_name,
        sub_process_name=sub_process_name,
        action=action,
        result=result
    )


    return processed_line.get_line()


if __name__ == '__main__':
    # Step 1 - Place logs to memory
    # Make sure that everything in single line
    with open('ofcdebug.log', 'r', encoding='ISO-8859-15') as line:
        for i in line:
            temp_line = ''
            if i.startswith('20'):
                raw_lines.append(i.strip())
            else:
                raw_lines[-1] + i.strip()

    # Process Raw Lines
    for i in raw_lines:
        try:
            processed_lines.append(convert_raw_line(i))
        except Exception as e:
            print(e)
            print(i)

    # Create an xlsx file
    workbook = xlsxwriter.Workbook('ofcdebug1.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    print(processed_lines[0])

    for date_time, process_id, thread_id, debug_level, process_name, sub_process_name, action, result in (processed_lines):
        worksheet.write(row, col, date_time)
        worksheet.write(row, col + 1, process_id)
        worksheet.write(row, col + 2, thread_id)
        worksheet.write(row, col + 3, debug_level)
        worksheet.write(row, col + 4, process_name)
        worksheet.write(row, col + 5, sub_process_name)
        worksheet.write(row, col + 6, action)
        worksheet.write(row, col + 7, result)
        row += 1

    workbook.close()
