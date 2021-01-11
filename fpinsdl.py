from pandas.io.html import read_html
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import html
import datetime




#table = driver.find_element_by_xpath('//*[@id="myTable"]')
#table_html = table.get_attribute('innerHTML')

#df = read_html(table_html)
#print df


def FPInsdl(nd):
    
    while True:
        
        url = "https://www.fpi.nsdl.co.in/web/Reports/Film_List_All.aspx"
        driver = webdriver.Chrome("D:\\Master\\chromedriver.exe")
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        temp =  soup.prettify()
        
        table=soup.find_all('tr')
        td=soup.find_all('td')
        td_val=[]
        for i in range(len(td)):
            #print td[i].text
            td_val.append(td[i].text)
            
        th=soup.find_all('th')
        th_val=[]
        for i in range(len(th)):
            #print th[i].text
            th_val.append(th[i].text)

        driver.close()





'''
u'\n            <thead id="tablhead" style="">\n\n            <tr class="col-md-12 row-border" role="row"><th rowspan="2" class="col-md-1 text-center sorting_asc" tabindex="0" aria-controls="myTable" colspan="1" aria-sort="ascending" aria-label="Sr. No.: activate to sort column descending" style="width: 5%;">Sr. No.</th><th rowspan="2" class="col-md-1 text-center sorting" tabindex="0" aria-controls="myTable" colspan="1" aria-label="ISIN: activate to sort column ascending" style="width: 8%;">ISIN</th><th rowspan="2" class="col-md-2 text-left sorting" tabindex="0" aria-controls="myTable" colspan="1" aria-label="Issuer Name: activate to sort column ascending" style="width: 15%;">Issuer Name</th><th colspan="5" class="col-md-7" rowspan="1">\n                    \tAggregate Permissible Foreign Investment Limits\t\n                </th><th rowspan="2" class="col-md-1 text-center sorting" tabindex="0" aria-controls="myTable" colspan="1" aria-label="Remarks: activate to sort column ascending" style="width: 40%;">Remarks</th></tr>\n                <tr role="row" class="row-border"><td style="font-weight: bold; width: 5%;" class="text-center sorting" tabindex="0" aria-controls="myTable" rowspan="1" colspan="1" aria-label="Non-Resident Indian (NRI) Limit (%): activate to sort column ascending">Non-Resident Indian (NRI) Limit (%)</td><td style="font-weight: bold; width: 5%;" class="text-center sorting" tabindex="0" aria-controls="myTable" rowspan="1" colspan="1" aria-label="Foreign Portfolio Investor (FPI) Limit  (%): activate to sort column ascending">Foreign Portfolio Investor (FPI) Limit  (%)</td><td style="font-weight: bold; width: 5%;" class="text-center sorting" tabindex="0" aria-controls="myTable" rowspan="1" colspan="1" aria-label="Sectoral Cap  (%): activate to sort column ascending">Sectoral Cap  (%)</td><td style="font-weight: bold; width: 10%;" class="text-center sorting" tabindex="0" aria-controls="myTable" rowspan="1" colspan="1" aria-label="Aggregate Permissible Limit upto which Company has obtained Govt. Approval  (%): activate to sort column ascending">Aggregate Permissible Limit upto which Company has obtained Govt. Approval  (%)</td><td style="font-weight: bold; text-align: center !important; width: 15%;" class="text-right sorting" tabindex="0" aria-controls="myTable" rowspan="1" colspan="1" aria-label="Paid up equity capital on fully diluted basis (in terms of number of shares) as reported by Stock Exchange(s) and used for monitoring of foreign investment limits\n                        : activate to sort column ascending">Paid up equity capital on fully diluted basis (in terms of number of shares) as reported by Stock Exchange(s) and used for monitoring of foreign investment limits\n                        </td></tr>\n                </thead>\n            <tbody id="tblbody"><tr role="row" class="odd row-border"><td class=" text-center">1</td><td class=" text-center">INE253B01015</td><td class=" text-left">21st CENTURY MANAGEMENT SERVICES LIMITED</td><td class=" text-center">10</td><td class=" text-center">100</td><td class=" text-center">100</td><td class=" text-center"></td><td class=" text-right">1,05,00,000</td><td class=" text-center">Automatic Route:100%</td></tr><tr role="row" class="even row-border"><td class=" text-center">2</td><td class=" text-center">INE748C01020</td><td class=" text-left">3I INFOTECH LIMITED</td><td class=" text-center">10</td><td class=" text-center">100</td><td class=" text-center">100</td><td class=" text-center"></td><td class=" text-right">1,70,99,49,989</td><td class=" text-center">Automatic Route:100%</td></tr><tr role="row" class="odd row-border"><td class=" text-center">3</td><td class=" text-center">INE470A01017</td><td class=" text-left">3M INDIA LIMITED</td><td class=" text-center">10</td><td class=" text-center">100</td><td class=" text-center">100</td><td class=" text-center"></td><td class=" text-right">1,12,65,070</td><td class=" text-center">Automatic Route:100%</td></tr><tr role="row" class="even row-border"><td class=" text-center">4</td><td class=" text-center">INE105C01023</td><td class=" text-left">3P LAND HOLDINGS LIMITED</td><td class=" text-center">10</td><td class=" text-center">100</td><td class=" text-center">100</td><td class=" text-center"></td><td class=" text-right">1,80,00,000</td><td class=" text-center">Automatic Route:100%</td></tr><tr role="row" class="odd row-border"><td class=" text-center">5</td><td class=" text-center">INE454F01010</td><td class=" text-left">7SEAS ENTERTAINMENT LIMITED</td><td class=" text-center">10</td><td class=" text-center">100</td><td class=" text-center">100</td><td class=" text-center"></td><td class=" text-right">1,11,10,900</td><td class=" text-center">Automatic Route:100%</td></tr><tr role="row" class="even row-border"><td class=" text-center">6</td><td class=" text-center">INE319X01018</td><td class=" text-left">A &amp; M FEBCON LIMITED</td><td class=" text-center">24</td><td class=" text-center">100</td><td class=" text-center">100</td><td class=" text-center"></td><td class=" text-right">1,28,13,205</td><td class=" text-center">Automatic Route:100%</td></tr><tr role="row" class="odd row-border"><td class=" text-center">7</td><td class=" text-center">INE749Y01014</td><td class=" text-left">A AND M JUMBO BAGS LIMITED</td><td class=" text-center">10</td><td class=" text-center">100</td><td class=" text-center">100</td><td class=" text-center"></td><td class=" text-right">70,10,000</td><td class=" text-center">Automatic Route:100%</td></tr><tr role="row" class="even row-border"><td class=" text-center">8</td><td class=" text-center">INE00YB01017</td><td class=" text-left">A B INFRABUILD LIMITED</td><td class=" text-center">10</td><td class=" text-center">100</td><td class=" text-center">100</td><td class=" text-center"></td><td class=" text-right">1,26,69,447</td><td class=" text-center">Automatic Route:100%</td></tr><tr role="row" class="odd row-border"><td class=" text-center">9</td><td class=" text-center">INE534E01020</td><td class=" text-left">A INFRASTRUCTURE LIMITED</td><td class=" text-center">10</td><td class=" text-center">100</td><td class=" text-center">100</td><td class=" text-center"></td><td class=" text-right">4,26,45,700</td><td class=" text-center">Automatic Route:100%</td></tr><tr role="row" class="even row-border"><td class=" text-center">10</td><td class=" text-center">INE663P01015</td><td class=" text-left">A. F. ENTERPRISES LIMITED</td><td class=" text-center">10</td><td class=" text-center">100</td><td class=" text-center">100</td><td class=" text-center"></td><td class=" text-right">40,00,000</td><td class=" text-center">Automatic Route:100%</td></tr></tbody>\n        '
'''