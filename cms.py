"""
This python script will be used as a CMS (Content Management System)
 for the website. It will be used to manage the content of the website.
 - Creating new galleries
 - Creating new posts/journal entries
"""

import os
import yaml
import frontmatter
import json
from datetime import datetime

BASE_GALLERY_PATH = "gallery/"
BASE_IMAGE_GALLERY_PATH = "img/galleries/"
BASE_ALBUM_PATH = "img/albums/"

DEFAULT_FRONTMATTER = {
    "layout": "page",
    "title": "",
    "description": "",
    "active": "gallery",
    "date": "",
    "header_image": "",
    "images": [
    ]
}

IMAGE_EXT = [".JPG",".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"]

def print_line():
  print("-" * 30)


def get_images(path):
  images = []
  for root, dirs, files in os.walk(path):
    for file in files:
      print(file)
      if file.endswith(tuple(IMAGE_EXT)):
        images.append(os.path.join(root, file))
  return images


def create_gallery():
  print_line()
  print("Creating a new gallery")
  gallery_name = input("Enter the name of the gallery: ")
  gallery_description = input("Enter the description of the gallery: ")
  print_line()
  image_input = input("Enter the path to the image(s) (Needs to be a separate folder): ")
  images_list = get_images(image_input)

  folder_name = gallery_name.lower().replace(" ", "_")

  path = os.path.join(BASE_GALLERY_PATH, folder_name)
  # os.mkdir(path)
  img_path = os.path.join(BASE_IMAGE_GALLERY_PATH, folder_name)
  # os.mkdir(img_path)

  # # Create a frontmatter for the gallery
  frontmatter_data = DEFAULT_FRONTMATTER.copy()
  frontmatter_data["title"] = gallery_name
  frontmatter_data["description"] = gallery_description
  frontmatter_data["date"] = datetime.today().strftime('%Y-%m-%d')
  for i, image in enumerate(images_list):
    # Copy the image to the gallery folder
    image_name = os.path.basename(image)
    new_image_path = os.path.join(img_path, image_name)
    # shutil.copy(image, new_image_path)
    frontmatter_data["images"].append({
      "image_path": new_image_path,
      "caption": "REPLACE_ME",
      "copyright": "© photorama"
    })


  with open(os.path.join("_templates/", "gallery_body.html"), "r") as f:
    content = f.read()

  file = frontmatter.Post(content=content, handler=None, **frontmatter_data)
  print(frontmatter.dumps(file))

  # Save the gallery to the database
  # Database code will be added later


if __name__ == '__main__':
  print("Welcome to the CMS for Photorama")
  print_line()
  print("Please select an option:")
  print("1. Create a new gallery")
  print("2. Create a new post/journal entry")
  print("3. Exit")

  # option = input("Enter your choice: ")
  option = "1"
  if option == "3":
    print("Exiting CMS")
    exit()

  if option == "1":
    create_gallery()
