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



def get_date(time_in_utc):
    time_regular=time.strftime("%H:%M , %d.%m.%Y",time.gmtime(time_in_utc))
    return time_regular
    
def get_articles(subreddit,num_of_articles,after):
    id = 0
    message_lst=[]
    # after=None
    params = (('limit', str(num_of_articles)),)
    while(True):
        try:
            if (after == None):
                response = requests.get(f'https://www.reddit.com/r/{subreddit}/.json', headers=headers, params=params)
            else:
                response = requests.get(f'https://www.reddit.com/r/{subreddit}/.json?after={after}', headers=headers,
                                        params=params)

            json_respone = response.json()
            datas_children = json_respone['data']['children']
            # [subreddit, json_respone, datas_children]=get_response(subreddit,after,params)
            after=json_respone['data']['after']
            dict = {}
            for item in datas_children:

                article=[{
                        "id":id,
                        "Title":item['data']['title'] ,
                        "Author":item['data']['author'],
                        "Url": item['data']['url'],
                        "Posted at":get_date(int(item['data']['created_utc'])),
                        "Score":item['data']['score'],



                        } ]
                article = article[0]

                message_lst.append(f"Article number {str(article['id']+1)}:\n ")

                message_lst.append(f"Title: {article[ 'Title']} by  {article['Author']} .\n")
                message_lst.append(f"Article's link: {article['Url']}\n")
                message_lst.append(f"Posted on {article['Posted at']}\n")
                message_lst.append(f"Has a score of {article['Score']} \n")
                message_lst.append("\n")
                id=id+1

                # dict[f"Article {str(id)}"]=article

        except:
            return [["wrong subreddit name, Please try again"],None]

        return [message_lst,after]



