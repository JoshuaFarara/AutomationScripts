import subprocess
import webbrowser
import time

class Workflow:

    def __init__(self, workflow_name):
        self.workflow_name = workflow_name
        self.website_urls = []

    def build_workflow(self):
        self.website_urls = self.add_url_to_workflow
    
    def add_url_to_workflow(workflow):
        url_to_add = input("Enter a new url...")
        return url_to_add
    
    
    def open_workflow1():
        website_urls = ['https://www.geeksforgeeks.org/100-days-of-code-a-complete-guide-for-beginners-and-experienced/', 'https://www.geeksforgeeks.org/python-programming-language/',
                        'https://www.geeksforgeeks.org/introduction-to-python/', 'https://www.geeksforgeeks.org/python-programming-examples/']
        open_in_chrome(website_urls)
        print("Workflow1, loaded successfully.")

    def open_in_chrome(urls):
    # Path to your Chrome installation
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    # Open a new Chrome window with the group of tabs
        subprocess.Popen([chrome_path, '--new-window'] + urls)

workflow=Workflow('ProjectTest')
workflow.build_workflow()