from flask import Flask, render_template
#from potato_detection import hb_detect_potatoes
#import shutil
#import os
#import time

# Set to True to use Cam device and run on Azure.
# Set to False to run a test with a single local image.
#production = False

#if production:
#    from readCam import takePicture

#def takePicture():
#    pass

#segment_dir = 'segmented'

app = Flask(__name__)

@app.route('/')
def kickstart():
   return render_template('start.html')


@app.route('/capture')
def get_ses():
    currentfile =  takePicture()
    return render_template("result.html", user_image = currentfile)



if __name__ == '__main__':
    app.run(debug=True)
