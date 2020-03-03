from os import getcwd
import sys
import os
import datetime
import time
import html

print(os.getcwd())

print(sys.platform)

print(sys.version)

print(datetime.date.isoformat(datetime.date.today()))

print(time.strftime("%H:%M"))

print(html.escape("This HTML fragment contains a <script>script</script> tag."))

print(html.unescape("I &hearts; Python's &lt;standard library&gt;."))