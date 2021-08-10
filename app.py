from flask import Flask
import wikipedia

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'

def build_url(str):
  return 'https://en.wikipedia.org/wiki/{}'.format(str.replace('"', '').replace(' ', '_'))

def contains_search(search):
  return lambda str: search.lower() in str.lower()

@app.route('/', subdomain='<search>', methods=['GET'])
def search_index(search):
  try:
    wikipedia.page(search)

    return {
      'links': [build_url(search)]
    }
  except wikipedia.DisambiguationError as e:
    filtered_list = list(filter(contains_search(search), e.options))

    return {
      'links': list(map(build_url, filtered_list))
    }
  except:
    return "Something terrible has happened!"

@app.route('/')
def hello_world():
  return "Hello, World!"

if __name__ == '__main__':
  app.run(debug=True)
