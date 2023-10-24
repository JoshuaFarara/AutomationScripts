import subprocess
import webbrowser
import time


'''
First iteration. Will open a list of websites in new tabs. 

'''

# def open_in_chrome(url):
#     # chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application'  # Path to your Chrome installation
#     # browser = webbrowser.get(chrome_path)

#     webbrowser.open(url, new=2)
#     # browser


#     # for url in website_urls:
#     #     browser.open_new_tab(url)
# # def open_dmc_workspace(url):
# #     website_urls = ['http://lyfjourney.com', 'https://joshuafarara.com', 'https://fararatheartist.com']
# #     for url in website_urls:
# #         open_in_chrome(url)

# # Usage example
# website_urls = ['http://lyfjourney.com', 'https://joshuafarara.com', 'https://fararatheartist.com']
# # open_in_chrome(website_urls)
# for url in website_urls:
#     open_in_chrome(url)
    





'''
Addon To create Website Workflows 

'''

def open_workflow1():
    website_urls = ['https://www.geeksforgeeks.org/100-days-of-code-a-complete-guide-for-beginners-and-experienced/', 'https://www.geeksforgeeks.org/python-programming-language/',
'https://www.geeksforgeeks.org/introduction-to-python/', 'https://www.geeksforgeeks.org/python-programming-examples/']
    open_in_chrome(website_urls)
    print("Workflow1, loaded successfully.")

def open_workflow2():
    website_urls = ['https://squareup.com/login?return_to=%2Fappointments%2Fcalendar/', 'https://analytics.google.com/analytics/web/?authuser=4#/report-home/a149998776w212601873p205023173',
'https://fararatheartist.com/', 'https://fararatheartist.com/bio-link/', 'https://bladedmoths.com/', 'https://www.instagram.com/fararatheartist/', 'https://studio.youtube.com/channel/UC2JvDDY9vZM57vKPkRraaAw/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D']
    open_in_chrome(website_urls)
    print("Workflow2, loaded successfully.")

def open_workflow3():
    website_urls = ['http://lyfjourney.com/', 'https://www.instagram.com/lyfjourney/', 'https://www.facebook.com/profile.php?id=100063472273527', 'https://drive.google.com/drive/u/4/my-drive']
    open_in_chrome(website_urls)
    print("Workflow3, loaded successfully.")

def open_workflow4():
    website_urls = ['https://tsheets.intuit.com/#w_timesheets_v2', 'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox', 'https://drive.google.com/drive/my-drive']
    open_in_chrome(website_urls)
    # for url in website_urls:
    #     webbrowser.open_new_tab(url)
    # webbrowser.open(website_urls, new=2)
    print("Workflow4, loaded successfully.")

def open_workflow5():
    website_urls = ['https://my.georgiasouthern.edu/portal/portal.php', 'https://georgiasouthern.desire2learn.com/d2l/home/742330', 'https://georgiasouthern.desire2learn.com/d2l/home/742625']
    open_in_chrome(website_urls)
    # for url in website_urls:
    #     webbrowser.open_new_tab(url)
    # webbrowser.open(website_urls, new=2)
    print("Workflow4, loaded successfully.")
    # 

def open_in_chrome(urls):
    # Path to your Chrome installation
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

    # Open a new Chrome window with the group of tabs
    subprocess.Popen([chrome_path, '--new-window'] + urls)

    # Open a new Chrome window
    # subprocess.Popen(['start', 'chrome', '--new-window'], shell=True)

    # Wait for the window to open (adjust the delay as needed)
    # You can also use other methods to ensure the window is fully loaded
    # time.sleep(3)
    # for url in urls:
    #     webbrowser.open_new_tab(url)
        # webbrowser.get('chrome').open_new(url)


def add_url_to_workflow(workflow):
    url_to_add = input("Enter a new url...")
    return url_to_add
    