import time

import getpass
from selenium import webdriver
from texttable import Texttable
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# [ device type, customer, tag name, version xpath, tag name xpath]

class EmvExtraction:
    def __init__(self):
        self.emv_ver_url = 'https://conf.invenco.com/display/CC/EMV+Versions'
        self.chrome_driver_filepath = 'D:/JonNgoStorage/version_checker/chromedriver_win32/chromedriver.exe'

    xpath = [
        ['G6-300','ALL','upc.contactlessemvl1.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[3]/td[2]/p[1]','//*[@id="main-content"]/div[1]/table/tbody/tr[3]/td[3]'],
        ['G6-300','ALL','opt.emv.contactless.kernel.mastercard.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[4]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[4]/td[3]'],
        ['G6-300','ALL','opt.emv.contactless.kernel.paywave.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[5]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[5]/td[3]'],
        ['G6-300','ALL','opt.emv.contactless.kernel.dpas.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[6]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[6]/td[3]'],
        ['G6-300','ALL','opt.emv.contactless.kernel.express.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[7]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[7]/td[3]'],
        ['G6-300','ALL','opt.emv.contactless.kernel.jcb.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[8]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[8]/td[3]'],
        ['G6-300','ALL','opt.emv.contactless.kernel.unionpay.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[9]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[9]/td[3]'],
        ['G6-300','ALL','opt.emv.contactless.kernel.interac.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[10]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[10]/td[3]'],
        ['G6-300','ALL','upc.emvkernel.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[11]/td[2]/p[1]','//*[@id="main-content"]/div[1]/table/tbody/tr[11]/td[3]'],
        ['G6-300','ALL','upc.offlinepin.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[12]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[12]/td[3]'],
        ['G6-300','ALL','upc.emvl1.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[13]/td[2]/span','//*[@id="main-content"]/div[1]/table/tbody/tr[13]/td[3]'],
        ['G6-300','ALL','upc.entrypoint.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[15]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[15]/td[3]/p[2]'],
        ['G6-300','ALL','upc.cep.ver','//*[@id="main-content"]/div[1]/table/tbody/tr[16]/td[2]','//*[@id="main-content"]/div[1]/table/tbody/tr[16]/td[3]/p[2]'],

        ['G7-100','NCR','upc.contactlessemvl1.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[3]/td[2]/p[1]','//*[@id="main-content"]/div[2]/table/tbody/tr[3]/td[4]'],
        ['G7-100','NCR','upc.paypass.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[4]/td[2]/span','//*[@id="main-content"]/div[2]/table/tbody/tr[4]/td[4]'],
        ['G7-100','NCR','upc.paywave.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[5]/td[2]','//*[@id="main-content"]/div[2]/table/tbody/tr[5]/td[4]'],
        ['G7-100','NCR','upc.dpas.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[6]/td[2]/span','//*[@id="main-content"]/div[2]/table/tbody/tr[6]/td[4]'],
        ['G7-100','NCR','upc.express.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[7]/td[2]/span','//*[@id="main-content"]/div[2]/table/tbody/tr[7]/td[4]'],
        ['G7-100','NCR','upc.interac.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[8]/td[2]','//*[@id="main-content"]/div[2]/table/tbody/tr[8]/td[4]'],
        ['G7-100','NCR','upc.emvkernel.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[9]/td[2]/p[1]','//*[@id="main-content"]/div[2]/table/tbody/tr[9]/td[4]'],
        ['G7-100','NCR','upc.offlinepin.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[10]/td[2]/span','//*[@id="main-content"]/div[2]/table/tbody/tr[10]/td[4]'],
        ['G7-100','NCR','upc.emvl1.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[11]/td[2]','//*[@id="main-content"]/div[2]/table/tbody/tr[11]/td[4]'],
        ['G7-100', 'NCR','upc.entrypoint.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[13]/td[2]/p[2]','//*[@id="main-content"]/div[2]/table/tbody/tr[13]/td[4]'],
        ['G7-100', 'NCR','upc.cep.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[14]/td[2]/p[2]','//*[@id="main-content"]/div[2]/table/tbody/tr[14]/td[4]'],

        ['G7-100', 'Canada','upc.contactlessemvl1.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[3]/td[3]/p[1]','//*[@id="main-content"]/div[2]/table/tbody/tr[3]/td[4]'],
        ['G7-100', 'Canada', 'upc.paypass.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[4]/td[3]/span','//*[@id="main-content"]/div[2]/table/tbody/tr[4]/td[4]'],
        ['G7-100', 'Canada', 'upc.paywave.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[5]/td[3]','//*[@id="main-content"]/div[2]/table/tbody/tr[5]/td[4]'],
        ['G7-100', 'Canada', 'upc.dpas.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[6]/td[3]/span','//*[@id="main-content"]/div[2]/table/tbody/tr[6]/td[4]'],
        ['G7-100', 'Canada', 'upc.express.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[7]/td[3]/span','//*[@id="main-content"]/div[2]/table/tbody/tr[7]/td[4]'],
        ['G7-100', 'Canada', 'upc.interac.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[8]/td[3]','//*[@id="main-content"]/div[2]/table/tbody/tr[8]/td[4]'],
        ['G7-100', 'Canada', 'upc.emvkernel.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[9]/td[3]/p[1]','//*[@id="main-content"]/div[2]/table/tbody/tr[9]/td[4]'],
        ['G7-100', 'Canada', 'upc.offlinepin.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[10]/td[3]/span','//*[@id="main-content"]/div[2]/table/tbody/tr[10]/td[4]'],
        ['G7-100', 'Canada', 'upc.emvl1.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[11]/td[3]','//*[@id="main-content"]/div[2]/table/tbody/tr[11]/td[4]'],
        ['G7-100', 'Canada', 'upc.entrypoint.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[13]/td[3]','//*[@id="main-content"]/div[2]/table/tbody/tr[13]/td[4]'],
        ['G7-100', 'Canada', 'upc.cep.ver','//*[@id="main-content"]/div[2]/table/tbody/tr[14]/td[3]','//*[@id="main-content"]/div[2]/table/tbody/tr[14]/td[4]'],

        ['G6-200', 'ALL', 'pcd.ver.emvl1', '//*[@id="main-content"]/div[4]/table/tbody/tr[1]/td[2]', '//*[@id="main-content"]/div[4]/table/tbody/tr[1]/td[3]'],
        ['G6-200', 'ALL', 'pcd.ver.kernels.pp','//*[@id="main-content"]/div[4]/table/tbody/tr[2]/td[2]/span', '//*[@id="main-content"]/div[4]/table/tbody/tr[2]/td[3]'],
        ['G6-200', 'ALL', 'pcd.ver.kernels.pw','//*[@id="main-content"]/div[4]/table/tbody/tr[3]/td[2]', '//*[@id="main-content"]/div[4]/table/tbody/tr[3]/td[3]'],
        ['G6-200', 'ALL', 'pcd.ver.kernels.dp','//*[@id="main-content"]/div[4]/table/tbody/tr[4]/td[2]/span', '//*[@id="main-content"]/div[4]/table/tbody/tr[4]/td[3]'],
        ['G6-200', 'ALL', 'pcd.ver.kernels.xp','//*[@id="main-content"]/div[4]/table/tbody/tr[5]/td[2]/span', '//*[@id="main-content"]/div[4]/table/tbody/tr[5]/td[3]'],
        ['G6-200', 'ALL', 'emv.ver.emvk','//*[@id="main-content"]/div[4]/table/tbody/tr[6]/td[2]', '//*[@id="main-content"]/div[4]/table/tbody/tr[6]/td[3]/p'],
        ['G6-200', 'ALL', 'upc.ver.emvl1','//*[@id="main-content"]/div[4]/table/tbody/tr[8]/td[2]', '//*[@id="main-content"]/div[4]/table/tbody/tr[8]/td[3]/p'],
    ]

    def extractVersion(self,v):
        #RegEx explanation
        # (
        # group and capture
        #   [\d.]+      any character of: digits (0-9), '.'(1 or more times)
        # )
        return re.search(r"([\d.]+)",v).group()

    def login(self,username,password,device_m,customer_m):
        driver = webdriver.Chrome(self.chrome_driver_filepath)
        driver.get(self.emv_ver_url);

        driver.set_page_load_timeout(20)
        driver.maximize_window()

        username_xpath = driver.find_element_by_id("os_username")
        password_xpath = driver.find_element_by_id("os_password")
        loginButton_xpath = driver.find_element_by_id("loginButton")

        username_xpath.send_keys(username)
        password_xpath.send_keys(password)
        loginButton_xpath.click()

        timeout = 5
        try:
            element_present = EC.presence_of_element_located((By.ID, 'title-text'))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        finally:
            print("Page loaded")

        tlist = []
        # tlist.append(["device type","customer","tag name", "version xpath", "tag name xpath"])
        # tlist.append(["TAG", "VERSION", "MATCH"])
        tlist.append(["TAG", "VERSION"])
        for row in self.xpath:
            if device_m == row[0] and customer_m == row[1]:
                # device = row[0]
                # customer = row[1]
                tag = row[2]
                version_xpath = row[3]
                tag_xpath = row[4]
                ver = driver.find_element_by_xpath(version_xpath).text
                # match_ver = driver.find_element_by_xpath(tag_xpath).text

                # ilist = [tag,self.extractVersion(ver),str(match_ver==tag)]
                ilist = [tag, self.extractVersion(ver)]
                tlist.append(ilist)

        table = Texttable()
        table.set_deco(Texttable.HEADER)
        # table.set_cols_dtype(['t', 't', 't']) # text
        # table.set_cols_width([45,15,5])
        table.set_cols_dtype(['t', 't']) # text
        table.set_cols_width([45,15])

        # table.set_cols_align(["l", "l", "l"])
        table.set_cols_align(["l", "l"])
        table.add_rows(tlist)
        print (table.draw())

        driver.quit()

        return tlist


