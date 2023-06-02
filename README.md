# Website Workflow Automation

## Description
The Website Workflow Automation program is designed to automate the process of opening groups of websites simultaneously, referred to as "workflows." It allows users to create predefined sets of websites and assign them to macro keys for seamless automation and increased productivity.

The program utilizes Python and various libraries, including `subprocess` and `webbrowser`, to open a new browser window with a group of websites as tabs when a specific workflow is triggered.

## Features
- Create multiple website workflows with different sets of websites.
- Assign each website workflow to a specific macro key for easy access and automation.
- Open a new browser window with the selected websites as tabs when a workflow is triggered.
- Improve productivity by quickly accessing sets of websites used frequently.

## Usage
1. Install Python: Make sure you have Python installed on your system. You can download and install Python from the official website: https://www.python.org/

2. Set up the environment:
   - Clone or download this repository to your local machine.
   - Install the required dependencies by running `pip install -r requirements.txt` in your command prompt or terminal.

3. Configure the website workflows:
   - Open the `chromeTabs.py` file in a text editor.
   - Define your website workflows by creating functions and specifying the URLs for each workflow.
   - Save the file after defining all the workflows.

4. Assign workflows to macro keys:
   - Open the `main.py` file in a text editor.
   - Import the desired workflow functions from `chromeTabs.py`.
   - Call the appropriate function for each macro key assignment.
   - Save the file after assigning the workflows.

5. Run the program:
   - Open your command prompt or terminal.
   - Navigate to the program's directory.
   - Execute the `main.py` file by running `python main.py`.
   - The program will be running and waiting for macro key triggers.

6. Trigger a workflow:
   - Press the assigned macro key for a specific workflow.
   - The program will open a new browser window with the set of websites as tabs for that workflow.

7. Enjoy automated website workflows and increased productivity!

## Customization
- You can customize the website URLs for each workflow by modifying the corresponding functions in the `chromeTabs.py` file.
- Adjust the macro key assignments in the `main.py` file based on your preferences and available macro keys on your system.
- Modify the program code to add more functionalities or integrate with other tools as needed.

## Requirements
- Python 3.x
- Internet connection
- Supported web browser (e.g., Chrome, Firefox)

## Limitations
- The program currently supports opening websites in a new browser window but does not support multiple separate browser instances.
- The behavior of macro keys and their assignment may vary depending on the macro software or hardware being used.

## Contributions
Contributions to the project are welcome. Feel free to open issues or submit pull requests on the project repository.

## Acknowledgments
This program was developed as a personal project and was inspired by the need for efficient website navigation and automation.

