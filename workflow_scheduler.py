# # from chromeTabs import all
# import chromeTabs 
# import schedule
# import time
# import subprocess

# def run_script(script_path):
#     subprocess.run(['python', script_path])  # Replace 'python' with the appropriate command if needed

# # Define the schedule for each script
# schedule.every().day.at("08:00").do(run_script, 'script1.py')
# schedule.every().day.at("12:30").do(run_script, 'script2.py')
# schedule.every().day.at("18:45").do(run_script, 'script3.py')

# while True:
#     schedule.run_pending()
#     time.sleep(1)