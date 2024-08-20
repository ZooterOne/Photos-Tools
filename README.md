<div align="center">
    <img src="assets/logo.png" alt="Photos Tools">
</div>

<h1 align="center">Photos Tools</h1>

## 🤔 About

Various tools to manage photos.

### 🔹DuplicatePhotosFinder

Process photos in a given folder and all its sub-folders, and generate a csv file reporting all duplicates.

```
DuplicatePhotosFinder [--directory <directory>] [--output <filename>.csv]
```

&nbsp;&nbsp;&nbsp;&nbsp;_directory: The path of the directory to process._

&nbsp;&nbsp;&nbsp;&nbsp;_output: The path of the output csv file to generate._

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