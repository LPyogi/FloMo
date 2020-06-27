from selenium import webdriver
import pprint
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
import numpy as np
list = [170, 151, 58, 50, 57, 51, 56, 47, 44, 77, 138, 99, 105, 109, 9, 5, 75, 111, 165, 20, 19, 129, 33, 89, 92, 66, 171, 1, 2, 137, 141, 22, 160, 130, 40, 69, 79, 80, 172, 14, 35, 88, 38, 93, 146, 62, 7, 34, 42, 131, 161, 132, 29, 144, 101, 94, 63, 61, 87, 16, 113, 162, 46, 24, 149, 150, 139, 123, 166, 107, 82, 13, 157, 70, 125, 97, 106, 26, 100, 85, 81, 86, 21, 115, 65, 48, 163, 121, 39, 73, 67, 155, 117, 8, 148, 4, 143, 12, 52, 116, 11, 25, 10, 133, 153, 135, 118, 102, 104, 103, 17, 154, 128, 31, 18 ,15, 41, 3, 90, 124, 108, 23, 37, 60, 127, 173, 136, 175, 110, 27, 158, 147, 167, 168, 64, 53, 6, 152, 95, 36, 49, 43, 169, 126, 164, 134, 28, 174, 71, 177 ,176 ,120 ,159, 142, 96 ,98 ,140, 30, 156, 32, 122]
list2 = ['Abhyudaya Nagar', 'Afghan Church', 'Andheri', 'Andheri (E)', 'Andheri (W)', 'Andheri Kurla Road', 'Andheri Rly Stn (W)', 'Bandra' 'Bandra (W)', 'Bhagwati Hospital', 'Bhaidas Auditarium', 'Bhandup (W)', 'Bhandup Complex', 'Bharatmata Cinema', 'Bhaucha Dhakka', 'Bhendi bazaar', 'Borivali Rly Stn','Borivli (W)', 'Breach Candy', 'Byculla Bridge', 'Byculla Rly Stn', 'CST Railway Stn', 'Century Bazar', 'Chembur', 'Chembur Naka', 'Chincholi Bunder', 'Coal Bandar', 'Colaba', 'Colaba Market', 'Cooper Hospital', 'Cuff Parade', 'Currey Road', 'DN Nagar Metro Stn', 'DN Road', 'Dadar (E)', 'Dahanukar Wadi', 'Dahisar', 'Dahisar Check Naka', 'Darukhana', 'Dava Bazar', 'Deepak Talkies', 'Deonar Municipal Colony', 'Dharavi', 'Diamond Garden', 'Dinanath Mangeshkar Natyagruha', 'Dindoshi', 'Dongri', 'Elphinston Road Rly Stn', 'Elphinstone  Road Rly Stn', 'Fort', 'Four Bungalow', 'GPO, Mumbai', 'GTB Rly Stn', 'Gandhi Market', 'Gawanpada', 'Ghatkopar (E)', 'Gokuldham', 'Goregaon (W)', 'Govandi', 'Grant Road', 'Grant Road Railway Stn', 'Haji Ali', 'Hill Road', 'Hindmata Cinema','IMD Colaba', 'INS Ashwini Hospital', 'ISCON Temple, Juhu', 'Jijamata Nagar', 'Jogeshwari Rly Stn', 'KEM Hospital', 'Kajupada', 'Kalbadevi Road', 'Kamala Nehru Park', 'Kandivali (W)','Kandivli Railway Stn', 'Kannamwar Nagar', 'Khindipada', 'Kings Circle', 'Kurla (W)', 'Kurla Bhabha Hospital', 'Kurla Kamani', 'Kurla Railway Station (W)', 'Lalbaug', 'Lamington Road', 'Liberty Garden', 'Lilawati Hospital', 'Mahalaxmi Mandir', 'Maharashtra Nagar', 'Mahim (E)', 'Malad', 'Malad Link Road', 'Malbar Hill', 'Malvani', 'Mandavi', 'Mankhurd', 'Mantralaya', 'Maratha Mandir', 'Marine Lines Rly Stn', 'Marol', 'Marve Beach', 'Masjid Bunder Rly Stn', 'Matunga', 'Memonwada', 'Metro Junction','Milan Subway', 'Milind Nagar, JVLR', 'Mithi Chowky Junction', 'Mulund (E)', 'Mulund (W)', 'Mulund Rly Stn', 'Mumbai Central', 'Mumbai Domestic Airport', 'Municipal Head Office', 'Nadkarni Park', 'Nair Hospital', 'Nana Chowk', 'Nana Jagannath Shankarshet Flyover', 'Nariman Point', 'Natraj Cinema', 'Nehru Science Centre', 'Parel Bhoiwada', 'Parel TT', 'Passport Office', 'Patkar College', 'Poisar', 'Powai', 'Powai Gardens', 'Prabhat Colony', 'Prabodhankar Natyagruha', 'Pratiksha Nagar', 'Priyadarshini Park', 'Rajawadi Hospital','Ram Mandir  Rly Stn', 'Reay Road', 'S V Road Malad (W)', 'Sakinaka', 'Sandhurst Road Rly Stn', 'Santacruz Rly Stn', 'Sarvoday Hospital', 'Sasmira Road', 'Sea Link Bandra', 'Senapati Bapat Marg', 'Sewri', 'Shatabdi Hospital Kandivli', 'Shiv Sagar Estate', 'Shivaji Nagar, JVLR', 'Sion Koliwada', 'Tagore Nagar', 'Thakur Complex' 'V N Desai Municipal Hospital', 'Vakola Police Station', 'Vashi Creek', 'Versova Village', 'Vidhan Bhavan', 'Vikhroli', 'Vikhroli Park Site', 'Vileparle Rly Stn (W)', 'Wadala', 'Walkeshwar', 'Worli', 'Worli Naka']
print(len(list))
print(len(list2))
result = np.empty([161,7])
for i in range(161):
    for j in range(7):
        result[i][j] = 0.0
for i in range(len(list)):
     result[i][0] = list[i]
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
url = 'http://dm.mcgm.gov.in/livefullpage'
driver.get(url)
for i in range(len(list)):
    Select(driver.find_element_by_id('menulistsublocation')).select_by_value(str(int(result[i][0])))
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
    print(i)
    print(result[i][:])
time.sleep(95)
