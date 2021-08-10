from flask import Flask
import wikipedia

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'

def build_url(str):
  return "https://en.wikipedia.org/wiki/{}".format(str.replace(' ', '_'))

@app.route('/', subdomain="<search>", methods=["GET"])
def search_index(search):
  page = wikipedia.search(search, 15)
  if page[0].lower() in search.lower():
    return {
      "links": ["https://en.wikipedia.org/wiki/{}".format(page[0])]
    }
  urls = list(map(build_url, page))
  return {
    "links": urls
  }

@app.route('/')
def hello_world():
  return "Hello, World!"

if __name__ == '__main__':
  app.run(debug=True)
