import urllib2, requests
import datetime
import json
import os
import time
from bs4 import BeautifulSoup

RANGE = int(os.environ.get('CHICAGO_RANGE', 2))
SEQUENCE = os.environ.get('CHICAGO_SEQUENCE', 0)
LOAD_ID = str(time.mktime(datetime.datetime.now().timetuple())).split('.')[0]

url = "http://www.chicagoelections.com/en/pctlevel3.asp"
response=requests.get(url,{"elec_code":9,"race_number":10,"ward":)


def get_html(ward):

    url = 'http://www.chicagoelections.com/en/pctlevel3/ward.asp'

    html = requests.get(url).content

    return html 

def get_table(html):

    soup = BeautifulSoup(html,”html.parser”) 

    table = soup.find(‘table’, {‘id’: ‘Autonumber1’}) 

    return table 

def set_load_id():
    os.environ['CHICAGO_LOAD_ID'] = LOAD_ID

def load_results():

    message = None
    results = []

    for ward in range(1, RANGE):
        html = get_html(str(ward))
        table = get_table(html)

        ward_dict = {}
        ward_dict['ward'] = ward
        ward_dict['precincts'] = []
        ward_dict['totals'] = {}

        for row in table.select('tr')[3:]:
            cells = row.select('td')
            try:
                int(cells[0].text.strip())
                precinct_dict = {}
                precinct_dict['total_votes'] = int(cells[1].text.strip())
                precinct_dict['rahm_votes'] = int(cells[2].text.strip())
                precinct_dict['garcia_votes'] = int(cells[4].text.strip())

                precinct_dict['rahm_pct'] = float(cells[3].text.replace('%', '').strip())
                precinct_dict['garcia_pct'] = float(cells[5].text.replace('%', '').strip())
                ward_dict['precincts'].append(precinct_dict)
            except ValueError:
                if cells[0].text.strip().lower() == 'total':
                    ward_dict['totals']['total_votes'] = int(cells[1].text.strip())
                    ward_dict['totals']['rahm_votes'] = int(cells[2].text.strip())
                    ward_dict['totals']['garcia_votes'] = int(cells[4].text.strip())

                    ward_dict['totals']['rahm_pct'] = float(cells[3].text.replace('%', '').strip())
                    ward_dict['totals']['garcia_pct'] = float(cells[5].text.replace('%', '').strip())

        results.append(ward_dict)

    return results, message


def print_results(payload):
    """
    Save the JSON results.
    """
    payload = json.dumps(payload)
    print payload

    success = True
    return success


def main():

    print "Loading timestamp %s" % LOAD_ID

    payload = load_results()
    success = print_results(payload)
    if success:
        set_load_id()

if __name__ == "__main__":
    main()