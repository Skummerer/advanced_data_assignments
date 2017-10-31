import urllib2
from bs4 import BeautifulSoup
url="https://www.mshp.dps.missouri.gov/HP68/search.jsp"
html=urllib2.urlopen(url).read()
soup=BeautifulSoup(html, 'html.parser')
table=soup.find('table',{'class': 'accidentOutput'})
for tr in table.find_all('tr'):
    for td in tr.find_all('td'):
        print td.text 
import urllib2, csv
from bs4 import BeautifulSoup
output_file=open('mopatrol2','w')
writer=csv.writer(output_file)
url="https://www.mshp.dps.missouri.gov/HP68/search.jsp"
html=urllib2.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
table=soup.find('table',{'class':'accidentOutput'})
row_list=table.find_all('tr')
for row in row_list:
	cell_list=row.find_all('td')
	data=[cell.text for cell in cell_list]
	writer.writerow(data)
