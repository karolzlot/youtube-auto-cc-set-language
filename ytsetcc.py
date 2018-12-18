import os ,shutil, logging as log
from subprocess import run
from pymediainfo import MediaInfo


def main():

    # CONFIGURATION

    inproper_cc_video_id = ""  # video id, which you want to have another language auto generated CC

    proper_cc_video_id   = "wFUxiIjp-Nk"    # video id which has auto CC in desired language 
    # examples: 
    # "wFUxiIjp-Nk" for English
    # "yTIFbqBP6B4" for Russian

    # default values below should work in most cases
    videoFormatCode = 247 
    # you can try also:
    #  247 or 136 for 720p 
    #  248 or 137 for 1080p
    #
    audioFormatCode = 140
    # you can try also: 140, 251, 171
    #   
    #   it should work if all video has at least 720p resolution, 
    #   however if it does not work use command below to find another format numbers: 
    #       youtube-dl -F q28W7N6Th58
    #   



####################
    # You don't need to change code below

    videoFormatCode=str(videoFormatCode)
    audioFormatCode=str(audioFormatCode)

    filename1 = run(r'youtube-dl --get-filename -o "%(title)s (subtitles).mkv" '+ inproper_cc_video_id +" --restrict-filenames", shell=True,check=True ,capture_output=True) 
    filename2= filename1.stdout.decode().strip()
    output_video_filename = filename2.replace("'", "")

    run(r'youtube-dl -o "./temp/inproper_cc.%(ext)s" --merge-output-format mkv  '+ inproper_cc_video_id +' -f '+ videoFormatCode +'+'+ audioFormatCode, shell=True, check=True) 
    run(r'youtube-dl -o "./temp/proper_cc.%(ext)s" --merge-output-format mkv '+ proper_cc_video_id +' -f '+ videoFormatCode +'+'+ audioFormatCode, shell=True, check=True) 
    run(r'youtube-dl -o "./temp/cc.%(ext)s" q28W7N6Th58 --merge-output-format mkv -f '+ videoFormatCode +'+'+ audioFormatCode, shell=True, check=True) 
    
    inproper_cc_duration = int(MediaInfo.parse('./temp/inproper_cc.mkv').tracks[0].duration/1000)
    proper_cc_duration = int(MediaInfo.parse('./temp/proper_cc.mkv').tracks[0].duration/1000)

    ratio= int(((inproper_cc_duration+5*60)/proper_cc_duration)+1)

    merge_string= ' +./temp/proper_cc.mkv '*ratio
    run(r'mkvmerge -o "./Upload_this_to_Youtube/'+ output_video_filename +'" ./temp/inproper_cc.mkv  +./temp/cc.mkv '+merge_string) 
    print("- - -")
    print("Success! Now upload video to Youtube, then wait few hours for subtitles to be generated")
    print("- - -")
    shutil.rmtree("./temp/")



if __name__ == '__main__':
    main()
