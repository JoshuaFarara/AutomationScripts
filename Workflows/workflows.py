import subprocess
import webbrowser
import time

class Workflow:

    def __init__(self):
        self.workflow_name = None
        self.website_urls = []

    def set_workflow_name(self, name):
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
  
    # def open_in_chrome(urls):
    #     # Path to your Chrome installation
    #     chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    #     # Open a new Chrome window with the group of tabs
    #     subprocess.Popen([chrome_path, '--new-window'] + urls)



# Now we need to create a workflow process. 
def build_workflow():
    workflow_name = input("Enter the name for your workflow: ")
    workflow_instance = Workflow()
    setattr(workflow_instance, workflow_name, workflow_instance)
    workflow_instance.set_workflow_name(workflow_name)
    workflow_instance.add_url_to_workflow()

def workflow_builder():
    workflow = Workflow()
    workflow.set_workflow_name('WorkflowBuildTest')
    workflow.add_url_to_workflow()
    return workflow


# Example usage:
workflow_name = input("Enter the name for your workflow: ")
workflow_instance = Workflow()
setattr(workflow_instance, workflow_name, workflow_instance)

# Setting the workflow name
workflow_instance.set_workflow_name(workflow_name)
workflow_instance.add_url_to_workflow()

WFTest.open_workflow()