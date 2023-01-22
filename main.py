from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


# that validation is used to check xpath everytime is called
def validacaoxpath(site, xpath):
    try:
        site.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


# for with an validation for every xpath, that's prevent when the page is not loaded and can't find the xpath div
def functionrepeat(site, functionlist):
    for i in functionlist:
        while not validacaoxpath(site, i):
            sleep(1)
        funcao = site.find_element(By.XPATH, i)
        funcao.click()
        sleep(3)


servico = Service(ChromeDriverManager().install())
site = webdriver.Chrome(service=servico)

# site.get('https://www.kabum.com.br/hardware/placa-de-video-vga')
site.get('https://www.kabum.com.br/hardware/placa-de-video-vga?page_number=1&page_size=20&facet_filters=eyJNZW3Ds3JpYSI6WyIxMCBHQiIsIjEyIEdCIiwiMTYgR0IiLCIyMCBHQiIsIjI0IEdCIiwiNiBHQiIsIjggR0IiXSwiR2VGb3JjZSBHVFggU8OpcmllIDE2IjpbIkdUWCAxNjYwIFRpIiwiR1RYIDE2NjAgU3VwZXIiXX0=&sort=price')
acoes = ActionChains(site)

ordenar = '//*[@id="Filter"]/div[1]/select'
precocrescente = '//*[@id="Filter"]/div[1]/select/option[2]'
cookieaccept = '//*[@id="onetrust-accept-btn-handler"]'

# first interaction list contains the first step when the site is loaded
firstinteraction = [ordenar, precocrescente, cookieaccept]

# calling function repeat
functionrepeat(site, firstinteraction)

# GPUVRAM ID's
tengb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[2]'
twelvegb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[3]'
sixteengb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[4]'
twentygb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[6]'
twentyfourgb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[7]'
sixgb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[9]'
eightgb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[10]'
seemoregpuvram = '//*[@id="asideFilters"]/div[2]/details[7]/div/span'

# list with all the vpuvram ids
# gpuvramlist = [tengb,twelvegb,sixteengb,seemoregpuvram,twentygb,twentyfourgb,sixgb,eightgb]

# #calling functionrepeat
# functionrepeat(site, gpuvramlist)

# #GPUTYPE
# sixteensixtyti = '//*[@id="asideFilters"]/div[2]/details[11]/div/label[6]'
# sixteensixtysuper = '//*[@id="asideFilters"]/div[2]/details[11]/div/label[5]'
# seemoreegputypetensixty = '//*[@id="asideFilters"]/div[2]/details[11]/div/span'
# gpublocka = [seemoreegputypetensixty, sixteensixtyti, sixteensixtysuper]
# functionrepeat(site, gpublocka)


# separated the first gpu by blocks cause the site could be broke if you use all the checkbox we need
# the first block of gpu info
all_gpu_list_1660 = []

first_gpu_name_xpath = '//*[@id="listing"]/div[3]/div/div[2]/div[1]/main/div[1]/a/div/button/div/h2/span'
first_gpu_price_xpath = '//*[@id="listing"]/div[3]/div/div[2]/div[1]/main/div[1]/a/div/div/span[2]'
first_gpu_name = site.find_element(By.XPATH, first_gpu_name_xpath).text
first_gpu_price = site.find_element(By.XPATH, first_gpu_price_xpath).text
site.find_element(By.XPATH, first_gpu_name_xpath).click()
current_url = site.current_url
gpu_link = current_url
site.back()

all_gpu_list_1660.append([first_gpu_name, first_gpu_price, gpu_link])



# second block of gpu info
second_gpu_name_xpath = '//*[@id="listing"]/div[3]/div/div[2]/div[1]/main/div[2]/a/div/button/div/h2/span'
second_gpu_price_xpath = '//*[@id="listing"]/div[3]/div/div[2]/div[1]/main/div[2]/a/div/div/span[2]'
second_gpu_name = site.find_element(By.XPATH, second_gpu_name_xpath).text
second_gpu_price = site.find_element(By.XPATH, second_gpu_price_xpath).text
site.find_element(By.XPATH, second_gpu_name_xpath).click()
current_url = site.current_url
gpu_link = current_url
site.back()
all_gpu_list_1660.append([second_gpu_name, second_gpu_price, gpu_link])


#third block of gpu info
third_gpu_name_xpath = '//*[@id="listing"]/div[3]/div/div[2]/div[1]/main/div[3]/a/div/button/div/h2/span'
third_gpu_price_xpath = '//*[@id="listing"]/div[3]/div/div[2]/div[1]/main/div[3]/a/div/div/span[2]'
third_gpu_name = site.find_element(By.XPATH, third_gpu_name_xpath).text
third_gpu_price = site.find_element(By.XPATH, third_gpu_price_xpath).text
site.find_element(By.XPATH, third_gpu_name_xpath).click()
current_url = site.current_url
gpu_link = current_url
site.back()
all_gpu_list_1660.append([third_gpu_name, third_gpu_price, gpu_link])

print(*all_gpu_list_1660,sep='\n')



# rtxtwentysixty = '//*[@id="asideFilters"]/div[2]/details[15]/div/label[1]'
# rtxtwentysixtysuper = '//*[@id="asideFilters"]/div[2]/details[15]/div/label[2]'
# rtxtwentyeighty = '//*[@id="asideFilters"]/div[2]/details[15]/div/label[3]'
# rtxthirtysixty = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[2]'
# rtxthirtysixtyti = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[3]'
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
# functionrepeat(site, gputypelist)

sleep(500)
