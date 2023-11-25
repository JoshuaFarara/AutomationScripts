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

    def __init__(self, workflow_manager):
        self.workflow_manager = workflow_manager

    def open_workflow(self, workflow_name):
        # if not workflow_name:
        #     print("Workflow name not set. Please set the name first.")
        #     return
        
        # if not .website_urls:
        #     print(f"No URLs added to {workflow_name} workflow yet.")
        #     return
        
        workflow_to_open = self.workflow_manager.workflows.get(workflow_name)
        if workflow_to_open:
            chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            # Open the workflow using subprocess or any other method
            print(f"Opening workflow '{workflow_name}'...")
            # Add your code to open the workflow (e.g., subprocess or webbrowser)
            # For example:
            # webbrowser.open_new_tab(workflow_to_open.website_urls[0])  # Open the first URL for demonstration
            subprocess.Popen([chrome_path, '--new-window'] + workflow_to_open.website_urls)
            print(f"Opened {workflow_name} workflow in Chrome successfully.")
        else:
            print(f"Workflow '{workflow_name}' not found.")