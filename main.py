from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


# that validation is used to check xpath everytime is called
def xpath_validation(site, xpath):
    try:
        site.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


# for with an validation for every xpath, that's prevent when the page is not loaded and can't find the xpath div
def function_repeat(site, function_list):
    for i in function_list:
        while not xpath_validation(site, i):
            sleep(1)
        funcao = site.find_element(By.XPATH, i)
        funcao.click()
        sleep(3)

# in this function we click on the first 3 gpus separated by type and save all the information we need in one list
def data_crawler(site, data_list):
    for i in range(1, 4):
        gpu_name_xpath = f'//*[@id="listing"]/div[3]/div/div[2]/div[1]/main/div[{i}]/a/div/button/div/h2/span'
        gpu_price_xpath = f'//*[@id="listing"]/div[3]/div/div[2]/div[1]/main/div[{i}]/a/div/div/span[2]'
        gpu_name = site.find_element(By.XPATH, gpu_name_xpath).text
        gpu_price = site.find_element(By.XPATH, gpu_price_xpath).text
        site.find_element(By.XPATH, gpu_name_xpath).click()
        current_url = site.current_url
        gpu_link = current_url
        data_list.append([gpu_name, gpu_price, gpu_link])
        site.back()

    for l in data_list:
        for i in l:
            print(i)
        print()


servico = Service(ChromeDriverManager().install())
site = webdriver.Chrome(service=servico)

site.get('https://www.kabum.com.br/hardware/placa-de-video-vga')
# site.get('https://www.kabum.com.br/hardware/placa-de-video-vga?page_number=1&page_size=20&facet_filters'
#          '=eyJNZW3Ds3JpYSI6WyIxMCBHQiIsIjEyIEdCIiwiMTYgR0IiLCIyMCBHQiIsIjI0IEdCIiwiNiBHQiIsIjggR0IiXSwiR2VGb3JjZSBSVFgg'
#          'U8OpcmllIDIwIjpbIlJUWCAyMDgwIFN1cGVyIiwiUlRYIDIwNjAgU3VwZXIiLCJSVFggMjA2MCJdfQ==&sort=price')
site_actions = ActionChains(site)

order_by = '//*[@id="Filter"]/div[1]/select'
preco_crescente = '//*[@id="Filter"]/div[1]/select/option[2]'
cookie_accept = '//*[@id="onetrust-accept-btn-handler"]'

# first interaction list contains the first step when the site is loaded
first_interaction = [order_by, preco_crescente, cookie_accept]

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

## all series 1660 we need to mine info
gpu_1660 = '//*[@id="asideFilters"]/div[2]/details[12]/div/label[4]'
gpu_1660_super = '//*[@id="asideFilters"]/div[2]/details[12]/div/label[5]'
gpu_1660_ti = '//*[@id="asideFilters"]/div[2]/details[12]/div/label[6]'
see_more_gpu_type_1660 = '//*[@id="asideFilters"]/div[2]/details[12]/div/span'

# rtx_1660 series we need for function repeat and click
gpu_series_1660 = [gpu_1660, gpu_1660_super, see_more_gpu_type_1660, gpu_1660_ti]
function_repeat(site, gpu_series_1660)

# list for data crawler function call
all_gpu_list_1660 = []
data_crawler(site, all_gpu_list_1660)

#removing 1660 series to call another one
function_repeat(site, gpu_series_1660)

# all series 2000 we need to mine inf
rtx_2060 = '//*[@id="asideFilters"]/div[2]/details[17]/div/label[1]'
rtx_2060_super = '//*[@id="asideFilters"]/div[2]/details[17]/div/label[2]'
rtx_2080 = '//*[@id="asideFilters"]/div[2]/details[17]/div/label[3]'

# rtx_200 series we need for function repeat and click
rtx_series_2000 = [rtx_2060, rtx_2060_super, rtx_2080]
function_repeat(site, rtx_series_2000)

# calling function data crawler to mine all the information and save in all_gpu_list_2000
all_gpu_list_2000 = []
data_crawler(site, all_gpu_list_2000)

#removing 2000 series to call another one
function_repeat(site, rtx_series_2000)

# rtx_thirty_sixty = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[2]'
# rtx_thirty_sixty_ti = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[3]'
# rtxthirtyseventy = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[4]'
# rtxthirtyseventyti = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[5]'
# rtxthirtyeighty = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[6]'
# rtxthirtyeightyti = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[7]'
# rtxthirtyninety = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[8]'
# rtxthirtyninetyti = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[9]'
# seemoregputypethirty = '//*[@id="asideFilters"]/div[2]/details[9]/div/span'
#
#
# list with all gputype
# gputypelist =[rtxtwentysixty,rtxtwentysixtysuper,rtxtwentyeighty,
#               rtxthirtysixty,rtxthirtysixtyti,rtxthirtyseventy,rtxthirtyseventyti,seemoregputypethirty,rtxthirtyeighty,
#               rtxthirtyeightyti,rtxthirtyninety,rtxthirtyninetyti]
#
# calling functionrepeat
# function_repeat(site, gputypelist)

sleep(500)
