from workflows import Workflow, WorkflowManager, WorkflowOpener


workflow_manager = WorkflowManager()
workflow_opener = WorkflowOpener()
new_workflow = Workflow.workflow_builder()
workflow_manager.add_workflow(new_workflow.workflow_name, new_workflow)
workflow_manager.view_workflow_urls(new_workflow.workflow_name)
workflow_opener.open_workflow(  )
