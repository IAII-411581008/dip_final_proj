def count_labels(annotation_file):
    # Read the annotation file and extract labels
    with open(annotation_file, 'r') as file:
        lines = [line.strip().split() for line in file]

    # Extract labels from the first column
    labels = [line[0] for line in lines]

    # Count occurrences of labels "0" and "16"
    label_counts = {"Person": labels.count("0"), "Dog": labels.count("16")}

    # Print the counts
    for label, count in label_counts.items():
        print(f"{label}: {count}")

import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

def plot_label_counts_on_image(image_path, annotation_file,frameIdx):
    # Read the annotation file and extract labels
    with open(annotation_file, 'r') as file:
        lines = [line.strip().split() for line in file]

    # Extract labels from the first column
    labels = [line[0] for line in lines]

    # Count occurrences of labels "0" and "16"
    label_counts = {"Person": labels.count("0"), "Dog": labels.count("16")}

    # Create an image with the counts displayed in the top left corner
    original_image = Image.open(image_path)
    
    # Create an ImageDraw object to add text to the image
    draw = ImageDraw.Draw(original_image)

    # Specify the font and size for the text (increased font size)
    font_size = 30
    font = ImageFont.truetype("arial.ttf", font_size)

    # Add text indicating the count of each label in the top left corner with bold, red text and line breaks
    text = ""
    draw.text((10, 10), f"ID: {411581008} \n", font=font, fill=(0, 255, 0))
    text += "\n"
    for label, count in label_counts.items():
        # Render the text twice for a bold effect
        if label == "Person":
           draw.text((10, 60), f"{label}: {count}", font=font, fill=(0, 255, 0))
        else:
            draw.text((10, 110), f"{label}: {count}", font=font, fill=(0, 255, 0))
        # draw.text((11, 11), f"{label}: {count}", font=font, fill=(255, 0, 0))

    final_image_path = os.path.join("runs\plot_count_label", f"person_dog_{frameIdx:04d}.png")
    original_image.save(final_image_path)

    # Display the final image
    # original_image.show()

import os
if __name__ == "__main__":
    
    annotationDir = r"E:\research_proj\dip_final_proj\ultralytics\runs\detect\predict11\labels"
    imgDir = r"E:\research_proj\dip_final_proj\ultralytics\runs\video2images"

    annotationFiles = os.listdir(annotationDir)
    imgFilenames = os.listdir(imgDir)
    
    for fileIdx in range(0,len(annotationFiles)):
        annotationFile = os.path.join(annotationDir, annotationFiles[fileIdx])
        imgFile = os.path.join(imgDir, imgFilenames[fileIdx])
        # Specify the path to your annotation file
        # annotation_file = r"E:\research_proj\dip_final_proj\ultralytics\runs\detect\predict11\labels\person_dog_1.txt"

        # Count and print the occurrences of labels "0" and "16"
        count_labels(annotationFile)

        image_path = r"E:\research_proj\dip_final_proj\ultralytics\runs\video2images\frame_0100.png"

        # Plot the label counts on the image
        plot_label_counts_on_image(imgFile, annotationFile,fileIdx)
