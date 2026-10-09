import os

# image directory is pre defined
IMAGE_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), "images"))

# Allowlist built from the products the app already knows about
ALLOWED_IMAGES = {p["image"] for p in PRODUCTS.values()}

# get file name from get request
filename = request.args.get("filename", "")


## SECURITY ENHANCED CODE

# FIX 1 (primary): allowlist validation
if filename not in ALLOWED_IMAGES:
    abort(404)


# FIX 2 (defence in depth): canonicalise and confirm containment
full_path = os.path.realpath(os.path.join(IMAGE_DIR, filename))
if os.path.commonpath([IMAGE_DIR, full_path]) != IMAGE_DIR:
    abort(404)
if not os.path.isfile(full_path):
    abort(404)


# FIX 3 safe serving function (applies its own safe_join check)
return send_from_directory(IMAGE_DIR, filename)


