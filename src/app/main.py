from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.conf import DEBUG


app = FastAPI(debug=DEBUG)


BODY = """
<html>
<head>
    <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>
<body>
    <p>REPL example</p>
    <py-repl></py-repl>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def repl():
    return BODY
