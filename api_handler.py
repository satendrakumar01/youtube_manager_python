import requests


def fetch_random_users():
    url = "https://api.freeapi.app/api/v1/public/randomusers/13"
    response = requests.get(url)
    data= response.json()
    if data["success"] and "data" in data:
        user_data= data["data"]["login"]["username"]
        email_data= data["data"]["email"]
        location_data= data["data"]["location"]["country"]
        print(f"Username: {user_data}, Email: {email_data}, Location: {location_data}")

        return user_data
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}, {data.get('error', 'No error message provided')}")
        return {"error": "Failed to fetch data", "status_code": response.status_code}
    





def main():
    try:
        fetch_random_users()
    except Exception as e:
        print(f"An error occurred: {e}")    

if __name__ == "__main__":
    main()