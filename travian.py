from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

def main():
    driver = webdriver.Chrome('chromedriver.exe')

    driver.get("SERVER URL/dorf1.php")
    #elem = driver.find_element_by_class_name('notNow level colorLayer gid4 buildingSlot13  level2')
    userName = driver.find_element_by_name("name")

    userName.send_keys("USERNAME")
    password = driver.find_element_by_name("password")

    password.send_keys("PASSWORD")
    login = driver.find_elements_by_id("s1")

    time.sleep(1)
    password.send_keys(Keys.ENTER)

    felidUpgradesSecoundVelig(driver)

def bulidingUpgrades(driver):
    woodValue = 0
    clayValue = 0 
    ironValue = 0
    cropValue = 0
    woodPath = '/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/a[1]/div[1]'
    clayPath = '/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/a[2]/div[1]'
    ironPath = '/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/a[3]/div[1]'
    cropPath = '/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[2]/a[1]/div[1]'


    numberOfFeildDone = 0
    start = True
    while True:
        driver.refresh()
        if driver.current_url == 'SERVER URL/login.php':
            userName = driver.find_element_by_name("name")

            userName.send_keys("USERNAME")
            password = driver.find_element_by_name("password")

            password.send_keys("PASSWORD")
            login = driver.find_elements_by_id("s1")

            time.sleep(1)
            password.send_keys(Keys.ENTER)
        if driver.current_url != 'SERVER URL/dorf2.php':
            driver.get('SERVER URL/dorf2.php')
            print('url chabged')
            
        if start:
            try:
                
                timer = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[2]/div[10]/ul/li/div[2]/span'        
                elem = driver.find_element_by_xpath(timer)
                
                timeLEft = elem.get_attribute('innerHTML')  
                print(timeLEft)
                x = sum(x * int(t) for x, t in zip([3600, 60, 1], timeLEft.split(":"))) 
                print('there is a building it will take  ' , x , 'sec') 
                print('not firest :) ')
                start = False
                time.sleep((x+10))
                
            except Exception:
                print('it is firest')
            

        levels = []
        paths = []
        clicked = False
        woodValue = driver.find_element_by_xpath(woodPath).get_attribute('innerHTML')
        clayValue = driver.find_element_by_xpath(clayPath).get_attribute('innerHTML')
        ironValue = driver.find_element_by_xpath(ironPath).get_attribute('innerHTML')
        cropValue = driver.find_element_by_xpath(cropPath).get_attribute('innerHTML')

        wo = float(woodValue) * 1000
        cl = float(clayValue) * 1000
        ir = float(ironValue)  * 1000
        cr = float(cropValue)   * 1000


        lowerLvl = 100
        chosenPath = ''
        cropFeilsList = [2,8,9,12,13,15]

        for c in range(1 , 19):
            if c not in cropFeilsList:

                path = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div['+str(c)+']/div'
                felid = driver.find_element_by_xpath(path)
                felidChosen = felid.get_attribute('innerHTML')
                levels.append(int(felidChosen))
                paths.append(path)
                if lowerLvl > int(felidChosen):            
                    lowerLvl = int(felidChosen)
                    chosenPath = path

        swapped = True
        while swapped:
            swapped = False
            for i in range(len(levels) - 1):
                if levels[i] > levels[i + 1]:
                    # Swap the elements
                    levels[i], levels[i + 1] = levels[i + 1], levels[i]
                    paths[i], paths[i + 1] = paths[i + 1], paths[i]
                    # Set the flag to True so we'll loop again
                    swapped = True

        #print(levels)
        #print(paths)

        for p in paths :
            

            elem = driver.find_element_by_xpath(p)
            elem.click()
            # to cheak if we have enof resoses we klick else to get aother one
            tempWood = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/span'
            tempClay = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/span'            
            tempIron = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/span'
            tempCrop = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[4]/span'

            tempWood = driver.find_element_by_xpath(tempWood).get_attribute('innerHTML')
            tempClay = driver.find_element_by_xpath(tempClay).get_attribute('innerHTML')
            tempIron = driver.find_element_by_xpath(tempIron).get_attribute('innerHTML')
            tempCrop = driver.find_element_by_xpath(tempCrop).get_attribute('innerHTML')
            print(wo)
            print(cl)
            print(ir)
            print(cr)
            print(int(tempWood) <= wo and int(tempClay) <= cl and int(tempIron) <= ir and int(tempCrop) <= cr)
            if int(tempWood) <= wo and int(tempClay) <= cl and int(tempIron) <= ir and int(tempCrop) <= cr:      
            
                elem = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[3]/div[2]/button')
                try:
                    elem.click()

                except Exception:
                    print('got error sleep for 10 sec')
                    time.sleep(10)    
                print('clicked') 
                time.sleep(40)
                clicked = True
                numberOfFeildDone +=1
                print('we completed ' , numberOfFeildDone , ' we start at 6:21')
                break
            driver.back()

        if clicked:      
            timer = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[2]/div[10]/ul/li/div[2]/span'        
            elem = driver.find_element_by_xpath(timer)
            
            timeLEft = elem.get_attribute('innerHTML')  
            print(timeLEft)
            x = sum(x * int(t) for x, t in zip([3600, 60, 1], timeLEft.split(":"))) 
            print('we will sleeo fo ' , x , 'sec') 
            time.sleep((x+10))
        else:
            print('sleeping for an houre')
            time.sleep(3600)
                

    print("done")
    driver.quit
    
def trainTrops(driver):
    url = 'SERVER URL/build.php?id=30'
    totalTraind = 0
    while True:
        driver.refresh()
        if driver.current_url == 'SERVER URL/login.php':
            userName = driver.find_element_by_name("name")

            userName.send_keys("USERNAME")
            password = driver.find_element_by_name("password")

            password.send_keys("PASSWORD")
            login = driver.find_elements_by_id("s1")

            time.sleep(1)
            password.send_keys(Keys.ENTER)
        if driver.current_url != url:
            driver.get(url)
            print('url chabged')
               
        path = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/form/div/div[1]/div[1]/div/div[2]/div[4]/a'   
        numberOFTropsToTrain = driver.find_element_by_xpath(path).get_attribute('innerHTML')
        
        totalTraind += int(numberOFTropsToTrain)

        trainFelid = driver.find_element_by_name("t1")
        trainFelid.send_keys(numberOFTropsToTrain)
        trainFelid.send_keys(Keys.ENTER)
        print("we traind " , totalTraind , 'so far')
        currentDT = datetime.datetime.now()
        print (currentDT.strftime("%H:%M:%S"))
        time.sleep(3600)     
    
        

def upgradTheBuliding(driver , p):
    woodValue = 0
    clayValue = 0 
    ironValue = 0
    cropValue = 0
    woodPath = '/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/a[1]/div[1]'
    clayPath = '/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/a[2]/div[1]'
    ironPath = '/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/a[3]/div[1]'
    cropPath = '/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[2]/a[1]/div[1]'


    numberOfFeildDone = 0
    start = True
    while True:
        driver.refresh()
        if driver.current_url == 'SERVER URL/login.php':
            userName = driver.find_element_by_name("name")

            userName.send_keys("USERNAME")
            password = driver.find_element_by_name("password")

            password.send_keys("PASSWORD")
            login = driver.find_elements_by_id("s1")

            time.sleep(1)
            password.send_keys(Keys.ENTER)
        if driver.current_url != 'SERVER URL/dorf1.php?newdid=15096&':
            driver.get('SERVER URL/dorf2.php')
            driver.get('SERVER URL/dorf2.php')
            print('url chabged')
            
        if start:
            try:
                
                timer = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[2]/div[10]/ul/li/div[2]/span'        
                elem = driver.find_element_by_xpath(timer)
                
                timeLEft = elem.get_attribute('innerHTML')  
                print(timeLEft)
                x = sum(x * int(t) for x, t in zip([3600, 60, 1], timeLEft.split(":"))) 
                print('there is a building it will take  ' , x , 'sec') 
                print('not firest :) ')
                start = False
                time.sleep((x+10))
                
            except Exception:
                print('it is firest')
            
        woodValue = driver.find_element_by_xpath(woodPath).get_attribute('innerHTML')
        clayValue = driver.find_element_by_xpath(clayPath).get_attribute('innerHTML')
        ironValue = driver.find_element_by_xpath(ironPath).get_attribute('innerHTML')
        cropValue = driver.find_element_by_xpath(cropPath).get_attribute('innerHTML')

        wo = float(woodValue) * 1000
        cl = float(clayValue) * 1000
        ir = float(ironValue)  * 1000
        cr = float(cropValue)   * 1000


        #p = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div/div[19]/div/div'
        elem = driver.find_element_by_xpath(p)
        elem.click()
        # to cheak if we have enof resoses we klick else to get aother one
        tempWood = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[3]/div[3]/div[1]/div[1]/div[1]/span'
        tempClay = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[3]/div[3]/div[1]/div[1]/div[2]/span'      
        tempIron = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[3]/div[3]/div[1]/div[1]/div[3]/span'
        tempCrop = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[3]/div[3]/div[1]/div[1]/div[4]/span'

        tempWood = driver.find_element_by_xpath(tempWood).get_attribute('innerHTML')
        tempClay = driver.find_element_by_xpath(tempClay).get_attribute('innerHTML')
        tempIron = driver.find_element_by_xpath(tempIron).get_attribute('innerHTML')
        tempCrop = driver.find_element_by_xpath(tempCrop).get_attribute('innerHTML')
        print(wo)
        print(cl)
        print(ir)
        print(cr)
        print(int(tempWood) <= wo and int(tempClay) <= cl and int(tempIron) <= ir and int(tempCrop) <= cr)
        if int(tempWood) <= wo and int(tempClay) <= cl and int(tempIron) <= ir and int(tempCrop) <= cr:      
            print('we have resusres to bulid')
                                                
            elem = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[3]/div[3]/div[3]/div[1]/button')
            try:
                elem.click()
            except Exception:
                print('got error sleep for 10 sec')
                time.sleep(10)    
            print('clicked') 
            time.sleep(40)
            clicked = True
            numberOfFeildDone +=1
            print('we completed ' , numberOfFeildDone )
        if clicked:      
            timer = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[2]/div[10]/ul/li/div[2]/span'        
            elem = driver.find_element_by_xpath(timer)
            
            timeLEft = elem.get_attribute('innerHTML')  
            print(timeLEft)
            x = sum(x * int(t) for x, t in zip([3600, 60, 1], timeLEft.split(":"))) 
            print('we will sleeo for ' , x , 'sec') 
            time.sleep((x+10))
        if numberOfFeildDone >= 1:
            break    
        else:
            #print('sleeping for an houre')
            #time.sleep(3600)  
            break  
            

def felidUpgrades(driver):
    woodValue = 0
    clayValue = 0 
    ironValue = 0
    cropValue = 0
    woodPath = '/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/a[1]/div[1]'
    clayPath = '/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/a[2]/div[1]'
    ironPath = '/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/a[3]/div[1]'
    cropPath = '/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[2]/a[1]/div[1]'


    numberOfFeildDone = 0
    start = True
    on = 1
    while True:
        driver.refresh()
        if driver.current_url == 'SERVER URL/login.php':
            userName = driver.find_element_by_name("name")

            userName.send_keys("USERNAME")
            password = driver.find_element_by_name("password")

            password.send_keys("PASSWORD")
            login = driver.find_elements_by_id("s1")

            time.sleep(1)
            password.send_keys(Keys.ENTER)
        if driver.current_url != 'SERVER URL/dorf1.php':
            driver.get('SERVER URL/dorf1.php')
            print('url chabged')
            
        if start:
            try:
                
                timer = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[2]/div[10]/ul/li/div[2]/span'        
                elem = driver.find_element_by_xpath(timer)
                
                timeLEft = elem.get_attribute('innerHTML')  
                print(timeLEft)
                x = sum(x * int(t) for x, t in zip([3600, 60, 1], timeLEft.split(":"))) 
                print('there is a building it will take  ' , x , 'sec') 
                print('not firest :) ')
                start = False
                time.sleep((x+10))
                
            except Exception:
                print('it is firest')
            

        levels = []
        paths = []
        clicked = False
        woodValue = driver.find_element_by_xpath(woodPath).get_attribute('innerHTML')
        clayValue = driver.find_element_by_xpath(clayPath).get_attribute('innerHTML')
        ironValue = driver.find_element_by_xpath(ironPath).get_attribute('innerHTML')
        cropValue = driver.find_element_by_xpath(cropPath).get_attribute('innerHTML')

        wo = float(woodValue) * 1000
        cl = float(clayValue) * 1000
        ir = float(ironValue)  * 1000
        cr = float(cropValue)   * 1000


        lowerLvl = 100
        chosenPath = ''
        cropFeilsList = [2,8,9,12,13,15]

        for c in range(1 , 19):
            if c not in cropFeilsList:
                path = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div['+str(c)+']/div'
                felid = driver.find_element_by_xpath(path)
                felidChosen = felid.get_attribute('innerHTML')
                levels.append(int(felidChosen))
                paths.append(path)
                if lowerLvl > int(felidChosen):            
                    lowerLvl = int(felidChosen)
                    chosenPath = path

        swapped = True
        while swapped:
            swapped = False
            for i in range(len(levels) - 1):
                if levels[i] > levels[i + 1]:
                    # Swap the elements
                    levels[i], levels[i + 1] = levels[i + 1], levels[i]
                    paths[i], paths[i + 1] = paths[i + 1], paths[i]
                    # Set the flag to True so we'll loop again
                    swapped = True

        #print(levels)
        #print(paths)

        for p in paths :
            

            elem = driver.find_element_by_xpath(p)
            elem.click()
            # to cheak if we have enof resoses we klick else to get aother one
            tempWood = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/span'
            tempClay = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/span'            
            tempIron = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/span'
            tempCrop = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[4]/span'

            tempWood = driver.find_element_by_xpath(tempWood).get_attribute('innerHTML')
            tempClay = driver.find_element_by_xpath(tempClay).get_attribute('innerHTML')
            tempIron = driver.find_element_by_xpath(tempIron).get_attribute('innerHTML')
            tempCrop = driver.find_element_by_xpath(tempCrop).get_attribute('innerHTML')
            print(wo)
            print(cl)
            print(ir)
            print(cr)
            print(int(tempWood) <= wo and int(tempClay) <= cl and int(tempIron) <= ir and int(tempCrop) <= cr)
            if int(tempWood) <= wo and int(tempClay) <= cl and int(tempIron) <= ir and int(tempCrop) <= cr:      
            
                elem = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[3]/div[2]/button')
                try:
                    elem.click()

                except Exception:
                    print('got error sleep for 10 sec')
                    time.sleep(10)    
                print('clicked') 
                time.sleep(40)
                clicked = True
                numberOfFeildDone +=1
                print('we completed ' , numberOfFeildDone , ' we start at 6:21')
                break
            driver.back()

        if clicked:      
            timer = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[2]/div[10]/ul/li/div[2]/span'        
            elem = driver.find_element_by_xpath(timer)
            
            timeLEft = elem.get_attribute('innerHTML')  
            print(timeLEft)
            x = sum(x * int(t) for x, t in zip([3600, 60, 1], timeLEft.split(":"))) 
            print('we will sleeo fo ' , x , 'sec') 
            time.sleep((x+10))

        if numberOfFeildDone % 18 == 0:
            p1 = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div/div[26]/div/div'
            p2 = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div/div[24]/div/div'
            p3 = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div/div[28]/div/div'
            if on == 1:
                upgradTheBuliding(driver , p1)
                on +=1 
            elif on == 2:
                upgradTheBuliding(driver , p2)  
                on +=1 
            else:
                upgradTheBuliding(driver , p3) 
                on = 1  

        else:
            print('sleeping for an houre')
            time.sleep(3600)
                

    print("done")
    driver.quit

def felidUpgradesSecoundVelig(driver):
    woodValue = 0
    clayValue = 0 
    ironValue = 0
    cropValue = 0
    woodPath = '/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/a[1]/div[1]'
    clayPath = '/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/a[2]/div[1]'
    ironPath = '/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[1]/a[3]/div[1]'
    cropPath = '/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div[2]/a[1]/div[1]'


    numberOfFeildDone = 0
    start = True
    on = 1
    while True:
        driver.refresh()
        if driver.current_url == 'SERVER URL/login.php':
            userName = driver.find_element_by_name("name")

            userName.send_keys("USERNAME")
            password = driver.find_element_by_name("password")

            password.send_keys("PASSWORD")
            login = driver.find_elements_by_id("s1")

            time.sleep(1)
            password.send_keys(Keys.ENTER)
        if driver.current_url != 'SERVER URL/dorf1.php?newdid=15096&':
            driver.get('SERVER URL/dorf1.php?newdid=15096&')
            print('url chabged')
            
        if start:
            try:
                
                timer = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[2]/div[10]/ul/li/div[2]/span'        
                elem = driver.find_element_by_xpath(timer)
                
                timeLEft = elem.get_attribute('innerHTML')  
                print(timeLEft)
                x = sum(x * int(t) for x, t in zip([3600, 60, 1], timeLEft.split(":"))) 
                print('there is a building it will take  ' , x , 'sec') 
                print('not firest :) ')
                start = False
                time.sleep((x+10))
                
            except Exception:
                print('it is firest')
            

        levels = []
        paths = []
        clicked = False
        woodValue = driver.find_element_by_xpath(woodPath).get_attribute('innerHTML')
        clayValue = driver.find_element_by_xpath(clayPath).get_attribute('innerHTML')
        ironValue = driver.find_element_by_xpath(ironPath).get_attribute('innerHTML')
        cropValue = driver.find_element_by_xpath(cropPath).get_attribute('innerHTML')

        wo = float(woodValue) * 1000
        cl = float(clayValue) * 1000
        ir = float(ironValue)  * 1000
        cr = float(cropValue)   * 1000


        lowerLvl = 100
        chosenPath = ''
        cropFeilsList = [1,2,4,5,8,9,12,13,15]
        #cropFeilsList = [1]
        for c in range(1 , 19):
            if c not in cropFeilsList:
                
                path = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div['+str(c)+']/div'
                felid = driver.find_element_by_xpath(path)
                felidChosen = felid.get_attribute('innerHTML')
                levels.append(int(felidChosen))
                paths.append(path)
                #if lowerLvl > int(felidChosen):            
                 #   lowerLvl = int(felidChosen)
                  #  chosenPath = path

        swapped = True
        while swapped:
            swapped = False
            for i in range(len(levels) - 1):
                if levels[i] > levels[i + 1]:
                    # Swap the elements
                    levels[i], levels[i + 1] = levels[i + 1], levels[i]
                    paths[i], paths[i + 1] = paths[i + 1], paths[i]
                    # Set the flag to True so we'll loop again
                    swapped = True

        #print(levels)
        #print(paths)

        for p in paths :
            

            elem = driver.find_element_by_xpath(p)
            elem.click()
            # to cheak if we have enof resoses we klick else to get aother one
            tempWood = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/span'
            tempClay = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/span'            
            tempIron = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/span'
            tempCrop = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[4]/span'

            tempWood = driver.find_element_by_xpath(tempWood).get_attribute('innerHTML')
            tempClay = driver.find_element_by_xpath(tempClay).get_attribute('innerHTML')
            tempIron = driver.find_element_by_xpath(tempIron).get_attribute('innerHTML')
            tempCrop = driver.find_element_by_xpath(tempCrop).get_attribute('innerHTML')
            print(wo)
            print(cl)
            print(ir)
            print(cr)
            print(int(tempWood) <= wo and int(tempClay) <= cl and int(tempIron) <= ir and int(tempCrop) <= cr)
            if int(tempWood) <= wo and int(tempClay) <= cl and int(tempIron) <= ir and int(tempCrop) <= cr:      
            
                elem = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[1]/div[3]/div[3]/div[2]/button')
                try:
                    elem.click()
                    print('clicked') 
                    time.sleep(40)
                    clicked = True
                    numberOfFeildDone +=1
                    print('we completed ' , numberOfFeildDone , ' start at 4:50 ' )
                    break

                except Exception:
                    print('got error sleep for 10 sec')
                    time.sleep(10)    
                
            driver.back()

        if clicked:      
            print('in clicked')
            while clicked:
                try:
                    driver.get('SERVER URL/dorf1.php?newdid=15096&')
                    timer = '/html/body/div[3]/div[4]/div[1]/div[2]/div[3]/div[1]/div[2]/div[10]/ul/li/div[2]/span'        
                    elem = driver.find_element_by_xpath(timer)
                    
                    timeLEft = elem.get_attribute('innerHTML')  
                    print(timeLEft)
                    x = sum(x * int(t) for x, t in zip([3600, 60, 1], timeLEft.split(":"))) 
                    print('we will sleeo fo ' , x , 'sec') 
                    time.sleep((x+10))
                    clicked = False
                except Exception:
                    driver.refresh()
                    
                    if driver.current_url == 'SERVER URL/login.php':
                        userName = driver.find_element_by_name("name")

                        userName.send_keys("USERNAME")
                        password = driver.find_element_by_name("password")

                        password.send_keys("PASSWORD")
                        login = driver.find_elements_by_id("s1")

                        time.sleep(1)
                        password.send_keys(Keys.ENTER)
                    if driver.current_url != 'SERVER URL/dorf1.php?newdid=15096&':
                        driver.get('SERVER URL/dorf1.php?newdid=15096&')
                        print('url chabged')
                    time.sleep(10)    

         


        else:
            print('sleeping for an 10 m')
            time.sleep(600)
                

    print("done")
    driver.quit


main()

