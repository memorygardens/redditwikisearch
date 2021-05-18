from flask import Flask, request, render_template
import wikipedia
import json
  
app = Flask(__name__)
#app.config['SERVER_NAME']='.wiki-search.com'
#app.url_map.default_subdomain = "*"

# create HOME View
@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        search = request.form["search"]

        query = wikipedia.search(search, results = 3)
        
        # Fetch data from wikipedia
        #loop here. 
        for x in query:
            print(x)
            page = wikipedia.page(x)
            print(page)
        pages = wikipedia.page(query)
        print("help")
        print(pages[1].url)
        result = (pages.url)
        print(result)
        return f"<h2>{pages}</h2>"
  
  
if __name__ == '__main__':

    app.run()