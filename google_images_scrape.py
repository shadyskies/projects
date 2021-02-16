import selenium
from selenium import webdriver
import requests
import os
import hashlib
from PIL import Image
import time
import io

def get_image_urls(wd:webdriver, max_links, query):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    search_url = f"https://www.google.com/search?tbm=isch&sxsrf=ALeKk00SMu3Udk8ijCHEDJ_BC6AHQG0Leg%3A1612191933731&source=hp&biw=1920&bih=979&ei=vRgYYPiiKpm-9QO8kIzACg&q={query}&oq={query}&gs_lcp=CgNpbWcQAzIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQMyBQgAELEDMgIIADIFCAAQsQM6CAgAELEDEIMBUNYCWO8RYNgSaABwAHgAgAGkAogB1hKSAQUwLjUuNpgBAKABAaoBC2d3cy13aXotaW1n&sclient=img&ved=0ahUKEwi49ZH8-sjuAhUZX30KHTwIA6gQ4dUDCAY&uact=5"

    wd.get(search_url)
    image_urls = []
    count = 0
    while count < max_links:
        scroll_to_end(wd)
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        num_results = len(thumbnail_results)
        print(f"Found {num_results} search result. Getting source of {num_results}:..{max_links}")
        
        for img in thumbnail_results:
            try:
                img.click()
            except:
                pass
            time.sleep(3) #change according to resolution
            
            actual_images = wd.find_elements_by_css_selector("img.n3VNCb")
            for actual in actual_images:
                if "http" in actual.get_attribute('src') and "encrypted" not in actual.get_attribute('src'):
                    image_urls.append(actual.get_attribute('src'))
                    print(f"{count+1}:{actual.get_attribute('src')}")

                count = len(image_urls)
                if count >= max_links:
                    print(f"Fetched {count} urls...Downloading!")
                    return image_urls
            
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)
            return
            load_more_button = wd.find_element_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

    return image_urls


def persist_image(folder_path,query, url, count):
    try:
        image_content = requests.get(url).content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        folder_path = os.path.join(folder_path, query)
        if os.path.exists(folder_path):
            file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        else:
            os.mkdir(folder_path)
            file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"{count} :: SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")



if __name__ == '__main__':
    # wd = webdriver.Chrome(executable_path='/chromedriver')
    query = input("Enter query to download...")
    max_links = int(input("Enter number of images to download..."))
    wd = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
    links = get_image_urls(wd, max_links, query)
    wd.quit()
    if not os.path.exists('pics/'):
        os.makedirs("pics")
    count = 0
    for img in links:
        count += 1
        persist_image("pics/", query, img, count)    
    print(f"Downloaded {len(os.listdir('pics/' + str(query)))} images")
    wd.quit()