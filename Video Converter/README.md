# Video Converter
This script converts all video files into a directory from one format to another using ffmpeg, therefore ffmpeg is needed to run the script.
The script is written using Python 3

## Usage
python3 convert_video.py [-h] [--dir DIR] [-R] [-r] input_format out_format

Convert all video files from a directory from a format to another using ffmpeg.

positional arguments:
  input_format          video format of the already existing file
  out_format            video format of the new created file

optional arguments:
  -h, --help            show this help message and exit
  --dir DIR, -d DIR, --directory DIR
                        directory in which are the video files to convert (default current directory)
  -R, --recursive       run recursively in all subdirectories
  -r, --replace, --overrite, --delete, --overrite-original-file, --delete-original-file
                        overrite original file
