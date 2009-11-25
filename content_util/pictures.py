def embed_picture(content):
    try:
        picture_name, url = content.split(",")
    except ValueError:
        picture_name = content.split(",")[0]
    try:
        from seivanheidari.picture.models import Photo
        photo_obj = Photo.objects.filter(name=picture_name)[0]
        picture = photo_obj.picture
        try:
            return "<a href='%s'><img src='%s' width='200' height='200' alt='%s' /></a>" % (url, picture.url_200x200, picture_name)
        except NameError:
            url = picture.url #original for download
    except IndexError:
        return "<b> Picture: '" + picture_name + "' doesn't exist! </b>"
    return "<a class='lightbox' href='%s'><img src='%s' width='200' height='200' alt='%s' /></a>" % (picture.url_1024x800, picture.url_200x200, picture_name)