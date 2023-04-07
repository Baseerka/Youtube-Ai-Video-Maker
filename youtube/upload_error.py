import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By 



def upload_errorr(video_data):
    options = webdriver.ChromeOptions()
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--log-level=3")
    options.add_argument("user-data-dir=C:\\Users\\vinay viswanath\\AppData\\Local\\Google\\Chrome Beta\\User Data\\")
    options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"
    print("Checking for video from videos folder...")
    time.sleep(6)

    dir_path = 'youtube/videos/'
    count = 0

    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    print(count, " Videos found in the videos folder, ready to upload...")
    time.sleep(6)

    for i in range(count):
        bot = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
        try:
            bot.get("https://studio.youtube.com")
            time.sleep(3)
            upload_button = bot.find_element(By.XPATH, '//*[@id="upload-icon"]')
            upload_button.click()
            time.sleep(1)
        except:
            exit("Upload icon click failed")

        try:
            file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
            simp_path = os.path.join(dir_path, os.listdir(dir_path)[i])
            abs_path = os.path.abspath(simp_path)
                
            file_input.send_keys(abs_path)
            time.sleep(7)
        except:
            exit("Error while adding video file.")

        try:
            error_title = video_data['title']
            title_box = bot.find_element(By.XPATH, '//*[@id="textbox"]')
            title_box.clear()
            title_box.send_keys(error_title)

            time.sleep(1)
        except:
            exit("Error while adding title.")
        
        try:
            video_description = video_data['description']
            description_box = bot.find_element(By.XPATH, '//div[@aria-label="Tell viewers about your video"]')
            description_box.send_keys(video_description)
            time.sleep(1)

        except:
            exit("Error while adding description.")

        try:
            next_button = bot.find_element(By.XPATH, '//*[@id="next-button"]')
            for i in range(3):
                next_button.click()
                time.sleep(1)
        except:
            exit("Error while pressing next button.")

        try:
            done_button = bot.find_element(By.XPATH, '//*[@id="done-button"]')
            done_button.click()
            time.sleep(5)
        except:
            exit("Error while finishing things up.")