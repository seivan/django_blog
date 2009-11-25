import re
from markup import *
from pictures import * 
from youtube import * 
from syntax import * 

def find_function(content):
    regex = re.compile(r"\[(?P<function>\w+) (?P<variable>[^\]]+)\]")
    match = regex.search(content)
    if not match: return content
    return regex.sub(match_function, content)

def match_function(match):
    if match.group("function") == "picture":
         return embed_picture(match.group("variable"))
    elif match.group("function") == "youtube":
         return embed_youtube(match.group("variable"))
    else:
         #return "<b> Functon %s, doesn't exist </b>" % match.group("function")
         return match.group(0)
      
def find_syntax(content):
    regex = re.compile(r'(\<code_(?P<language>.+?)\>)(?P<code>.+?)(\<\/code\>)', re.DOTALL)
    match = regex.search(content)
    if not match: return content
    return regex.sub(embed_syntax, content)

def find_markup(content):
    regex = re.compile(r'(\<markup\>)(?P<markup>.+?)(\<\/markup\>)', re.DOTALL)
    match = regex.search(content)
    if not match: return content
    return regex.sub(embed_markup, content)


 
