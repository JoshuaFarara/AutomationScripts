import os

def create_batch_file(directory, file_name, python_script_path):
    batch_file_path = os.path.join(directory, file_name)
    command_to_execute = f'python "{python_script_path}"'
    
    with open(batch_file_path, 'w') as batch_file:
        batch_file.write('@echo off\n')
        batch_file.write(command_to_execute)

# Example usage:
script_path = 'C:\\Users\\User\\Desktop\\AutomationScripts\\Workflows\\workflow_100DayC.py'
batch_directory = 'C:\\Users\\User\\Desktop\\AutomationScripts\\Workflows\\Batch'
batch_file_name = 'run_workflow.bat'

create_batch_file(batch_directory, batch_file_name, script_path)