import os
import subprocess
import argparse

def convertDirFiles(directory, origin, dest):
    dir_content = os.listdir(directory)
    for i in dir_content:
        global recursive
        if i[-len(origin):]==origin:
            clean_name=i[:-len(origin)]
            #If the file does not have already an mp4 conversion
            if not str(clean_name+dest) in dir_content:
                try:
                    subprocess.run(["ffmpeg", "-i", str(directory+"/"+i), "-f", dest[1:], str(directory+"/"+clean_name+dest)])
                except:
                    print("ffmpeg error running ", "ffmpeg", "-i", str(directory+"/"+i), str(directory+"/"+clean_name+dest))
                
                global replace
                if replace:
                    try:
                        subprocess.run(["rm", str(directory+"/"+i)])
                    except:
                        print("ffmpeg error running ", "ffmpeg", "-i", str(directory+"/"+i), str(directory+"/"+clean_name+dest))
        elif recursive and os.path.isdir(directory+'/'+i):
            convertDirFiles(directory+"/"+i, origin, dest)


#main
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Convert all video files from a directory from a format to another using ffmpeg.')
    parser.add_argument('--dir','-d','--directory', default='.',
                    help='directory in which are the video files to convert (default current directory)')
    parser.add_argument('input_format', metavar='input_format', type=str,
                    help='video format of the already existing file')
    parser.add_argument('output_format', metavar='out_format', type=str,
                    help='video format of the new created file')
    parser.add_argument('-R','--recursive', action='store_true',
                    help='run recursively in all subdirectories')
    parser.add_argument('-r', '--replace', '--overrite', '--delete','--overrite-original-file', '--delete-original-file', action='store_true',
                    help='overrite original file')
    


    args = parser.parse_args()

    global replace
    replace = args.replace
    global recursive 
    recursive = args.recursive

    directory=args.dir
    if args.input_format[0]!='.':
        origin=str('.'+args.input_format)
    else:    
        origin=args.input_format
    
    if args.output_format[0]!='.':
        dest=str('.'+args.output_format)
    else:    
        dest=args.output_format

    convertDirFiles(directory, origin, dest)
    