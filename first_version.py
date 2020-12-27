import json

import requests
import time

headers = {
    'authority': 'www.reddit.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9,he-IL;q=0.8,he;q=0.7,lb;q=0.6',
}

num_of_articles=10
params = (
    ('limit', str(num_of_articles)),
)

def get_date(time_in_utc):
    time_regular=time.strftime("%H:%M , %d.%m.%Y",time.gmtime(time_in_utc))
    return time_regular

def get_response(subreddit,after):
    if (after == None):
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/.json', headers=headers, params=params)
    else:
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/.json?after={after}', headers=headers,
                                params=params)

    json_respone = response.json()
    datas_children = json_respone['data']['children']

    if(len(datas_children) != 0):
        return [subreddit,json_respone,datas_children]
    else:
        while (len(datas_children) == 0):
            print("The subbrediit you looked for was'nt found, lets try again ")
            print("Please enter a subreddit name ")
            subreddit = input()
            if (after == None):
                response = requests.get(f'https://www.reddit.com/r/{subreddit}/.json', headers=headers,
                                        params=params)
            else:
                response = requests.get(f'https://www.reddit.com/r/{subreddit}/.json?after={after}',
                                        headers=headers, params=params)
            json_respone = response.json()
            datas_children = json_respone['data']['children']

    return [subreddit, json_respone, datas_children]



def get_articles(subreddit):
    id = 0
    after=None
    while(True):
        try:
            [subreddit, json_respone, datas_children]=get_response(subreddit,after)
            after=json_respone['data']['after']
            dict = {}
            for item in datas_children:

                article=[{
                        "id":id,
                        "Title":item['data']['title'] ,
                        "Author":item['data']['author'],
                        "Url:": item['data']['url'],
                        "Posted at:":get_date(int(item['data']['created_utc'])),
                        "Score":item['data']['score'],



                        } ]
                article = article[0]
                dict[f"Article {str(id)}"]=article



                id=id+1
            j = json.dumps(dict)
            parsed = json.loads(j)
            print(json.dumps(parsed, indent=2))
            # print(dict.keys())

            print( "\nThat is all for now, show the next articles? (Y/N) ")
            user_input=input().lower();
            while(user_input != "y"  and  user_input != "n"  ):
                print("wrong answer.. let's try again, show the next articles? (Y/N) ")
                user_input = input().lower();

            if(user_input=="y"):
                    print("Yes")
            else:
                print("No")
                print("do you want to search for another subreddit?  (Y/N)")
                user_input = input().lower();
                while (user_input != "y" and user_input != "n"):
                    print("wrong answer.. let's try again, search for another subreddit? (Y/N) ")
                    user_input = input().lower();
                if (user_input == "y"):
                    print("Yes")
                    return True
                else:
                    print("No")
                    return False
        except:
            print("The subbrediit you looked for wasn't found, lets try again ")
            print("Please enter a subreddit name ")
            subreddit = input()



if(__name__=="__main__"):
    print("Please enter a subreddit name ")
    subreddit=input()
    another_subreddit=True
    while(another_subreddit):
        another_subreddit= get_articles(subreddit)
        if(another_subreddit):
            print("Please enter a subreddit name ")
            subreddit = input()
