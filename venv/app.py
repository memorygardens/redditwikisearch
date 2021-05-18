from flask import Flask, request, render_template
import wikipedia
import json
  
app = Flask(__name__)
#app.config['SERVER_NAME']='.wiki-search.com'
#app.url_map.default_subdomain = "*"


@app.route("/", methods=['POST', 'GET'])
#adding subdomain = "{search}" bricks it, but I know it is necessary to change * to the correct search term based on the users input. 
def home():
    #display index if no search is happening 
    if request.method == "GET":
        return render_template("index.html")
    #display search form and begin using wikipedia api
    else:
        search = request.form["search"]
        #search wiki based on search term 3 results currently
        query = wikipedia.search(search, results = 3)
        
        #get the wiki page is needed to get the url
        pages = wikipedia.page(query)
        #get the url
        result = (pages.url)

        #pass url into a string and display to user
        return f"<h2>{result}</h2>"
  
  
if __name__ == '__main__':

    app.run()