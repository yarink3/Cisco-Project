from flask import Flask, render_template , request, redirect ,flash
import datetime
# import sqlite3
from Appreddit import *


app = Flask(__name__)
app.secret_key = 'yarin kagal'

numOfUrls = 0
redirectionsSoFar=0
numOfWrongRedirections=0

@app.route('/',methods=['post','get'])
def index():
    message=""
    if(request.method=='POST' ):
        print(request)
        subreddit=request.form.get('subreddit_name')
        num_of_articles=request.form.get('num_of_articles')
        # after=None
        # if(request.name=="next_articles"):
        # after=request.form.get('after')

        print("Subreddit entered "+subreddit)

        [message_lst,after]=get_articles(subreddit,num_of_articles,None)
        if(len(message_lst)==0):
            flash("We couldn't find anything about this subreddit, try again", "error")
        else:
            for line in message_lst:
                if(line=="\n"):
                    flash(line,"new_line")
                if(line[0:14]=="Article's link"):
                    flash(line[16:len(line)-1],"link")
                elif line[0:5]=="Title":
                    flash(line[7:len(line)-1],"bold")
                else:
                    flash(line,"regular")

    return render_template('index.html')


@app.route('/handle_form', methods=['POST'])
def handle_form():

    print("hello")
    return render_template('index.html')






if __name__ == '__main__':
    app.debug=True
    app.run(host= '0.0.0.0',port=5000)
