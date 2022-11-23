from selenium import webdriver
import time
from selenium.webdriver.common.by import By

testLINK="https://www.instagram.com/_teri.lau/"
def AutoLogin(driver):
    user="Noir_2357"
    pw="somnium8947"
    # driver.find_element(by=By.XPATH, value="// input[@name='username']").send_keys(user)
    # driver.find_element(by=By.XPATH, value="// input[@name='password']").send_keys(pw)
    driver.find_element(by=By.XPATH, value="// input[@name='username']").send_keys(user)
    driver.find_element(by=By.XPATH, value="// input[@name='password']").send_keys(pw)
#     driver.find_element_by_css_selector('._ab8w._ab94._ab99._ab9f._ab9m._ab9p._abcm').click()
    # driver.find_element(by=By.XPATH, value="// div[contains(text(),\'Log in')]").click()
    driver.find_element(by=By.XPATH, value="// div[contains(text(),\'Log in')]").click()
def getFollowerNum(driver):
    
    followerDiv=driver.find_element(by=By.XPATH, value="// div[contains(text(),\'followers')]")
    print("yes")
    followerNo=followerDiv.find_element(By.TAG_NAME, "span").text
#     print(len(followerNo))
    Num=followerNo
    print(Num)
    followerDiv.click()
    return Num

def scrollDown(driver,Num):
    time.sleep(3)
    element=driver.find_element(By.CLASS_NAME, 'isgrP')

    verical_ordinate = 1000
    for i in range(0, round(int(Num)/10)):
        print(verical_ordinate)
        driver.execute_script("arguments[0].scrollTop = arguments[1]", element, verical_ordinate)
        verical_ordinate += 1000
        time.sleep(1)
        
def getLinks(driver,url):
    
    elems=driver.find_elements(By.CSS_SELECTOR, '.notranslate._0imsa')
    links = [elem.get_attribute('href') for elem in elems]
    printLinks(links)
    return links
    
def printLinks(links):
    for link in links:
        print (link)
    print("Total target users number:"+str(len(links)))


def sendmsg(msg,driver,links):
    for link in links:
        driver.get(link)
        time.sleep(2)
        driver.find_element(by=By.XPATH, value="// div[contains(text(),\'Message')]").click()
        time.sleep(2)
        driver.find_element(by=By.XPATH, value="// button[contains(text(),\'Not Now')]").click()
        time.sleep(2)
        contenttosent=msg
        contentspace=driver.find_element(by=By.XPATH, value="// textarea[@placeholder='Message...']")
        contentspace.send_keys(contenttosent)
        driver.find_element(by=By.XPATH, value="// button[contains(text(),\'Send')]").click()
    print("Finish sending all messages")

def sendmsgTest(driver):
    link="https://www.instagram.com/hh.w__/"
    driver.get(link)
    time.sleep(2)
    driver.find_element(by=By.XPATH, value="// div[contains(text(),\'Message')]").click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value="// button[contains(text(),\'Not Now')]").click()
    time.sleep(2)
    contenttosent="唔買保險我叫林作請你食tamjai啊---來自自動回復程式"
    contentspace=driver.find_element(by=By.XPATH, value="// textarea[@placeholder='Message...']")
    contentspace.send_keys(contenttosent)
    driver.find_element(by=By.XPATH, value="// button[contains(text(),\'Send')]").click()
    print("Finish sending all messages")
    
def main():
    print("--------------------------------------------------------------------------------------")
    print("Hello Welcome to ColdCall 神器")
    input("Press Enter to continue...")
    print("--------------------------------------------------------------------------------------")
    # driver = webdriver.Chrome()
    
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})
    driver_url = "chromedriver.exe"
    driver=webdriver.Chrome(executable_path=driver_url,chrome_options=options)
    driver.maximize_window()
    driver.get("https://www.instagram.com")
    time.sleep(3)
    AutoLogin(driver)
    time.sleep(3)
    sendmsgTest(driver)###
    print("DONE, YOU ARE SUCH A LAZY ASS")
    return###
    print("--------------------------------------------------------------------------------------")
    print("Please Log into IG, then enter the url of the page of followers you want to send msg to")
    print("--------------------------------------------------------------------------------------")
    url = input("Enter URL:")
    # urls="hhh"
    print("--------------------------------------------------------------------------------------")
    print("The URL is:")
    print(url)
    print("--------------------------------------------------------------------------------------")
    input("Press Enter to continue...")
    print("--------------------------------------------------------------------------------------")
    driver.get(url)
    input("Press Enter to continue...")
    print("--------------------------------------------------------------------------------------")
    num=getFollowerNum(driver)
    scrollDown(driver,num)
    links=getLinks(driver,url)

    print("--------------------------------------------------------------------------------------")
    msg = input("Please enter the message you want to send:/n")
    print("Are u sure you are going to send the following?")
    print(msg)
    print("--------------------------------------------------------------------------------------")

    yes_choices = ['yes', 'y']
    no_choices = ['no', 'n']

    while True:
        print("--------------------------------------------------------------------------------------")
        user_input = input('Are u sure you are going to send (THICK TWICE!!! NO RETURN !!!) (yes/no): ')
        if user_input.lower() in yes_choices:
            # sendmsg(msg,driver,links)
            sendmsgTest(msg,driver,links)
            print("Send Jor")
            break
        elif user_input.lower() in no_choices:
            print("--------------------------------------------------------------------------------------")
            msg = input("Please enter the message you want to send")
            print("Are u sure you are going to send the following?")
            print(msg)
            continue
        else:
            print('Type yes or no')
            continue
    print("--------------------------------------------------------------------------------------")
    print("DONE, YOU ARE SUCH A LAZY ASS")
    

if __name__ == "__main__":
    main()