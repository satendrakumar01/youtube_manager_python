import requests

def test_get_stock_data():
    url="https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata"
    response= requests.get(url)
    data= response.json()

    if data["success"] and "data" in data:
        stock_data= data["data"]["data"][0]["Symbol"]
        Name_data= data["data"]["data"][0]["Name"]
        MarketCap_data= data["data"]["data"][0]["MarketCap"]
        currentPrice_data= data["data"]["data"][0]["CurrentPrice"]
        for stock in data["data"]["data"]:
            print(f"Stock Symbol: {stock['Symbol']}")
            print(f"Stock Name: {stock['Name']}")
            print(f"Market Cap: {stock['MarketCap']}")
            print(f"Current Price: {stock['CurrentPrice']}")
            print("*"*20) 
        # print(f"Stock Symbol: {stock_data}")
        # print(f"Stock Name: {Name_data}")
        # print(f"Market Cap: {MarketCap_data}")
        # print(f"Current Price: {currentPrice_data}")    
        return stock_data, Name_data, MarketCap_data, currentPrice_data
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}, {data.get('error', 'No error message provided')}")
        return {"error": "Failed to fetch data", "status_code": response.status_code}       
  







def main():
    try:
        test_get_stock_data()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()