import requests



def fetch_random_joke():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"

    response = requests.get(url)
    print(response.text)  # Debugging line to print the raw response text
    data = response.json()
    # print(f"Response Data: {data}")  # Debugging line to print the entire response data
    if data["success"] and "data" in data:
        # print(f"Data keys: {data['data'].keys()}")  # Debugging line to print the keys in the 'data' dictionary
        joke_data = data["data"]["data"][0]["content"]
        print(f"Joke: {joke_data}")
        jokes=[]
        # for joke in data["data"]["data"]:
        #     jokes.append(joke["content"])
        # for joke in jokes:
        #     print("*"*20)
        #     print(f"Joke: {joke}")
        #     print("*"*20)
        # print(f"Jokes: {jokes}\n")
        return joke_data
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}, {data.get('error', 'No error message provided')}")
        return {"error": "Failed to fetch data", "status_code": response.status_code}   







def main():

    # fetch_random_joke()
    try:
        fetch_random_joke()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()