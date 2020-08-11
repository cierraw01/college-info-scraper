import requests
import csv
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

URL = "https://nces.ed.gov/collegenavigator/"
page = requests.get(URL)

options = Options()
options.add_argument("--window-size=1920,1200")

driver_path = "\\Users\\patri\\Downloads\\chromedriver_win32 (1)\\chromedriver"
driver = webdriver.Chrome(options=options, executable_path=driver_path)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="default")

colleges_list = ["Stanford", "Harvard", "University of Texas at Austin", "Rice University",
                 "Howard University", "Texas State University", "Rensselaer Polytechnic Institute",
                 "University of California-Berkeley", "University of California-Los Angeles",
                 "Dartmouth College", "Cornell University", "Columbia University in the City of New York",
                 "Neumont", "Purdue University-Main Campus", "Massachusetts Institute of Technology",
                 "Duke University", "University of Pennsylvania", "University of Southern California",
                 "Vanderbilt University", "Worcester Polytechnic Institute", "University of California-Irvine",
                 "Northwestern University", "California Polytechnic State University", "University of California-Santa Cruz",
                 "University of California-Davis", "University of Massachusetts Amherst", "Harvey Mudd College",
                 "University of Rochester", "University of Pittsburgh-Pittsburgh Campus", "University of Hawaii at Manoa",
                 "Hawaii Pacific University", "California State University Northridge", "California State University Long Beach",
                 "University of North Texas", "University of Texas at San Antonio", "Brown University", 
                 "University of Colorado Boulder", "Colorado School of Mines", "University of Washington-Seattle",
                 "Washington University in St. Louis", "Rochester Institute of Technology", "Carnegie Mellon"]

for_csv = []

for college in colleges_list:
    
    our_price, acceptance_rate, RnW25, RnW75, M25, M75 = "", "", "", "", "", ""
    
    driver.get(URL)
    search_bar = driver.find_element_by_id("ctl00_cphCollegeNavBody_ucSearchMain_txtName")
    search_bar.send_keys(f"{college}\n")
    time.sleep(1)
    
    school_name = driver.find_element_by_xpath('//*[@id="ctl00_cphCollegeNavBody_ucResultsMain_tblResults"]/tbody/tr/td[2]/a')
    school_name_str = school_name.text
    loc = driver.find_element_by_xpath('//*[@id="ctl00_cphCollegeNavBody_ucResultsMain_tblResults"]/tbody/tr/td[2]').text
    if (college == "Howard University" or college == "Texas State University" or college == "University of Rochester"):
        school_name = driver.find_element_by_xpath('//*[@id="ctl00_cphCollegeNavBody_ucResultsMain_tblResults"]/tbody/tr[2]/td[2]/a')
        school_name_str = school_name.text
        loc = driver.find_element_by_xpath('//*[@id="ctl00_cphCollegeNavBody_ucResultsMain_tblResults"]/tbody/tr[2]/td[2]').text
    elif (college == "University of Pennsylvania"):
        next_page = driver.find_element_by_xpath('//*[@id="ctl00_cphCollegeNavBody_ucResultsMain_divPagingControls"]/div/a')
        next_page.click()
        time.sleep(1)
        school_name = driver.find_element_by_xpath('//*[@id="ctl00_cphCollegeNavBody_ucResultsMain_tblResults"]/tbody/tr[1]/td[2]/a')
        school_name_str = school_name.text
        loc = driver.find_element_by_xpath('//*[@id="ctl00_cphCollegeNavBody_ucResultsMain_tblResults"]/tbody/tr[1]/td[2]').text
    elif (college == "Northwestern University"):
        school_name = driver.find_element_by_xpath('//*[@id="ctl00_cphCollegeNavBody_ucResultsMain_tblResults"]/tbody/tr[5]/td[2]/a')
        school_name_str = school_name.text
        loc = driver.find_element_by_xpath('//*[@id="ctl00_cphCollegeNavBody_ucResultsMain_tblResults"]/tbody/tr[5]/td[2]').text
    elif (college == "University of Southern California"):
        school_name = driver.find_element_by_xpath('//*[@id="ctl00_cphCollegeNavBody_ucResultsMain_tblResults"]/tbody/tr[3]/td[2]/a')
        school_name_str = school_name.text
        loc = driver.find_element_by_xpath('//*[@id="ctl00_cphCollegeNavBody_ucResultsMain_tblResults"]/tbody/tr[3]/td[2]').text       
##    elif (college == "Columbia University"):
##        school_name = driver.find_element_by_xpath('//*[@id="ctl00_cphCollegeNavBody_ucResultsMain_tblResults"]/tbody/tr[5]/td[2]/a')
##        school_name_str = school_name.text
##        loc = driver.find_element_by_xpath('//*[@id="ctl00_cphCollegeNavBody_ucResultsMain_tblResults"]/tbody/tr[5]/td[2]').text        
    school_name.click()
    time.sleep(1)
    
    school_website = driver.find_element_by_xpath('//*[@id="RightContent"]/div[4]/div/div[2]/table/tbody/tr[2]/td[2]/a').text
    school_type = driver.find_element_by_xpath('//*[@id="RightContent"]/div[4]/div/div[2]/table/tbody/tr[3]/td[2]').text
    city_size = driver.find_element_by_xpath('//*[@id="RightContent"]/div[4]/div/div[2]/table/tbody/tr[5]/td[2]').text
    
    price = driver.find_element_by_xpath('//*[@id="netprc"]/div[1]')
    price.click()
    time.sleep(1)
    try:
        our_price = driver.find_element_by_xpath('//*[@id="divctl00_cphCollegeNavBody_ucInstitutionMain_ctl02"]/div/table[2]/tbody/tr[5]/td[4]').text
    except:
        pass
    admissions = driver.find_element_by_xpath('//*[@id="admsns"]/div[1]')
    admissions.click()
    time.sleep(1)
    try:
        acceptance_rate = driver.find_element_by_xpath('//*[@id="divctl00_cphCollegeNavBody_ucInstitutionMain_ctl04"]/div/table[2]/tbody/tr[2]/td[2]').text
    except:
        pass
    try:
        RnW25 = driver.find_element_by_xpath('//*[@id="divctl00_cphCollegeNavBody_ucInstitutionMain_ctl04"]/div/table[5]/tbody/tr[1]/td[2]').text
        RnW75 = driver.find_element_by_xpath('//*[@id="divctl00_cphCollegeNavBody_ucInstitutionMain_ctl04"]/div/table[5]/tbody/tr[1]/td[3]').text
        M25 = driver.find_element_by_xpath('//*[@id="divctl00_cphCollegeNavBody_ucInstitutionMain_ctl04"]/div/table[5]/tbody/tr[2]/td[2]').text
        M75 = driver.find_element_by_xpath('//*[@id="divctl00_cphCollegeNavBody_ucInstitutionMain_ctl04"]/div/table[5]/tbody/tr[2]/td[3]').text
    except:
        pass

    chance = ""
    try:
        if (int(RnW25) > 720 or int(M25) > 640):
            chance = "Reach"
            rate = acceptance_rate[:-1]
            if(int(rate)<16):
                chance = "Wildcard"
        elif (int(RnW75) < 720 and int(M75) < 640):
            chance = "Safety"
        else:
            chance = "Target"
    except:
        pass

    loc_list = loc.splitlines()
    location = loc_list[1]
    
    college_dict = {"name": school_name_str, "chance": chance, "website": school_website, "type": school_type,
                    "location": location, "city size": city_size, "acceptance rate": acceptance_rate, "price": our_price,
                    "separator": "-", "reading25": RnW25, "reading75": RnW75, "math25": M25, "math75": M75}
    for_csv.append(college_dict)
    
    print(f"{school_name_str}: {chance}")
    print(f"{school_website}")
    print(f"{school_type}")
    print(f"Location: {location}")
    print(f"{city_size}")
    print(f"Acceptance Rate: {acceptance_rate}")
    print(f"Expected Net Price: {our_price}")
    print(f"Reading and Writing: {RnW25}-{RnW75}")
    print(f"Math: {M25}-{M75}")
    print("")
    
driver.quit()

with open('colleges_file.csv',mode="w") as colleges_file:
    colleges_writer = csv.writer(colleges_file, delimiter=",", quotechar='"', lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
    for c in for_csv:
        colleges_writer.writerow([c["name"],c["chance"],c["website"],
        c["type"],c["location"],c["city size"],c["acceptance rate"],
        c["price"],c["reading25"],c["separator"],c["reading75"],
        c["math25"],c["separator"],c["math75"]])




