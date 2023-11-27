import subprocess

class Workflow:

    def __init__(self):
        self.workflow_name = None
        self.website_urls = []
        self.hotkeys = None


    def set_workflow_name(self):
        name = input("Enter the name for the new workflow:")
        self.workflow_name = name
       

    def set_url(self):
        if not self.workflow_name:
            print("Workflow name not set. Please set the name first.")
            return
        
        url_to_add = input(f"Enter a new URL for {self.workflow_name}: ")
        self.website_urls.append(url_to_add)
        print(f"Added {url_to_add} to {self.workflow_name} workflow.")
    
    def set_hotkeys(self):
        hotkeys = input("Enter youtr custom hotkeys to open the new workflow e.g.Ctrl+Alt+X:")
        self.hotkeys = hotkeys

    # Now we need to create a workflow process. 
    @classmethod
    def workflow_builder(cls):
        workflow = cls()
        workflow.set_workflow_name()
        workflow.set_url()
        workflow.set_hotkeys()
        print(f"The {workflow.workflow_name} workflow was built successfully.")
        for url in workflow.website_urls:
            print('The initial url for this workflow is: ', url)
        print(f"You have chosen {workflow.hotkeys}, as your hotkeys for this workflow.")
        
        # return workflow
    def __str__(self):
        return f"Workflow: {self.workflow_name}\nURLs: {', '.join(self.website_urls)}"
        
Workflow.workflow_builder()

class WorkflowManager:
    def __init__(self):
        self.workflows = []

    def add_workflow(self, workflow):
        self.workflows.append(workflow)
        print(f"{workflow.workflow_name} added to Workflow Manager.")

    def view_workflow(self, workflow_name):
        for workflow in self.workflows:
            if workflow.workflow_name == workflow_name:
                print(workflow)
                return
        print(f"Workflow '{workflow_name}' not found.")

    def add_url_to_workflow(self, workflow_name, url):
        for workflow in self.workflows:
            if workflow.workflow_name == workflow_name:
                workflow.website_urls.append(url)
                print(f"Added {url} to {workflow_name} workflow.")
                return
        print(f"Workflow '{workflow_name}' not found.")

    def open_workflow_in_browser(self, workflow_name):
        # Code to open the workflow in a browser goes here
        pass

    def update_workflow(self, workflow_name, new_name):
        for workflow in self.workflows:
            if workflow.workflow_name == workflow_name:
                workflow.workflow_name = new_name
                print(f"Updated workflow name to {new_name}.")
                return
        print(f"Workflow '{workflow_name}' not found.")

    def delete_workflow(self, workflow_name):
        for workflow in self.workflows:
            if workflow.workflow_name == workflow_name:
                self.workflows.remove(workflow)
                print(f"Deleted workflow '{workflow_name}'.")
                return
        print(f"Workflow '{workflow_name}' not found.")