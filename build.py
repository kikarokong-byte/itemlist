"""Build index.html from src/app.html with the TH Sarabun New fonts inlined.

    python3 build.py              -> writes index.html (standalone page, open it in a browser)
    python3 build.py --body OUT   -> also writes OUT without the <html>/<head>/<body> wrapper
"""
import base64
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent


def b64(name):
    return base64.b64encode((ROOT / "fonts" / name).read_bytes()).decode("ascii")


body = (ROOT / "src" / "app.html").read_text(encoding="utf-8")
body = body.replace("@@FONT_REGULAR@@", b64("THSarabunNew.ttf")).replace("@@FONT_BOLD@@", b64("THSarabunNew-Bold.ttf"))

page = (
    '<!doctype html>\n<html lang="th">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    "</head>\n<body>\n" + body + "\n</body>\n</html>\n"
)
(ROOT / "index.html").write_text(page, encoding="utf-8")

if len(sys.argv) == 3 and sys.argv[1] == "--body":
    pathlib.Path(sys.argv[2]).write_text(body, encoding="utf-8")
