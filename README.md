# **Digital Image Processing Final Project- Object Detection**

## Project Report
The project report is located in `Project_Report` Folder
<br/>
實驗報告書已放置於 `Project_Report` 資料夾中，請老師與助教點閱觀看，謝謝 ~
<br/>

## Student Information
- Student Name: 陳韋澎 Wei-Peng Tang
- Student ID: 411581008
- Institute: 智能系統研究所 Institute of Artificial Intelligence Innovation

## Software and Requirements
The experiments were accomplished by Python 3.10, the experimental setups are listed as follow:

### PC Setup:
- GPU: NVIDIA RTX 3080 (10 GB)
- CPU: Intel i9-12900K @3.20GHz
- DRAM: 64 GB

### Library and API Version:
- Cuda 11.2
- Cudnn 8.5.0
- Python 3.10
- Matlab R2022b
- Cmake 3.22.1
- Opencv-python 4.6.0
- Scipy 1.4.1
- Torch 1.8.0
- Tqdm 4.64.0


## Programming Structure 
![Programming Structure](https://github.com/IAII-411581008/dip_final_proj/blob/main/programming_structure.png)

## Installation 
Please install the enviroment as follows:
1. Clone the entire source code from the ultralytics official and install the required toolkits as follows:
    ```sh
    # clone ultralytics
    git clone https://github.com/ultralytics/ultralytics

    # toolkits installation
    pip install ultralytics
    
    ```

2. Clone our source code and the experimental results inside the ultralytics directory as follows:
    ```sh
    # cd to ultralytics
    cd ultralytics

    # clone dip_final_project
    git clone https://github.com/IAII-411581008/dip_final_proj.git

3. Lastly, make sure you have similar programming structure with [Programming Structure](https://github.com/IAII-411581008/dip_final_proj/blob/main/programming_structure.png).


## Run It
1. First, enhance the raw video by using `video_preprocessing.mlx` script and the proceeded results will be save at `.../ultralytics/runs/video2frame_pre`.

2. After that, you may predict your own testing video using the following command:
    ```sh
    # Leveraging pretrained YOLOv8X for detection
    yolo predict model=[MODEL_WEIGHTS] source=[TEST_VIDEO_PATH] conf=[CONFIDENCE_SCORE_THRESHOLD] iou=[IOU_THRESHOLD] show=True classes=[SPECIFIC_CLASSES] save_txt=True save_frames=True

    # For example, this experiment, we used the hyperparams as follows:
    yolo predict model=yolov8x.pt source=E:\research_proj\dip_final_proj\ultralytics\runs\frame2video_pre\frame2video_pre.mp4 show=True conf=0.2 classes=0,1,16,17 save_txt=True iou=0.2 save_frames=True
    ```

3. You may check the predicted results at `.../ultralytics/runs/detect/predict` folder.

4. Subsequently, you may plot the number of each class on the top left of video by modifying the video and annotation paths of `plot_num_classes.py` script as follows:
    ``` python
    # modify these lines to your output dir
    video_path = r"runs\detect\[PRIDICTED_RESULT_DIR]\[PREDICTED_VIDEO].avi"
    annotationDir = r"\runs\detect\[PRIDICTED_RESULT_DIR]\labels"
    ```

5. Lastly, you may find the final predicted video at `runs\imgs2video` folder.
