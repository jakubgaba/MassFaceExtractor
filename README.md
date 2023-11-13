<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="FaceExtractor" />

  &#xa0;

  <!-- <a href="https://faceextractor.netlify.app">Demo</a> -->
</div>

<h1 align="center">FaceExtractor</h1>

<p align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/jakubgaba/MassFaceExtractor?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/jakubgaba/MassFaceExtractor?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/{{YOUR_GITHUB_USERNAME}}/faceextractor?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/{{YOUR_GITHUB_USERNAME}}/faceextractor?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/{{YOUR_GITHUB_USERNAME}}/faceextractor?color=56BEB8" /> -->
</p>



<h4 align="center"> 
	🚧  FaceExtractor 🚀 Under construction...  🚧
</h4> 

<hr>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="https://github.com/jakubgaba" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Extracting face from a directory, after that images are gonna be scaled. To controll scale margin you can change margin inside of a code.
```bash
margin = 50
```

## :sparkles: Features ##

:heavy_check_mark: haarcascade_frontalface_default.xml;\
:heavy_check_mark: haarcascade_profileface.xml;\
:heavy_check_mark: Scale;\
## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) installed.
1. Python: A recent version of Python installed (Python 3.6 or newer is recommended).
2. OpenCV Library: Install OpenCV for Python. You can do this via pip:
```bash
pip install opencv-python
```
3. Write Permissions: The script will attempt to create a directory (./test) and write output images there, so ensure you have the necessary permissions in your working environment.
4. Secure all path correct !.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/jakubgaba/MassFaceExtractor

# Access
$ cd MassFaceExtractor

# How to
$ Create two files 'input' and 'output'.
$ Open file extractFaceWithoutResize.py 
$ Modify directory and out_src as you wish. out_src is for output and directory is for input, where are you images stored.
$ Modify directory and out_src as you wish. out_src is for output and directory is for input, where are you images stored.

# Run the project
$ python3 extractFaceWithoutResize.py
