from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


site = webdriver.Chrome(service=Service(executable_path='chromedriver.exe'))
site.get('https://www.kabum.com.br/hardware/placa-de-video-vga')
acoes = ActionChains(site)

ordenar = '//*[@id="Filter"]/div[1]/select'
precocrescente = '//*[@id="Filter"]/div[1]/select/option[2]'

#GPUVRAM
tengb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[2]'
twelvegb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[3]'
sixteengb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[4]'
twentygb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[6]'
twentyfourgb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[7]'
sixgb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[9]'
eightgb = '//*[@id="asideFilters"]/div[2]/details[7]/div/label[10]'
seemoregpuvram = '//*[@id="asideFilters"]/div[2]/details[7]/div/span'


#order by price (lowest to highest price)
ordenarbutton = site.find_element(By.XPATH, ordenar)
ordenarbutton.click()
sleep(3)

precocrescentebutton = site.find_element(By.XPATH, precocrescente)
precocrescentebutton.click()
sleep(3)

#click on see more
seemorebutton = site.find_element(By.XPATH, seemoregpuvram)
seemorebutton.click()
sleep(3)

#selection how many gigabytes of vram you want to search
sixgbbutton = site.find_element(By.XPATH, sixgb)
sixgbbutton.click()
sleep(3)

eightgbbutton = site.find_element(By.XPATH, eightgb)
eightgbbutton.click()
sleep(3)

tengbbutton = site.find_element(By.XPATH, tengb)
tengbbutton.click()
sleep(3)

twelvegbbutton = site.find_element(By.XPATH, twelvegb)
twelvegbbutton.click()
sleep(3)

twentygbbutton = site.find_element(By.XPATH, twentygb)
twentygbbutton.click()
sleep(3)

twentyfourgbbutton = site.find_element(By.XPATH, twentyfourgb)
twentyfourgbbutton.click()
sleep(3)

#GPUTYPE
sixteensixtyti = '//*[@id="asideFilters"]/div[2]/details[11]/div/label[6]'
sixteensixtysuper = '//*[@id="asideFilters"]/div[2]/details[11]/div/label[5]'
rtxtwentysixty = '//*[@id="asideFilters"]/div[2]/details[15]/div/label[1]'
rtxtwentysixtysuper = '//*[@id="asideFilters"]/div[2]/details[15]/div/label[2]'
rtxtwentyeighty = '//*[@id="asideFilters"]/div[2]/details[15]/div/label[3]'
rtxthirtysixty = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[2]'
rtxthirtysixtyi = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[3]'
rtxthirtyseventy = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[4]'
rtxthirtyseventyti = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[5]'
rtxthirtyeighty = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[6]'
rtxthirtyeightyti = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[7]'
rtxthirtyninety = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[8]'
rtxthirtyninetyti = '//*[@id="asideFilters"]/div[2]/details[9]/div/label[9]'
seemoregputypethirty = '//*[@id="asideFilters"]/div[2]/details[9]/div/span'
seemoreegputypetensixty = '//*[@id="asideFilters"]/div[2]/details[11]/div/span'




















