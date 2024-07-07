from video_processing import process_videos

if __name__ == "__main__":
    video_files = ["data/video1.mp4", "data/video2.mp4"]
    output_file = "data/output_video.mp4"
    process_videos(video_files, output_file)
