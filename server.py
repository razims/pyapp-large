import os
from flask import Flask
import sys

app = Flask(__name__)
port = int(os.environ.get('PORT', 3000))


@app.route('/')
def hello():
    return "Hello World from Python %s : %s" % (sys.version, sys.version_info)


if __name__ == '__main__':
    app.run(port=port)
