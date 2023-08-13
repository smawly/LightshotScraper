import requests
from bs4 import BeautifulSoup
import string
import random
import time

def generate_random_part():
    characters = string.ascii_lowercase + string.digits
    random_part = ''.join(random.choice(characters) for _ in range(6))
    return random_part

def check_screenshot(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html_code = response.text
        soup = BeautifulSoup(html_code, 'html.parser')
        img_tag = soup.find('img', id='screenshot-image')

        if img_tag:
            src = img_tag.get('src')
            expected_src = "/html/body/div[3]/div/img//st.prntscr.com/2023/07/24/0635/img/0_173a7b_211be8ff.png"
            if src and expected_src in src:
                return True, src
            else:
                return False, src
        else:
            return False, "Image not found."
    else:
        return False, f"Failed to fetch page: {response.status_code}"

def scrape_images(num_images_to_find):
    base_url = "https://prnt.sc"

    result = []
    counter = 0

    while counter < num_images_to_find:
        random_part = generate_random_part()
        url = f"{base_url}/{random_part}"
        print(f"Checking URL: {url}")

        is_valid, src = check_screenshot(url)
        if is_valid:
            result.append(f"{url} - true ({src})")
            counter += 1
        else:
            result.append(f"{url} - false ({src})")

        time.sleep(1)  # Add a 1-second delay before checking the next URL

    return result

if __name__ == "__main__":
    num_images_to_find = 5
    result = scrape_images(num_images_to_find)

    print("Results:")
    for i, r in enumerate(result, start=1):
        print(f"Check {i}: {r}")
