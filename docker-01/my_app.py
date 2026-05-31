from flask import Flask

app = Flask('__main__')

@app.route('/')
def home():
  return "Hello World!"

@app.route('/about')
def about():
  return "This is about page!"


if __name__ == '__main__':
  app.run('0.0.0.0',port = 5000);