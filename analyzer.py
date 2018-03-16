import json
import csv
import os
from haralyzer import HarPage

'''
Copy all files into path specified "har_files" in this case.

Rename all files from 0 to n. Like 0.har, 1.har and so on.

Specific max number as limit in the for loop. for x in range (0, n)

Make sure CSV file is empty and exists as it writes into it.




'''


for x in range(0, 86):

    with open(os.path.join('har_files',f'{x}.har'), 'r') as f:
        har_page = HarPage('page_1', har_data=json.loads(f.read()))

    with open ("output.csv", "a") as csv_file:
        csv_app = csv.writer(csv_file)
        csv_app.writerow([har_page.url,
                          har_page.hostname,
                          har_page.page_load_time,
                          har_page.time_to_first_byte,
                          har_page.page_size,
                          har_page.content_load_time,
                          har_page.html_load_time,
                          har_page.css_load_time,
                          har_page.js_load_time,
                          har_page.initial_load_time,
                          har_page.audio_load_time,
                          har_page.video_load_time,
                          har_page.image_load_time])




'''
### WORK WITH LOAD TIMES (all load times are in ms) ###
# Link http://pythonhosted.org/haralyzer/haralyzer.html

#Page url
print("Page URL")
print(har_page.url)

#Hostname
print(har_page.hostname)

#PLT
print("PLT")
print(har_page.page_load_time)

# TTFB
print("TTFB")
print(har_page.time_to_first_byte)

#Page Size
print("Page Size")
print(har_page.page_size)

#Content Load Time - Returns the full load time (in milliseconds) of the page itself
print(har_page.content_load_time)

#HTML Load Time - Returns the browser load time for all html files.
print(har_page.html_load_time)

#CSS Load Time - Returns the browser load time for all CSS files.
print(har_page.css_load_time)

#JS Load Time
print(har_page.js_load_time)

#Initial Load Time - Load time for the first non-redirect page
print(har_page.initial_load_time)

# Audio Load Time
print(har_page.audio_load_time)

#Video Load Time
print(har_page.video_load_time)

# Get image load time in milliseconds as rendered by the browser
print(har_page.image_load_time)


'''




'''
# Get the transferred sizes (works only with HAR files, generated with Chrome)
print(har_page.page_size_trans)
print(har_page.image_size_trans)
print(har_page.css_size_trans)
print(har_page.text_size_trans)
print(har_page.js_size_trans)
print(har_page.audio_size_trans)
print(har_page.video_size_trans)


'''
