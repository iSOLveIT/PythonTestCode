# Local modules
import os
# User-defined modules
from project import app


app.config["SECRET_KEY"] = os.urandom(89)   # Secret_key

if __name__ == '__main__':
    app.run(port=8000)
