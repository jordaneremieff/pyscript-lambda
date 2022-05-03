from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from app.conf import DEBUG, LIB_PATH


app = FastAPI(debug=DEBUG)

BODY = """
<html>
<head>
    <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>
<py-env>
</py-env>
<body>
    <py-script>
        print("Hello, world!")
    </py-script>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return BODY
