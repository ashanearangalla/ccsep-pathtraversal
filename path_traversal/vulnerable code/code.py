import os

# image directory is pre defined
IMAGE_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), "images"))

# filename (provided by get request, where user can insert any file he desire) = "../secret_files/credentials.txt" escapes image directory and allow attacker to view other folders

filename = request.args.get("filename", "")



# VULNERABLE CODE (no validation or sanitization done to the filename variable)
path = os.path.join(IMAGE_DIR, filename)



# if attacker decides to go to the root directory and view sensitve files eg: ../../../etc/passwd file the attacker will be ablt to identify usernames and more sensitve info tthat the attacker can use to take control of the whole server, 

