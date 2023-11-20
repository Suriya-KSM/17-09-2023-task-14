import requests


class JSON:

    def __init__(self, web_url):
        self.url = web_url

    # fetch data from the API server
    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()

    def fetch_currency_details(self):
        datas=self.fetch_data()
        for data in datas:
            name = data['name']['common']
            currencies=data.get('currencies',"No currency")
            print('\n\nCountries and their currencies: ',f"{name}:{currencies}")
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



obj.fetch_currency_details()


obj.DOLLAR()

obj.EURO()