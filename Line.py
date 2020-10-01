
class ProcessedLine:
    def __init__(self, date_time, process_id, thread_id, debug_level, process_name, sub_process_name, action, result):
        self.date_time = date_time
        self.process_id = process_id
        self.thread_id = thread_id
        self.debug_level = debug_level
        self.process_name = process_name
        self.sub_process_name = sub_process_name
        self.action = action
        self.result = result

    def get_line(self):
        temp_list = []
        temp_list.append(str(self.date_time))
        temp_list.append(str(self.process_id))
        temp_list.append(str(self.thread_id))
        temp_list.append(str(self.debug_level))
        temp_list.append(str(self.process_name))
        temp_list.append(str(self.sub_process_name))
        temp_list.append(str(self.action))
        temp_list.append(str(self.result))
        return temp_list


    # def __str__(self):
    #     """Return a string representation of the object"""
    #     return str(self.date_time) + '[' + self.process_id + ':' + self.thread_id + ']' + ' ' + self.debug_level + ' ' + self.sub_process_name + self.proces_name + self.action + self.result
