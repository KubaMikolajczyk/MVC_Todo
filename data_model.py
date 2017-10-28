import controler


class TodoList:
    '''class which holds whole list of tasks'''

    def __init__(self):
        self.todo_list = []


class FileOperations:
    '''operations related to file handling'''

    def saving_to_file(file_name):
        export_file_string = ''

        with open(file_name, 'w') as new_file_write:
            for task_object in task_list.todo_list:
                export_file_string += task_object.task_name + ","
                
                export_file_string += task_object.task_description + ","
                # returns string equivalents of integers instead of bools for optimalisation
                if task_object.is_done:
                    export_file_string += '1' + ","
                else:
                    export_file_string += '0' + ","
                
                export_file_string += "\n"

            new_file_write.write(export_file_string)
            new_file_write.close()
    
    def loading_from_file(file_name):
        from_file_to_obj_list = []

        with open(file_name, 'r') as load_file:
                for line in load_file:
                    from_file_to_obj_list.append(line.split(','))
                
                for task_object in from_file_to_obj_list:
                    new_object = controler.AddItem()
                    new_object.task_name = task_object[0]
                    new_object.task_description = task_object[1]
                    if task_object[2] == "1":
                        new_object.is_done = True
                    else:
                        new_object.is_done = False
                    task_list.todo_list.append(new_object)

task_list = TodoList() 