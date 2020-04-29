from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image


source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
thumbnails_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails_per_frame")
os.makedirs(thumbnail_dir, exist_ok = True)
os.makedirs(thumbnails_per_frame_dir, exist_ok = True)

clip = VideoFileClip(source_path)
print(clip.reader.fps)#ammount of frames shown per second
print(clip.reader.nframes) #number of frames
print(clip.duration) # in seconds

duration = clip.duration
max_duration = int(duration + 1)



for i in range(0, max_duration):
    # print(f"frame at {i} seconds")
    frame = clip.get_frame(int(i))
    # print(frame)
    new_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")
    # print(f"frame at {i} seconds saved at {new_img_filepath}")
    new_img =  Image.fromarray(frame)
    new_img.save(new_img_filepath)


for i,frame in  enumerate(clip.iter_frames()):
    # print(f"frame at {i} seconds")
    # frame = clip.get_frame(int(i))
    # # print(frame)
    new_img_filepath = os.path.join(thumbnails_per_frame_dir, f"{i}.jpg")
    # print(f"frame at {i} seconds saved at {new_img_filepath}")
    new_img =  Image.fromarray(frame)
    new_img.save(new_img_filepath)
    