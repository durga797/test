import os
from urllib2 import urlopen, URLError, HTTPError
import pandas as pd 
import zipfile


def dlfile(url):
    #Open the url
    try:
        f = urlopen(url)
        print "downloading " + url

        # Open our local file for writing
        with open(os.path.basename(url), "wb") as local_file:
            local_file.write(f.read())
    #handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url
    loc = url.split('/')[-1]
    zip_ref = zipfile.ZipFile(loc, 'r')
    extracted = zip_ref.namelist()
    zip_ref.extractall()
    zip_ref.close()

    return extracted[0]