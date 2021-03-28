import urllib.request
import numpy as np
from tqdm import tqdm
from selenium import webdriver
import time
#instantiate the driver
sleeps = [1, 0.5, 1.5, 0.7]
driver_path = "/Users/larrydcj/Documents/Programming/Projects/AC_Classifier/chromedriver/chromedriver"
wd = webdriver.Chrome(executable_path=driver_path)

q = "A-10"
search_url = f"https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}"


wd.get(search_url)

page_scroll_sleep = 2

    # Get scroll height
last_height = wd.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
	wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(page_scroll_sleep)
	new_height = wd.execute_script("return document.body.scrollHeight")

	if new_height == last_height:
		try:
			element = wd.find_elements_by_class_name('mye4qd')
			element[0].click()
		except:
			break

	last_height = new_height

# gets link list of images
image_links = wd.find_elements_by_class_name('rg_i.Q4LuWd')

src_links = [image_links[i].get_attribute('src') for i in range(len(image_links))]
data_src_links = [image_links[i].get_attribute('data-src') for i in range(len(image_links))]
# urllib save images into folder and renames using data_name string
for i, link in enumerate(tqdm(image_links)):
	name = data_name + f'{i}.jpeg'
	urllib.request.urlretrieve(link, name)
	time.sleep(np.random.choice(sleeps))

wd.quit()