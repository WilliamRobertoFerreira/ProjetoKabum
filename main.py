from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


# that validation is used to check xpath everytime is called
def xpath_validation(site, xpath):
    """
    This Function look for the xpath before start the scraping, Trying to find the information
    :param site: site is the webdriver service
    :param xpath: xpath is where is the information XPath expression can be used to search through an XML document,
     and extract information from any part of the document, such as an element or attribute
    :return: return True if the xpath is located, if not, return false
    """
    try:
        site.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


# for with an validation for every xpath, that's prevent when the page is not loaded and can't find the xpath div
def function_repeat(site, function_list):
    """
    This function use xpath validation, if the information is located in the website it continues, if not it waits 1
    second waiting for the page to load
    :param site: site is the webdriver service
    :param function_list: Function list is an list with all parameters we need to use to click or select in the website
    :return: return the click on selected information
    """
    for i in function_list:
        while not xpath_validation(site, i):
            sleep(1)
        funcao = site.find_element(By.XPATH, i)
        funcao.click()
        sleep(3)


# in this function we click on the first 3 gpus separated by type and save all the information we need in one list
def data_scraping(site, data_list):
    """

    :param site: site is the webdriver service
    :param data_list: This data list have all the data will return in the end of funcion, it scrap information like
    price, link and name
    :return: return a list with the first 3 gpu info
    """
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
    """
    That def return the data we mined, using a method list in list, It separates multiple lists within a single list
    :param data_list:
    :return:
    """
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

site.get('https://www.kabum.com.br/hardware/placa-de-video-vga')
site_actions = ActionChains(site)

order_by = '//*[@id="Filter"]/div[1]/select'
price_asc = '//*[@id="Filter"]/div[1]/select/option[2]'
cookie_accept = '//*[@id="onetrust-accept-btn-handler"]'

# first interaction list contains the first step when the site is loaded
first_interaction = [order_by, price_asc, cookie_accept]

# calling function repeat
function_repeat(site, first_interaction)

# GPUVRAM ID's
ten_gb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[2]'
twelve_gb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[3]'
sixteen_gb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[4]'
twenty_gb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[6]'
twenty_four_gb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[7]'
six_gb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[9]'
eight_gb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[10]'
see_more_gpu_video_ram = '//*[@id="asideFilters"]/div[2]/details[7]/div/span'

# list with all the GPU video ram
gpu_video_ram_list = [ten_gb, twelve_gb, sixteen_gb, see_more_gpu_video_ram, twenty_gb, twenty_four_gb, six_gb,
                      eight_gb]

# calling function_repeat
function_repeat(site, gpu_video_ram_list)

# all series 1660 we need to mine info
gpu_1660 = '//*[@id="asideFilters"]/div[2]/details[12]/div/label[4]'
gpu_1660_super = '//*[@id="asideFilters"]/div[2]/details[12]/div/label[5]'
gpu_1660_ti = '//*[@id="asideFilters"]/div[2]/details[12]/div/label[6]'
see_more_gpu_type_1660 = '//*[@id="asideFilters"]/div[2]/details[12]/div/span'

# rtx_1660 series we need for function repeat and click
gtx_series_1660 = [gpu_1660, gpu_1660_super, see_more_gpu_type_1660, gpu_1660_ti]
function_repeat(site, gtx_series_1660)

# list for data crawler function call
all_gpu_list_1660 = []
data_scraping(site, all_gpu_list_1660)

# removing 1660 series to call another one
gtx_series_1660_unselect = [gpu_1660, gpu_1660_super, gpu_1660_ti]
function_repeat(site, gtx_series_1660_unselect)

# all series 2000 we need to mine info
rtx_2060 = '//*[@id="asideFilters"]/div[2]/details[17]/div/label[1]'
rtx_2060_super = '//*[@id="asideFilters"]/div[2]/details[17]/div/label[2]'
rtx_2080 = '//*[@id="asideFilters"]/div[2]/details[17]/div/label[3]'

# rtx_200 series we need for function repeat and click
rtx_series_2000 = [rtx_2060, rtx_2060_super, rtx_2080]
function_repeat(site, rtx_series_2000)

# calling function data crawler to mine all the information and save in all_gpu_list_2000
all_gpu_list_2000 = []
data_scraping(site, all_gpu_list_2000)

# removing series 20 to call another one
function_repeat(site, rtx_series_2000)

# all series 30 we need to mine info
rtx_3060 = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[2]'
rtx_3060_ti = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[3]'
rtx_3070 = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[4]'
rtx_3070_ti = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[5]'
see_more_gpu_type_3000 = '//*[@id="asideFilters"]/div[2]/details[9]/div/span'
rtx_3080 = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[6]'
rtx_3080_ti = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[7]'
rtx_3090 = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[8]'
rtx_3090_ti = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[9]'

# list with all rtx series 30
rtx_series_3000 = [rtx_3060, rtx_3060_ti, rtx_3070, rtx_3070_ti, see_more_gpu_type_3000,
                   rtx_3080, rtx_3080_ti, rtx_3090, rtx_3090_ti]

# calling function_repeat
function_repeat(site, rtx_series_3000)

# calling function data crawler to mine all the information and save in all_gpu_list_3000
all_gpu_list_3000 = []
data_scraping(site, all_gpu_list_3000)

# calling function_repeat do unselect all the info we don't need anymore
rtx_series_3000_unselect = [rtx_3060, rtx_3060_ti, rtx_3070, rtx_3070_ti,
                            rtx_3080, rtx_3080_ti, rtx_3090, rtx_3090_ti]
function_repeat(site, rtx_series_3000_unselect)

print('All series 16 with values and links: ')
show_lists(all_gpu_list_1660)

print('All Series 20 with values and links: ')
show_lists(all_gpu_list_2000)

print('All series 30 with values and links: ')
show_lists(all_gpu_list_3000)
