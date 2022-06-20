import requests
import os

#url = os.environ.get('URL') 
#response = requests.get(url)




def main():
    print("Hello World!")
    url = '' 
    while url != 'quit':
        #url = input("URL: ")
        url = os.environ.get('URL') 
        response = requests.get(url)   
        print(response.status_code)
        print(response.json())

if __name__ == "__main__":
    main()
