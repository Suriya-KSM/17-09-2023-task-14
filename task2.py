import requests


class Database:

    def __init__(self, web_url):
        self.url = web_url

    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()


    def details_of_breweries(self,state):
        count1 = 0
        self.state = state
        for data in self.fetch_data():
            if str(data['state']) == self.state:
                print(data['name'])
                count1 = count1 + 1
        print("\nBreweries count", count1)

    def types_of_breweries(self,state):
        self.state = state
        list1 = []
        result = {}
        for data in self.fetch_data():
            list1.append(data['brewery_type'])
            for i in list1:
                result[i] = list1.count(i)
        print(result)

    def website_breweries(self,state):
        self.state= state
        count2 = 0
        for data in self.fetch_data():
            if data['website_url']:
                count2 = count2 + 1
        print("\nTotal number of breweries which having websites", count2,'\n')




url1 = "https://api.openbrewerydb.org/v1/breweries?by_state=Alaska"
print("Lists of brewery in Alaska\n")
obj = Database(url1)
obj.details_of_breweries("Alaska")
obj.types_of_breweries("Alaska")
obj.website_breweries("Alaska")

url2 = "https://api.openbrewerydb.org/v1/breweries?by_state=Maine"
print("\n\nLists of brewery in Maine\n")
obj1 = Database(url2)
obj1.details_of_breweries("Maine")
obj1.types_of_breweries("Maine")
obj1.website_breweries("Maine")

url3 = "https://api.openbrewerydb.org/v1/breweries?by_state=New%20York"
print("\n\nLists of brewery in New York\n")
obj2 = Database(url1)
obj2.details_of_breweries("New York")
obj2.types_of_breweries("New York")
obj2.website_breweries("New York")