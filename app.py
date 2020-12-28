from flask import Flask, render_template , request, redirect ,flash
from UI_Version import *

app = Flask(__name__)
app.secret_key = 'yarin kagal'

@app.route('/',methods=['post','get'])
def index():
    """
    A function to run and display the main web page.
    :return: Rendering the index.html file as a template (can be found inside 'templates' directory)
    """
    if(request.method=='POST' ):
        subreddit=request.form.get('subreddit_name')
        num_of_articles=request.form.get('num_of_articles')

        message_lst=get_articles(subreddit,num_of_articles)
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
                elif line[0:2]=="by":
                    flash(line[4:len(line)-1],"author")
                else:
                    flash(line,"regular")

    return render_template('index.html')



if __name__ == '__main__':
    app.run(host= '0.0.0.0',port=5000)
