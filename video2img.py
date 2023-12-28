import cv2
import os

def video_to_images(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get the frames per second (fps) and frame width/height
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print(f"FPS: {fps}, Width: {width}, Height: {height}, Total Frames: {total_frames}")

    # Loop through each frame and save it as an image
    for frame_num in range(total_frames):
        ret, frame = cap.read()

        if not ret:
            break

        # Save the frame as an image
        image_path = os.path.join(output_folder, f"person_dog_{frame_num:04d}.png")
        cv2.imwrite(image_path, frame)

        # Display progress
        if frame_num % 100 == 0:
            print(f"Processing frame {frame_num}/{total_frames}")

    # Release the video capture object
    cap.release()

    print(f"Frames saved to {output_folder}")

if __name__ == "__main__":
    # Specify the path to the input video and output folder
    video_path = r"runs\detect\predict11\person_dog.avi"
    output_folder = r"runs\video2images"

    # Convert the video to images
    video_to_images(video_path, output_folder)
