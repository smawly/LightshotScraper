import string
import random

def generate_random_part():
    characters = string.ascii_lowercase + string.digits
    random_part = ''.join(random.choice(characters) for _ in range(6))
    return random_part

def generate_random_site_url():
    base_url = "https://prnt.sc"
    random_part = generate_random_part()
    url = f"{base_url}/{random_part}"
    return url

if __name__ == "__main__":
    num_sites_to_generate = 5
    
    for i in range(num_sites_to_generate):
        random_site_url = generate_random_site_url()
        print(f"Random Site {i+1}: {random_site_url}")
