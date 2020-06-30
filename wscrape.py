from selenium import webdriver
import pprint
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
import numpy as np

list = [84,26,2,71,27,74,79,28,69,30,66,67,31,3,77,70,82,32,33,10,34,72,59,56,40,35,36,89,78,38,39,95,73,6,4,5,65,7,41,42,29,8,64,63,93,9,12,94,43,25,91,44,13,80,83,85,37,16,90,45,68,61,14,15,46,49,50,47,19,17,18,86,75,1,81,87,21,22,88,23,60,62,92,51,52,53,76,54]

list2 = ['Aarey Colony Goregaon(E)', 'Andheri Fire Stn', 'B Ward Office', 'BKC Navdadeep Park', 'Bandra Fire Station', 'Bandra Reclaimation', 'Bhandarwada Reservior', 'Bhandup Complex', 'Bhandup IMD Raingauge', 'Borivali Fire Station', 'Britania storm water pumping', 'Building Proposal office Vikhroli (W)', 'Byculla Fire Station', 'C Ward Office', 'CTI   Borivali (E)', 'Chakala Andheri (E)', 'Charkop', 'Chembur Fire Station', 'Chincholi Fire Station', 'City Institute of DM', 'Colaba Fire Station', 'Colaba Navy Nagar', 'Colaba Pumping Station', 'Cooper Hospital', 'D Ward Office', 'Dadar Fire Station', 'Dahisar Fire Station', 'Datt Kripa Prabodhini', 'Deonar Chembur', 'Dharavi Fire Station', 'Dindoshi Fire Station', 'Dr C D Deshmukh Garden', 'Dump Yard  Kandivali (E)', 'Eye Hospital Grant Rd', 'F North Ward Office', 'F South Ward Office', 'Frosberry Reserviour', 'G South Ward Office', 'Gawanpada Fire Station', 'Goregaon', 'H East Ward Office', 'H West Ward Office', 'HBT Trauma Hospital', 'Haji Ali Pumping station', 'IIT Powai', 'K East Ward Office', 'K West Ward Office', 'Kalidas Natya Mulund West', 'Kandivali Fire Station', 'Kandivali Workshop', 'Khotwadi Santacruz (W)', 'Kurla Fire Station', 'L Ward Office', 'LBS Garden Worli', 'Lokhandwala Complex', 'Love Grove Station', 'M East Ward Office', 'M West Ward Office', 'MG Swimming Pool Dadar-W', 'Malad Fire Station', 'Malad IMD Raingauge', 'Malbar hill', 'Malwani Fire Stn', 'Mandavi Fire Stn', 'Marol Fire Station', 'Memonwada Fire Stn', 'Mulund Fire Station', 'Municipal Head Office 1', 'N Ward Office', 'Nair Hospital', 'Nariman Point Fire Stn', 'Nehru Science Centre Worli', 'Panvel', 'Prabodhankar Thackeray Natya Mandir', 'R South Kandivali West', 'Rajawadi Hospital', 'Rawali Camp', 'S Ward Office', 'SPS Garden Mulund West', 'SWD Workshop Dadar', 'SWM Santacruz Workshop', 'Versova pumping station', 'Vidyavihar (E)', 'Vikhroli Fire Station', 'Vile Parle Fire Stn', 'Wadala Fire Station', 'Wonders Park  Nerul', 'Worli Fire Station']

result = np.zeros([(len(list)),7])
for i in range(len(list)):
     result[i][0] = list[i]

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
url = 'http://dm.mcgm.gov.in/livefullpage'
driver.get(url)
while(1):
    time.sleep(5)
    for i in range(len(list)):
        Select(driver.find_element_by_id('menulistlocation')).select_by_value(str(int(result[i][0])))
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        out = soup.find(id = 'rain15min')
        result[i][1] = out.getText()
        out = soup.find(id = 'rain1hour')
        result[i][2] = out.getText()
        out = soup.find(id = 'rain3hour')
        result[i][3] = out.getText()
        out = soup.find(id = 'rain6hour')
        result[i][4] = out.getText()
        out = soup.find(id = 'rain12hour')
        result[i][5] = out.getText()
        out = soup.find(id = 'rain24hour')
        result[i][6] = out.getText()
        print(result[i][:])
        print(list2[i])
    time.sleep(90)
# list2 = ['Abhyudaya Nagar', 'Afghan Church', 'Andheri', 'Andheri (E)', 'Andheri (W)', 'Andheri Kurla Road', 'Andheri Rly Stn (W)', 'Bandra', 'Bandra (W)', 'Bhagwati Hospital', 'Bhaidas Auditarium', 'Bhandup (W)', 'Bhandup Complex', 'Bharatmata Cinema', 'Bhaucha Dhakka', 'Bhendi bazaar', 'Borivali Rly Stn','Borivli (W)', 'Breach Candy', 'Byculla Bridge', 'Byculla Rly Stn', 'CST Railway Stn', 'Century Bazar', 'Chembur', 'Chembur Naka', 'Chincholi Bunder', 'Coal Bandar', 'Colaba', 'Colaba Market', 'Cooper Hospital', 'Cuff Parade', 'Currey Road', 'DN Nagar Metro Stn', 'DN Road', 'Dadar (E)', 'Dahanukar Wadi', 'Dahisar', 'Dahisar Check Naka', 'Darukhana', 'Dava Bazar', 'Deepak Talkies', 'Deonar Municipal Colony', 'Dharavi', 'Diamond Garden', 'Dinanath Mangeshkar Natyagruha', 'Dindoshi', 'Dongri', 'Elphinston Road Rly Stn', 'Elphinstone  Road Rly Stn', 'Fort', 'Four Bungalow', 'GPO, Mumbai', 'GTB Rly Stn', 'Gandhi Market', 'Gawanpada', 'Ghatkopar (E)', 'Gokuldham', 'Goregaon (W)', 'Govandi', 'Grant Road', 'Grant Road Railway Stn', 'Haji Ali', 'Hill Road', 'Hindmata Cinema','IMD Colaba', 'INS Ashwini Hospital', 'ISCON Temple, Juhu', 'Jijamata Nagar', 'Jogeshwari Rly Stn', 'KEM Hospital', 'Kajupada', 'Kalbadevi Road', 'Kamala Nehru Park', 'Kandivali (W)','Kandivli Railway Stn', 'Kannamwar Nagar', 'Khindipada', 'Kings Circle', 'Kurla (W)', 'Kurla Bhabha Hospital', 'Kurla Kamani', 'Kurla Railway Station (W)', 'Lalbaug', 'Lamington Road', 'Liberty Garden', 'Lilawati Hospital', 'Mahalaxmi Mandir', 'Maharashtra Nagar', 'Mahim (E)', 'Malad', 'Malad Link Road', 'Malbar Hill', 'Malvani', 'Mandavi', 'Mankhurd', 'Mantralaya', 'Maratha Mandir', 'Marine Lines Rly Stn', 'Marol', 'Marve Beach', 'Masjid Bunder Rly Stn', 'Matunga', 'Memonwada', 'Metro Junction','Milan Subway', 'Milind Nagar, JVLR', 'Mithi Chowky Junction', 'Mulund (E)', 'Mulund (W)', 'Mulund Rly Stn', 'Mumbai Central', 'Mumbai Domestic Airport', 'Municipal Head Office', 'Nadkarni Park', 'Nair Hospital', 'Nana Chowk', 'Nana Jagannath Shankarshet Flyover', 'Nariman Point', 'Natraj Cinema', 'Nehru Science Centre', 'Parel Bhoiwada', 'Parel TT', 'Passport Office', 'Patkar College', 'Poisar', 'Powai', 'Powai Gardens', 'Prabhat Colony', 'Prabodhankar Natyagruha', 'Pratiksha Nagar', 'Priyadarshini Park', 'Rajawadi Hospital','Ram Mandir  Rly Stn', 'Reay Road', 'S V Road Malad (W)', 'Sakinaka', 'Sandhurst Road Rly Stn', 'Santacruz Rly Stn', 'Sarvoday Hospital', 'Sasmira Road', 'Sea Link Bandra', 'Senapati Bapat Marg', 'Sewri', 'Shatabdi Hospital Kandivli', 'Shiv Sagar Estate', 'Shivaji Nagar, JVLR', 'Sion Koliwada', 'Tagore Nagar', 'Thakur Complex', 'V N Desai Municipal Hospital', 'Vakola Police Station', 'Vashi Creek', 'Versova Village', 'Vidhan Bhavan', 'Vikhroli', 'Vikhroli Park Site', 'Vileparle Rly Stn (W)', 'Wadala', 'Walkeshwar', 'Worli', 'Worli Naka']
