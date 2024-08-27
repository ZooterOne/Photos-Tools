<div align="center">
    <img src="assets/logo.png" alt="Photos Tools">
</div>

<h1 align="center">Photos Tools</h1>

## 🤔 About

Various tools to manage photos.
Supported photo formats are PNG, JPG and HEIC.

### 🔹DuplicatePhotosFinder

Process photos in a given folder and all its sub-folders, and generate a csv file reporting all duplicates.

```
DuplicatePhotosFinder [--directory <directory>] [--output <filename>.csv]
```

&nbsp;&nbsp;&nbsp;&nbsp;_directory: The path of the directory to process._

&nbsp;&nbsp;&nbsp;&nbsp;_output: The path of the output csv file to generate._

### 🔹SortPhotos

Sort photos into folders named using date and location from photo Exif data.

```
SortPhotos [-directory <directory>] [-output <output>] [--location] [--undefined <name>] [--copy]
```

&nbsp;&nbsp;&nbsp;&nbsp;_directory: The path of the directory to process._

&nbsp;&nbsp;&nbsp;&nbsp;_output: The path of the directory to copy or move sorted photo into._

&nbsp;&nbsp;&nbsp;&nbsp;_location: Use location in addition to date to name folders._

&nbsp;&nbsp;&nbsp;&nbsp;_undefined: The folder name to use when Exif data cannot be retrieved. Modification date will be used in such case._

&nbsp;&nbsp;&nbsp;&nbsp;_copy: Copy the photos instead of moving them._

## 📝 Implementation

![LANGUAGE](https://img.shields.io/badge/python-royalblue?style=for-the-badge&logo=python&logoColor=white)
![EDITOR](https://img.shields.io/badge/vscode-coral?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![OS](https://img.shields.io/badge/linux-yellowgreen?style=for-the-badge&logo=linux&logoColor=white)

### ⚙ Installation

 Clone the project and go to the project directory.
 ``` bash
 git clone https://github.com/ZooterOne/Photos-Tools
 cd Photos-Tools
 ```

 Setup the Python environment.
 ``` bash
 python -m venv .venv
 source .venv/bin/activate
 pip install -r requirements.txt 
 ```

 ### 🏃‍♂️ Run script
 
 ``` bash
 python <script name>.py <parameters>
 ```

### 🧪 Run tests

 ``` bash
 python -m unittest -v
 ```

 ## 💡 Future developments

 - Use perceptual hash algorithm to detect duplicate photos.
 - Add UI to DuplicatePhotoFinder.
 - Develop a tool using Segment Anything Model.