from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

# in this function we click on the first 3 gpus separated by type and save all the information we need in one list
def data_scraping(site, data_list):
    for i in range(1, 4):
        sleep(2)
        gpu_name_xpath = f'//*[@id="listing"]/div[3]/div/div[2]/div[1]/main/div[{i}]/a/div/button/div/h2/span'
        gpu_price_xpath = f'//*[@id="listing"]/div[3]/div/div[2]/div[1]/main/div[{i}]/a/div/div/span[2]'
        gpu_name = site.find_element(By.XPATH, gpu_name_xpath).text
        gpu_price = site.find_element(By.XPATH, gpu_price_xpath).text
        sleep(2)
        site.find_element(By.XPATH, gpu_name_xpath).click()
        sleep(3)
        current_url = site.current_url
        gpu_link = current_url
        data_list.append([gpu_name, gpu_price, gpu_link])
        site.back()
        sleep(1)


def show_lists(data_list):
    for l in data_list:
        for i in l:
            print(i)
        print()


# if you are using Chrome browser please select this one
driver_service = Service(ChromeDriverManager().install())
site = webdriver.Chrome(service=driver_service)

# if you are using Firefox Browser please select this one
# driver_service = Service(GeckoDriverManager().install())
# site = webdriver.Firefox(service=driver_service)

# calling series 16 page
site.get('https://www.kabum.com.br/hardware/placa-de-video-vga?page_number=1&page_size=20&facet_filters=eyJNZW3'
         'Ds3JpYSI6WyIxMiBHQiIsIjE2IEdCIiwiMjAgR0IiLCIyNCBHQiIsIjYgR0IiLCI4IEdCIiwiMTAgR0IiXSwiR'
         '2VGb3JjZSBHVFggU8OpcmllIDE2IjpbIkdUWCAxNjYwIiwiR1RYIDE2NjAgU3VwZXIiLCJHVFggMTY2MCBUaSJdfQ==&sort=price')
sleep(2)
cookie_accept = '//*[@id="onetrust-accept-btn-handler"]'
site.find_element(By.XPATH, cookie_accept).click()
sleep(2)


# list for data crawler function call
all_gpu_list_1660 = []
data_scraping(site, all_gpu_list_1660)
sleep(2)

# calling series 20 page
site.get('https://www.kabum.com.br/hardware/placa-de-video-vga?page_number=1&page_size=20&facet_filters=eyJNZW3Ds3JpY'
         'SI6WyIxMiBHQiIsIjE2IEdCIiwiMjAgR0IiLCIyNCBHQiIsIjYgR0IiLCI4IEdCIiwiMTAgR0IiXSwiR2VGb3JjZSBSVFggU8OpcmllIDIw'
         'IjpbIlJUWCAyMDYwIiwiUlRYIDIwNjAgU3VwZXIiLCJSVFggMjA4MCBTdXBlciJdfQ==&sort=price')
sleep(2)

# calling function data crawler to mine all the information and save in all_gpu_list_2000
all_gpu_list_2000 = []
data_scraping(site, all_gpu_list_2000)
sleep(2)

# calling series 30 page
site.get('https://www.kabum.com.br/hardware/placa-de-video-vga?page_number=1&page_size=20&facet_filters=eyJNZW3Ds3'
         'JpYSI6WyIxMiBHQiIsIjE2IEdCIiwiMjAgR0IiLCIyNCBHQiIsIjYgR0IiLCI4IEdCIiwiMTAgR0IiXSwiR2VGb3JjZSBSVFggU8Opcm'
         'llIDMwIjpbIlJUWCAzMDYwIiwiUlRYIDMwNjAgVGkiLCJSVFggMzA3MCIsIlJUWCAzMDcwIFRpIiwiUlRYIDMwODAiLCJSVFggMzA4MC'
         'BUaSIsIlJUWCAzMDkwIiwiUlRYIDMwOTAgVGkiXX0=&sort=price')
sleep(2)

# calling function data crawler to mine all the information and save in all_gpu_list_3000
all_gpu_list_3000 = []
data_scraping(site, all_gpu_list_3000)
sleep(2)

#printing all the results
print('All series 16 with values and links: ')
show_lists(all_gpu_list_1660)

print('All Series 20 with values and links: ')
show_lists(all_gpu_list_2000)

print('All series 30 with values and links: ')
show_lists(all_gpu_list_3000)
