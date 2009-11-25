import textile

def embed_markup(match):
    return textile.textile(match.group("markup"))
