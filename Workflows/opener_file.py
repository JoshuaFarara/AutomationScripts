from instantiation_file import workflow_manager, workflow_opener
from workflows import Workflow
# from workflows import instantiation_file
# WorkflowManager, WorkflowOpener

# workflow_manager = WorkflowManager()
# workflow_opener = WorkflowOpener(workflow_manager)

new_workflow = Workflow.workflow_builder()
workflow_manager.add_workflow(new_workflow.workflow_name, new_workflow)
workflow_manager.view_workflow_urls(new_workflow.workflow_name)
workflow_opener.open_workflow('testopener')
