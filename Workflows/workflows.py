import subprocess
import webbrowser
import time

class Workflow:

    def __init__(self):
        self.workflow_name = None
        self.website_urls = []

    def set_workflow_name(self):
        name = input("Enter the name for the new workflow:")
        self.workflow_name = name
       

    def add_url_to_workflow(self):
        if not self.workflow_name:
            print("Workflow name not set. Please set the name first.")
            return
        
        url_to_add = input(f"Enter a new URL for {self.workflow_name}: ")
        self.website_urls.append(url_to_add)
        print(f"Added {url_to_add} to {self.workflow_name} workflow.")
    
    
    def open_workflow(self):
        if not self.workflow_name:
            print("Workflow name not set. Please set the name first.")
            return
        
        if not self.website_urls:
            print(f"No URLs added to {self.workflow_name} workflow yet.")
            return
        
        # Path to your Chrome installation
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        # Open a new Chrome window with the group of tabs
        subprocess.Popen([chrome_path, '--new-window'] + self.website_urls)
        print(f"Opened {self.workflow_name} workflow in Chrome successfully.")

    # Now we need to create a workflow process. 
    @classmethod
    def workflow_builder(cls):
        workflow = cls()
        workflow.set_workflow_name()
        workflow.add_url_to_workflow()
        print(f"The {workflow.workflow_name} workflow was built successfully.")
        for url in workflow.website_urls:
            print(url)
        return workflow
    
    def save_workflow(self):
        pass

class WorkflowManager:
    def __init__(self):
        self.workflows = {}

    def add_workflow(self, workflow_name, workflow_instance):
        if workflow_name not in self.workflows:
            self.workflows[workflow_name] = workflow_instance
            print(f"Workflow '{workflow_name}' added to the manager.")
        else:
            print(f"Workflow '{workflow_name}' already exists in the manager.")


    def view_workflow_urls(self, workflow_name):
        if workflow_name in self.workflows:
            workflow = self.workflows[workflow_name]
            print(f"Workflow Name: {workflow_name}")
            for url in workflow.website_urls:
                print(url)
        else:
            print(f"Workflow '{workflow_name}' not found in the manager.")
    
class WorkflowOpener(WorkflowManager):
    def open_workflow(self, workflow_name):
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

        if not self.workflow_name:
            print("Workflow name not set. Please set the name first.")
            return
        
        if not self.website_urls:
            print(f"No URLs added to {self.workflow_name} workflow yet.")
            return
        
        workflow_to_open = self.workflows.get(workflow_name)
        if workflow_to_open:
            # Open the workflow using subprocess or any other method
            print(f"Opening workflow '{workflow_name}'...")
            # Add your code to open the workflow (e.g., subprocess or webbrowser)
            # For example:
            # webbrowser.open_new_tab(workflow_to_open.website_urls[0])  # Open the first URL for demonstration
            subprocess.Popen([chrome_path, '--new-window'] + workflow_to_open.website_urls)
            print(f"Opened {self.workflow_name} workflow in Chrome successfully.")
        else:
            print(f"Workflow '{workflow_name}' not found.")

# Example usage:
# workflow_manager = WorkflowManager()
# new_workflow = Workflow.workflow_builder()
# workflow_manager.add_workflow(new_workflow.workflow_name, new_workflow)
# workflow_manager.view_workflow_urls(new_workflow.workflow_name)
# workflow_name = input("Enter the name for the new workflow: ")


# Storing the created workflow in the data structure
# workflows[workflow_name] = new_workflow

# # Accessing the stored workflow by name
# stored_workflow = workflows.get(workflow_name)

# # You can use stored_workflow to perform operations or access its methods
# if stored_workflow:
#     stored_workflow.add_url_to_workflow()
#     # stored_workflow.open_workflow()

# # setattr(workflow_instance, workflow_name, workflow_instance)

# # # Setting the workflow name
# # workflow_instance.set_workflow_name(workflow_name)
# # workflow_instance.add_url_to_workflow()

# # WFTest.open_workflow()
# for workflow in workflows:
#     print(f"Workflow Name: {workflow_name}")