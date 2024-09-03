# import requests

# url = "https://example.com/"

# response = requests.get(url)

# if response.status_code == 200:
#     content = response.text

#     # Save the content to a file
#     with open('document.html', 'w', encoding='utf-8') as file:
#         file.write(content)
    
#     print("Content saved to 'document.html' successfully!")
# else:
#     print("Failed to retrieve the content. Status code:", response.status_code)


# import requests

# url = "https://example.com/"  # Replace with the Django website URL

# response = requests.get(url)

# if response.status_code == 200:
#     content = response.text

#     # Save the content to a file
#     with open('django_website.html', 'w', encoding='utf-8') as file:
#         file.write(content)
    
#     print("Content saved to 'django_website.html' successfully!")
# else:
#     print("Failed to retrieve the content. Status code:", response.status_code)


#installed selenium and webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


url = "https://example.com"  # Replace with the ReactJS website URL

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get(url)

# Get the page source (fully rendered HTML)
content = driver.page_source

# Save the content to a file
with open('reactjs_website.html', 'w', encoding='utf-8') as file:
    file.write(content)

driver.quit()

print("Content saved to 'reactjs_website.html' successfully!")
