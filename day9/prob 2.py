'''
**Currency Converter:**
   Create a currency converter program using a currency exchange rate API.
   - Use a currency exchange rate API (like Open Exchange Rates) to convert an amount from one currency to another based on user input.
'''
import requests,json
class currency():
    def currency_converter(self,From,to,value):
         api_key="e8220e0e156d4cc5b50c80eb9923591f"
         api_url="https://openexchangerates.org/api/convert/"
         if From=="india":
               From="INR"
         elif From=="arabia":
               From="AED"
         if to=="america":
               to="USD"
         elif to=="srilanka":
               to="LKR"
         updated_url=api_url+str(value)+"/"+From+"/"+to+"?"+"app_id="+api_key
         response=requests.get(updated_url)
         if response.status_code==200:
               data=response.json
               converted_value = data.get("result", 0)
               print(f"converted amount from {From} to {to} is:{converted_value}")
         else:
               print("response status is getting error")
from_input=input("Enter which country currency,From:").lower()
to_input=input("Enter which country currency,To:").lower()
no_of_currency=float(input("Enter no of currencies to convert :"))
currency_api=currency()
currency_api.currency_converter(from_input,to_input,no_of_currency)