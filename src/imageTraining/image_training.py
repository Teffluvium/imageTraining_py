"""Image Training stuff"""
# from dataclasses import dataclass
# from pathlib import Path

# import cv2


# @dataclass
# class ImageTraining:
#     """Generate a training set for the image recognition model."""

#     # Image modification parameters
#     num_training_images: int = 10  # Number of training images
#     output_width: int = 256  # Output image width
#     output_height: int = 256  # Output image height
#     fgd_scale: float = (
#         0.75  # Percentage that foreground image occupies relative to background
#     )
#     roi_scale: float = 0.75  # Percentage of image to crop and use as the background
#     warp_scale: float = (
#         0.3  # Amount of distrotion/perspective warp. 0.0 is no warp, 1.0 is full warp
#     )
#     angle_max: float = 30.0  # Maximum angle of rotation for the foreground image

#     # Custom Vision parameters
#     tag_id: str = (
#         "===@@@ tagId @@@==="  # Placeholder for the tagIds in the image JSON file
#     )
#     tag_list_file: str = "training.json"  # Output JSON file for Custom Vision

#     # Paths and stuff
#     bgd_path: Path = Path("bgd_images")
#     src_img_file: Path = Path("src_image.jpg")
#     output_training_path: Path = Path("training_images")

#     def generate_training_images(self):
#         pass
