import unittest
from src.video_processing import process_videos

class TestVideoProcessing(unittest.TestCase):
    def test_process_videos(self):
        video_files = ["data/video1.mp4", "data/video2.mp4"]
        output_file = "data/test_output_video.mp4"
        process_videos(video_files, output_file)
        # Add assertions to verify the output

if __name__ == "__main__":
    unittest.main()
