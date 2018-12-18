# youtube-auto-cc-set-language
Allows you to set language of youtube auto generated subtitles


[![License](https://img.shields.io/badge/License-MIT-orange.svg)](https://github.com/Charlkie/PyMail/blob/master/LICENSE)
![](https://img.shields.io/badge/Version-Alpha%200.0.1-brightgreen.svg)


If you have any question, open an issue :-)

Pull requests are welcome

Tested on Windows

Setup
-----

1. Install ffmpeg
2. install mkvtoolnix
2. Install python package:

  
       pip install pymediainfo
4. If not on Windows install MediaInfo
https://mediaarea.net/en/MediaInfo
    


Usage
------------

modify config in ytsetcc.py:
    
    # CONFIGURATION

    inproper_cc_video_id = ""  # video id, which you want to have another language auto generated CC

    proper_cc_video_id   = "wFUxiIjp-Nk"    # video id which has auto CC in desired language 
    # examples: 
    # "wFUxiIjp-Nk" for English
    # "yTIFbqBP6B4" for Russian


2. Run  ytsetcc.py

3. Upload generated video to YouTube

4. Wait few hours for subtitles to be generated





