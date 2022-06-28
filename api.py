import requests

import time


def top_numbers():
    response = requests.get(
        "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    )
    dic = response.json()  # パース

    numbers = []
    for number in range(0, 50):
        numbers.append(dic[number])

    return numbers


def get_info(numbers):

    for n in numbers:
        response = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{n}.json?print=pretty"
        )
        dic = response.json()

        title = dic["title"]
        url = dic["url"]
        if "url" in dic:
            
            print(f"'title':'{title}','link':'{url}'")
       
        else:
            print(f"'title':{title}")


for i in range(10):
    time.sleep(1)  # ここで1秒止まる


def main():
    numbers = top_numbers()
    get_info(numbers)


if __name__ == "__main__":
    main()
