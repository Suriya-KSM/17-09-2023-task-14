import requests


class JSON:

    def __init__(self, web_url):
        self.url = web_url

    # fetch data from the API server
    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()

    def fetch_currency_details(self):
        for data in self.fetch_data():
            print('\n\nName of the Country: ',data['name']['official'])
            for i,j in data['currencies'].items():
                print('Currecy: ',j['name'], ' Symbol:',j['symbol'])
        print('\n\n')



    def DOLLAR(self):
        print("\nList of Countries which has DOLLAR as it's Currency is given below:\n")
        for data1 in self.fetch_data():
            currency_keys = list(data1.get('currencies', {}).keys())
            if currency_keys == ["USD"]:
                print(data1['name']['common'])


    def EURO(self):
        print("\nList of Countries which has EURO as it's Currency is given below:\n")
        for data2 in self.fetch_data():
            
            currency_keys = list(data2.get('currencies', {}).keys())
            if currency_keys == ["EUR"]:
                print(data2["name"]["common"])


url = "https://restcountries.com/v3.1/all"

obj=JSON(url)


obj.DOLLAR()

obj.EURO()

obj.fetch_currency_details()