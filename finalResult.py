# this file is where the routing occurs using input from the user

from flask import Flask, render_template, request, url_for, redirect
from string import Template
import requests
import random
import os

HTML_TEMPLATE = Template

app = Flask(__name__)

#list of videos to create the random order
happyVideos = ["y6Sxv-sUYtM", "aQUlA8Hcv4s", "d-diB65scQU", "pIgZ7gMze7A", "s6fPN5aQVDI", "iPUmE-tne5U", "s3Q80mk7bxE", "OPf0YbXqDm0"]
heartbrokenVideos = ["YQHsXMglC9A", "DksSPZTZES0", "0G3_kG5FFfQ", "SR6iYWJxHqs", "3JWTaaS7LdU", "RBumgq5yVrA", "VbfpW0pbvaU", "eM213aMKTHg"]
angryVideos = ["Y6aaLBmUSbI", "ToxmbOr00co", "uxUATkpMQ8A", "4uDwvJK0YdI", "HORkT4a2MhQ", "6fVE8kSM43I", "7NQ8OCcQ3LA", "qO-mSLxih-c"]
energeticVideos = ["PJqKkZ1VVMk", "Gbfnh1oVTk0", "eFFgbc5Vcbw", "_iyAFr8bFTM", "-dnxpbxxI-Y", "btPJPFnesV4", "09R8_2nJtjg", "gCYcHz2k5x0"]
mellowVideos = ["y7mwZULsVcQ", "DDGiSoLIG8I", "YtHWqQIfQLE", "PYF8Y47qZQY", "fBq87dbKyHQ", "hTWKbfoikeg", "8gOnU1ZKWHU", "4ormKAt8hVE"]
depressingVideos = ["7luYt6eanbA", "__Dw3YC6WzY", "yNtgGM0Csfk", "v-gk_5sdwNw", "PoWQunKQElE", "1LhmSppDLcw", "d-RMRtQ4BVE", "amwQytRNvEw"]
groovyVideos = ["DohRa9lsx0Q", "Lrle0x_DHBM", "3GwjfUFyY6M", "imYJpr09IgQ", "6QIw1BQIvT4", "yca6UsllwYs", "FGBhQbmPwH8", "god7hAPv8f0"]
romanticVideos = ["uRbaDeflYLI", "9Y-0nWVdBH4", "1bGOgY1CmiU", "MiY5auB3OWg", "5V430M59Yn8", "lp-EO5I60KA", "450p7goxZqg", "izGwDsrQ1eQ"]
spiritualVideos = ["8YumIy3rMDY", "vMfr6Yb04E4", "CmkFt2HSkao", "JEvy8mROAj0", "tebjshm7f_I", "ElVC6rfX3Z8", "COQ6cni_TG8", "zC617kE1maU"]

# checking to see if the video is okay
def is_url_ok(url):
    return 200 == requests.head(url).status_code

# linking the html file and python file
@app.route('/')
def home():
    return render_template("homepage.html")

# redirects to happy songs
@app.route('/happyLink', methods = ['GET', 'POST'])
def happy():
    #whenever the happy link is called, a new index is created to match the one in the list of mood videos
    index = random.randint(0, len(happyVideos) - 1)
    # this will be passed in to happyLink.html
    return render_template("happy.html", happyID = happyVideos[index])

# redirects to heartbroken songs                        
@app.route('/heartbrokenLink', methods = ['GET','POST'])
def heartbroken():
    index = random.randint(0, len(heartbrokenVideos) - 1)
    return render_template("heartbroken.html", heartbrokenID = heartbrokenVideos[index])
    
# redirects to angry songs
@app.route('/angryLink', methods = ['GET', 'POST'])
def angry():
    index = random.randint(0, len(angryVideos) - 1)
    return render_template("angry.html", angryID = angryVideos[index])

# redirects to energetic songs
@app.route('/energeticLink', methods = ['GET', 'POST'])
def energetic():
    index = random.randint(0, len(energeticVideos) - 1)
    return render_template("energetic.html", energeticID = energeticVideos[index])

# redirects to mellow songs
@app.route('/mellowLink', methods = ['GET', 'POST'])
def mellow():
    index = random.randint(0, len(mellowVideos) - 1)
    return render_template("mellow.html", mellowID = mellowVideos[index])

# redirects to depressing songs    
@app.route('/depressingLink', methods = ['GET', 'POST'])
def depressing():
    index = random.randint(0, len(depressingVideos) - 1)
    return render_template("depressed.html", depressingID = depressingVideos[index])

# redirects to groovy songs  
@app.route('/groovyLink', methods = ['GET', 'POST'])
def groovy():
    index = random.randint(0, len(groovyVideos) - 1)
    return render_template("groovy.html", groovyID = groovyVideos[index])

# redirects to romantic songs
@app.route('/romanticyLink', methods = ['GET', 'POST'])
def romantic():
    index = random.randint(0, len(romanticVideos) - 1)
    return render_template("romantic.html", romanticID = romanticVideos[index])

# redirects to spiritual songs  
@app.route('/spiritualLink', methods = ['GET', 'POST'])
def spiritual():
    index = random.randint(0, len(spiritualVideos) - 1)
    return render_template("spiritual.html", spiritualID = spiritualVideos[index])

# making sure it runs?
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port = int(os.getenv('PORT', 8080)), host = os.getenv('IP', '0.0.0.0'))
