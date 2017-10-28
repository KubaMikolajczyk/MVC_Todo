import controler


class TodoList:
    ''''''

    def __init__(self):
        self.todo_list = []


class FileOperations:
    ''''''

    def saving_to_file(file_name):
        export_file_string = ''

        with open(file_name, 'w') as new_file_write:
            for task_object in task_list.todo_list:
                export_file_string += task_object.task_name + ","
                export_file_string += task_object.task_description + ","
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
                    task_list.todo_list.append(new_object)

task_list = TodoList()

