from flask import Flask, request, render_template
import wikipedia
import json
  
app = Flask(__name__)
app.config['SERVER_NAME']='*.wiki-search.com'
app.url_map.default_subdomain = "www"

# create HOME View
@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        search = request.form["search"]

        query = wikipedia.page(search)
        
        # Fetch data from wikipedia
        #result = (query.url)
        result[0] = list.insert(query.url)
        return f"<h2>{result}</h2>"
  
  
if __name__ == '__main__':

    app.run()