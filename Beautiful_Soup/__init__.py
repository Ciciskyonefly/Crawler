from bs4 import BeautifulSoup
from base64 import _a85chars
import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')

#print (soup.prettify())

print (soup.head.next_element)

print (soup.find_all("b"))

print (soup.find_all("a"))

for tag in soup.find_all(re.compile("^b")):
    print (tag.name)
    
print (soup.find_all(["a","b"]))

for tag in soup.find_all(True):
    print (tag.name)
    
    
def has_class_but_no_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

print (soup.find_all(has_class_but_no_id))