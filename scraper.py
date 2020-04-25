import flickrapi
import urllib.request
from PIL import Image

# Flickr api access key 
flickr=flickrapi.FlickrAPI('c6a2c45591d4973ff525042472446ca2', '202ffe6f387ce29b', cache=True)


keyword = 'building'

photos = flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=1000,           # may be you can try different numbers..
                     sort='relevance',
		     license_name='No known copyright restrictions')

urls = []
for i, photo in enumerate(photos):
    print (i)
    
    url = photo.get('url_c')
    urls.append(url)
    
    # get 50 urls
    if i > 10000:
        break

print (urls)
j = 0

# Download image from the url and save it to '00001.jpg'
while j < 1001:
    try:
        urllib.request.urlretrieve(urls[j], str('000' + str(j) + '.jpg'))
        # Resize the image and overwrite it
        image = Image.open(('000' + str(j) + '.jpg')) 
        #image = image.resize((256, 256), Image.ANTIALIAS)
        image.save(('000' + str(j) + '.jpg'))
    except:
        pass
    j += 1