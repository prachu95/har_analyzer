import json
from haralyzer import HarPage

with open('b.har', 'r') as f:
    har_page = HarPage('page_1', har_data=json.loads(f.read()))


### WORK WITH LOAD TIMES (all load times are in ms) ###
# Link http://pythonhosted.org/haralyzer/haralyzer.html


# Audio Load Time
print(har_page.audio_load_time)

#Video Load Time
print(har_page.video_load_time)

#JS Load Time
print(har_page.js_load_time)

#Hostname
print(har_page.hostname)

#Initial Load Time - Load time for the first non-redirect page
print(har_page.initial_load_time)

#CSS Load Time - Returns the browser load time for all CSS files.
print(har_page.css_load_time)

#Content Load Time - Returns the full load time (in milliseconds) of the page itself
print(har_page.content_load_time)

#HTML Load Time - Returns the browser load time for all html files.
print(har_page.html_load_time)

#Page url
print("Page URL")
print(har_page.url)

#Page Size
print("Page Size")
print(har_page.page_size)

# TTFB
print("TTFB")
print(har_page.time_to_first_byte)

#PLT
print("PLT")
print(har_page.page_load_time)


# Get image load time in milliseconds as rendered by the browser
print(har_page.image_load_time)


# Get the transferred sizes (works only with HAR files, generated with Chrome)
print(har_page.page_size_trans)
print(har_page.image_size_trans)
print(har_page.css_size_trans)
print(har_page.text_size_trans)
print(har_page.js_size_trans)
print(har_page.audio_size_trans)
print(har_page.video_size_trans)






# Get the TOTAL image load time
#har_page.total_image_load_time

# prints 2875
# We could do this with 'css', 'js', 'html', 'audio', or 'video'

### WORK WITH SIZES (all sizes are in bytes) ###

# Get the total page size (with all assets)
#print(har_page.total_page_size)

# prints 2423765

# Get the size of the actual first page that was not a redirect
# (i.e. - the HTML of the first page we care about)
#har_page.page_size
#print(x)
# prints 26951

# Get the total image size
#har_page.total_image_size
# prints 733488
# We could do this with 'css', 'js', 'html', 'audio', or 'video'
