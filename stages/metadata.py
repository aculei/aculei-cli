import datetime
from PIL import Image
import exiftool
import re

from stages import moonphase

TAGS_FOR_CAMERA = ["Keywords", "Subject", "WeightedFlatSubject"]
TAGS_FOR_DATETIME = ["CreateDate", "DateCreated"]

def get_image_metadata(img: Image):
    """Get metadata from an image file."""
    with exiftool.ExifToolHelper() as et:
        try:
            metadata = {}
            filename = img.filename
            metadata['filename'] = filename
            tags = TAGS_FOR_CAMERA + TAGS_FOR_DATETIME
            for d in et.get_tags([filename], tags=tags):
                for k, v in d.items():
                    metadata[k] = v
            
            # Now normalize metadata
            data = {} 
            pattern_datetime = re.compile(r'.*(CreateDate|DateCreated)$')
            pattern_camera = re.compile(r'.*(Keywords|Subject|WeightedFlatSubject)$')
            date_format = "%Y-%m-%d %H:%M:%S"
            exif_date_format = "%Y:%m:%d %H:%M:%S"
            for key in metadata:
                if pattern_datetime.match(key):
                    
                    if isinstance(metadata[key], datetime.datetime):
                        parsed_date = metadata[key].strftime(date_format)
                    else:
                        parsed_date = datetime.datetime.strptime(metadata[key], exif_date_format).strftime(date_format)
                    
                    data['datetime'] = parsed_date
                    break
                if pattern_camera.match(key):
                    data['camera'] = metadata[key]  
            
            # Calculate moon phase
            moon_phase = moonphase.phase(data['datetime'])
            data['moon_phase'] = moon_phase

            return data
        except Exception as e:
            print(e)
            return None

