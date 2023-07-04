<h1 align="center">Welcome to path-maker 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.1-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/alessandroDeIturbe/path-maker/wiki" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/alessandroDeIturbe/path-maker/blob/main/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

# pfm - Python File Manager

> pfm is a command-line tool that allows you to create files and directories in an easy and efficient way. It provides a simple interface to create files and directories with customizable names and locations.

Examples:
  pfm file.txt                      - Create a file named "file.txt" in the current directory.
  pfm folder/subfolder/             - Create a directory structure with a folder named "folder" and a subfolder named "subfolder".
  pfm file1.txt,file2.txt,folder/   - Create multiple files and a directory in the same location.

Note:
  - If the specified file or directory already exists, an error message will be displayed.
  - If the starting folder specified by --start-folder does not exist, an error message will be displayed. You can choose to continue in the current folder by entering 'y'.


### 🏠 [Homepage](https://github.com/alessandroDeIturbe/path-maker)

## Install

  ```sh
  pip install .
  ```

## Usage

  ```sh
  pfm <path> [--start-folder <start-folder>]
  ```

## Arguments

  <path>                Path of the file or directory to create. If multiple path are separated by commas, files and directories will be created in the same location.

## Options:

  --start-folder <start-folder>         Starting folder path (optional). If specified, pfm will navigate to this folder before creating the files or directories.

## Examples:

  pfm file.txt                      - Create a file named "file.txt" in the current directory.
  pfm folder/subfolder/             - Create a directory structure with a folder named "folder" and a subfolder named "subfolder".
  pfm file1.txt,file2.txt,folder/   - Create multiple files and a directory in the same location.

## Note:

  - If the specified file or directory already exists, an error message will be displayed.
  - If the starting folder specified by --start-folder does not exist, an error message will be displayed. You can choose to continue in the current folder by entering 'y'.



## Author

👤 **Alessandro De Iturbe**

- Github: [@alessandroDeIturbe](https://github.com/alessandroDeIturbe)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/alessandroDeIturbe/path-maker/issues).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2023 [Alessandro De Iturbe](https://github.com/alessandroDeIturbe).<br />
This project is [MIT](https://github.com/alessandroDeIturbe/path-maker/blob/main/LICENSE) licensed.
