openai_api = "YOUR_API_KEY"  #!Important if you want to take facts and images automatically
#used for fact generation !Important (do not change unless you want to make anything else)
prompt = "20 weird facts each fact is 15 words long or less with different topics and sentences structure, don't add any of the old facts,turn them into a Json file like {'facts':{'fact':'', 'topic': ''} and give the topic as a prompt which can be used to generate image about which the fact is talking bout not the catogory but the item itself, don't give anything else other than the dictionary."
voice = "Matthew" #options = ["Brian","Emma","Russell","Joey","Matthew","Joanna","Kimberly","Amy","Geraint","Nicole","Justin","Ivy","Kendra","Salli","Raveena",]
#Matthew is my personal favorite :)
auto_upload = False #Set it to true if you have pasted the file to the folder in the main directory
manual_upload = False
browser_data_dir = "user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome Beta\\User Data\\" #Change it into your own path
browser_exe_path = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe" #Change it into your own path