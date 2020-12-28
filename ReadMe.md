# Subbredit Presenter
The Subbredit Presenter is a full stack application to present Reddit.com subreddits in a useful way.


## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)


## General info
This project uses Python flask , JavaScript and HTML in order to display information about the articles asked by the user.

## Screenshots
!(./Screenshot.png)

## Technologies
* Server - Python (3.7) flask
* Client - JavaScript, HTML

## Setup
* install python 3 (or above)
* install pip (sudo apt-get install python3-pip)
* install flask (pip3 install Flask)


## Code Examples

`def get_articles(subreddit, num_of_articles):
    """
    :param subreddit: The name of the subreddit asked by the user. 
    :param num_of_articles:  The number of articles asked by the user.
    :return: messages - A list of strings representing the founded articles.
    """
    id = 0
    message_lst = []
    params = (('limit', str(num_of_articles)),)
    while (True):
        try:
            response = requests.get(f'https://www.reddit.com/r/{subreddit}/.json', headers=headers, params=params)
            json_respone = response.json()
            datas_children = json_respone['data']['children']
            for item in datas_children:
                article = [{
                    "id": id,
                    "Title": item['data']['title'],
                    "Author": item['data']['author'],
                    "Url": item['data']['url'],
                    "Posted at": get_date(int(item['data']['created_utc'])),
                    "Score": item['data']['score'],
                }]
                article = article[0]
                message_lst.append(f"Article number {str(article['id'] + 1)}:\n ")
                message_lst.append(f"Title: {article['Title']}")
                message_lst.append(f"by  {article['Author']}/")
                message_lst.append(f"Article's link: {article['Url']}\n")
                message_lst.append(f"Posted on {article['Posted at']}\n")
                message_lst.append(f"Has a score of {article['Score']} \n")
                message_lst.append("\n")
                id = id + 1
        except:
            return ["wrong subreddit name, Please try again"]
        return message_lst`


## Features
List of features ready and TODOs for future development
* Rest API - to communicate between the server and the client.

## Status
Project is: finished

