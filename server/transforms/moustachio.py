#!/bin/python2
import sys
import requests
import urllib
import cStringIO
from pprint import pprint
from PIL import Image, ImageStat
from face_client.face_client import FaceClient

from secrets import API_KEY, API_SECRET
MOUSTACHE_PATH = "transforms/moustache.png"

def process_image(image_url, moustache, response):
    pprint(response)

    face = Image.open(cStringIO.StringIO(urllib.urlopen(image_url).read()))

    # quit if no faces detected
    if len(response['photos']) == 0 or len(response['photos'][0]['tags']) == 0:
        print 'No faces.'
        return face

    image_width = response['photos'][0]['width']
    image_height = response['photos'][0]['height']

    response = response['photos'][0]['tags'][0]

    # quit if not looking at camera
    if abs(response['yaw']) > 30:
        print 'Bad yaw.'
        return face

    roll = response['roll']

    face_width = response['width']
    face_height = response['height']

    face_x = response['center']['x']
    face_y = response['center']['y']

    mouth = response['mouth_center']
    nose = response['nose']

    # quit if unsure of face
    if mouth['confidence'] < 40 and nose['confidence'] < 40:
        print 'Not sure.'
        return face

    #vertical space to fit moustache.
    noseToMouth = abs((mouth['y'] - nose['y']) * image_height * 0.01)

    moustache = scale_moustache(moustache, noseToMouth)
    moustache = rotate_moustache(moustache, roll)

    pos = (int(nose['x'] * image_width * 0.01 - moustache.size[0]/2), int(nose['y'] * image_height * 0.01 ))

    paste_on(face, moustache, pos)
    return face

def scale_moustache(moustache, height):
    (m_width, m_height) = moustache.size
    scale = height / m_height
    return moustache.resize((int(m_width * scale), int(m_height * scale)))

def rotate_moustache(moustache, roll):
    return moustache.rotate(-1 * roll, resample=Image.BICUBIC, expand=True)

def paste_on(face, moustache, pos):
    face.paste(moustache, pos, moustache)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        image_url = sys.argv[1]

        client = FaceClient(API_KEY, API_SECRET)
        response = client.faces_detect(image_url)
        moustache = Image.open(MOUSTACHE_PATH)
        
        face = process_image(image_url, moustache, response)
        face.save('/tmp/out.png')
