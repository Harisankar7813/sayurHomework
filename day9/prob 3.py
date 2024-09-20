'''
**Fetching News Headlines:**
   Develop a program that fetches the latest news headlines from a news API.
   - Utilize a news API (such as NewsAPI) to retrieve the top headlines or articles for a specific category or from a particular source.
'''
import requests,json
class Headlines():
    def latest_news(self,country,category):
        api_key="2f4ff0d13914495992c74d412dacb452"
        api_url="https://newsapi.org/v2/top-headlines?"
        if country=="india":
            country="in"
        elif country=="unitedarab":
            country="ae"
        elif country=="australia":
            country="au"
        elif country=="unitedstate":
            country="us"
        updated_url=api_url+"country="+country+"&category="+category+"&apikey="+api_key
        response=requests.get(updated_url)
        if response.status_code==200:
            data=response.json()
            articles = data.get("articles", [])
            if articles:
                headline = articles[0].get("title", "No headlines available")
                print(f"{country} Top Headline ({category}): {headline}")
            else:
                print(f"No headlines available for {country} in the {category} category")
        else:
            print(f"response.status_code error")
country_name=input("Enter which Country news you want:").lower()
category_name=input("Enter what kind of category news you prefer business,entertainment,general,health,science,sports,technology:").lower()
headlines_api=Headlines()
headlines_api.latest_news(country_name,category_name)

'''
output
Enter which Country news you want:unitedstate
nt,general,health,science,sports,technology:general
us Top Headline (general): Asia stock markets today: Live updates, Australia, China trade, oil prices - CNBC
Enter which Country news you want:india
Enter what kind of category news you prefer business,entertainment,general,health,science,sports,technology:business
in Top Headline (business): Sensex, Nifty on record-breaking spree but experts caution against reckless buying - CNBCTV18
'''