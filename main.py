from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

#that validation is used to check xpath everytime is called
def validacaoxpath(site, xpath):
    try:
        site.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

#for with an validation for every xpath, that's prevent when the page is not loaded and can't find the xpath div
def functionrepeat(site, functionlist):
    for i in functionlist:
        while not validacaoxpath(site, i):
            sleep(1)
        funcao = site.find_element(By.XPATH, i)
        funcao.click()
        sleep(3)

site = webdriver.Chrome(service=Service(executable_path='chromedriver.exe'))
site.get('https://www.kabum.com.br/hardware/placa-de-video-vga')
acoes = ActionChains(site)

ordenar = '//*[@id="Filter"]/div[1]/select'
precocrescente = '//*[@id="Filter"]/div[1]/select/option[2]'
cookieaccept = '//*[@id="onetrust-accept-btn-handler"]'

#first interaction list contains the first step when the site is loaded
firstinteraction = [cookieaccept,ordenar,precocrescente]

#calling function repeat
functionrepeat(site, firstinteraction)

#GPUVRAM ID's
tengb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[2]'
twelvegb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[3]'
sixteengb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[4]'
twentygb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[6]'
twentyfourgb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[7]'
sixgb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[9]'
eightgb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[10]'
seemoregpuvram = '//*[@id="asideFilters"]/div[2]/details[7]/div/span'

#list with all the vpuvram ids
gpuvramlist = [tengb,twelvegb,sixteengb,seemoregpuvram,twentygb,twentyfourgb,sixgb,eightgb]

#calling functionrepeat
functionrepeat(site, gpuvramlist)

#GPUTYPE
# sixteensixtyti = '//*[@id="asideFilters"]/div[2]/details[11]/div/label[6]'
sixteensixtysuper = '//*[@id="asideFilters"]/div[2]/details[11]/div/label[5]'
rtxtwentysixty = '//*[@id="asideFilters"]/div[2]/details[15]/div/label[1]'
rtxtwentysixtysuper = '//*[@id="asideFilters"]/div[2]/details[15]/div/label[2]'
rtxtwentyeighty = '//*[@id="asideFilters"]/div[2]/details[15]/div/label[3]'
rtxthirtysixty = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[2]'
rtxthirtysixtyti = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[3]'
rtxthirtyseventy = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[4]'
rtxthirtyseventyti = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[5]'
rtxthirtyeighty = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[6]'
rtxthirtyeightyti = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[7]'
rtxthirtyninety = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[8]'
rtxthirtyninetyti = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[9]'
seemoregputypethirty = '//*[@id="asideFilters"]/div[2]/details[9]/div/span'
seemoreegputypetensixty = '//*[@id="asideFilters"]/div[2]/details[11]/div/span'

#list with all gputype
gputypelist =[seemoreegputypetensixty,sixteensixtysuper,rtxtwentysixty,rtxtwentysixtysuper,rtxtwentyeighty,
              rtxthirtysixty,rtxthirtysixtyti,rtxthirtyseventy,rtxthirtyseventyti,seemoregputypethirty,rtxthirtyeighty,
              rtxthirtyeightyti,rtxthirtyninety,rtxthirtyninetyti]

#calling functionrepeat
functionrepeat(site, gputypelist)






















