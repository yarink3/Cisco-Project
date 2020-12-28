# Subbredit Presenter
The Subbredit Presenter is a full stack application to present Reddit.com subreddits in a useful way.


## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Link to the website (UI version)](#link-to-website)
* [Setup](#setup)
* [How to run](#how-to-run)
* [Features](#features)
* [Status](#status)



## General info
This project uses Python flask , JavaScript and HTML in order to display information about the articles of the subbredit asked by the user.

## Screenshots
![main web page](https://github.com/yarink3/subbredit-presenter/blob/main/Screenshot.png)

## Technologies
* Server - Python (3.7) flask
* Client - JavaScript, HTML

## Link to the website (UI version)
* https://yarin-kagal.herokuapp.com/

## Setup
* install python 3 (or above)
* install pip (sudo apt-get install python3-pip)
* install flask (pip3 install Flask)

## How to run
* On terminal run:
 git clone https://github.com/yarink3/subreddit-presenter.git
 cd subreddit-presenter
* This Project has 2 version, command line version and GUI version.
* To run the command line version ,run:
 first_version.py
* To run the GUI version ,run
  python3 app.py
  go to http://localhost:5000/ and follow the instructions

## Code Examples

```
   def get_articles(subreddit, num_of_articles):
    
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

        return message_lst

```


## Features
* Rest API - to communicate between the server and the client.

## Status
Project is: finished

