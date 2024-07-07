from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip

def process_videos(video_files, output_file):
    clips = [VideoFileClip(video) for video in video_files]

    # Resize clips (optional)
    clips = [clip.resize(height=360) for clip in clips]

    # Combine clips
    final_clip = concatenate_videoclips(clips)

    # Create a text clip
    txt_clip = TextClip("This is a text overlay", fontsize=24, color='white')
    txt_clip = txt_clip.set_pos('center').set_duration(10)

    # Overlay the text on the final clip
    final_video = CompositeVideoClip([final_clip, txt_clip])

    # Export the final video
    final_video.write_videofile(output_file, codec="libx264")
