import cv2
import os

def frames_to_video(frames_folder, output_video_path, fps):
    # Get the list of image files in the frames folder
    image_files = [f for f in os.listdir(frames_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

    if not image_files:
        print("No image files found in the specified folder.")
        return

    # Sort the image files based on their numerical names
    image_files.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

    # Get the dimensions of the first image
    first_image = cv2.imread(os.path.join(frames_folder, image_files[0]))
    height, width, _ = first_image.shape

    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Iterate through image files and write frames to the video
    for image_file in image_files:
        frame = cv2.imread(os.path.join(frames_folder, image_file))
        video_writer.write(frame)
        # print(image_file)
    # Release the video writer
    video_writer.release()

    print(f"Video successfully created: {output_video_path}")

if __name__ == "__main__":
    frames_folder = r"runs\plot_count_label"
    output_video_path = r"runs\imgs2video\person_dog.mp4"
    fps = 30  # Specify the desired frames per second (fps) for the output video

    # Replace "path/to/frames" with the path to your folder containing frames
    frames_to_video(frames_folder, output_video_path, fps)
