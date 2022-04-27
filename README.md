<p align=center>
<img target = "banner" src="https://raw.githubusercontent.com/LowSugarCoke/SNReminder/main/banner.PNG">
</p>
<p align=center>
<a target="badge" href="https://github.com/LowSugarCoke/Pixiv-Downloader/blob/main/img/banner.png" title="python version"><img src="https://img.shields.io/badge/python-v3.9.7-brightgreen"></a>
<a target="badge" href="https://github.com/LowSugarCoke/Pixiv-Downloader/blob/main/img/banner.png" title="python version"><img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" width=85/></a>  
</p>

>SN Reminder update the anime episode based on your saving local data. It shows the latest anime list on the application. 

SN website:https://sn-video.com/index.html

# Install
## Release 
Download exe as below:

https://github.com/LowSugarCoke/SNReminder/releases/tag/v1.0.0

## Download source code
In order to use pixiv-downloader, make sure that you have python 3.9.7 and python packages as below:
* requests 2.26.0
* tk 0.1.0
* pyinstaller 4.10

```
$ git clone https://github.com/LowSugarCoke/SNReminder.git
```
## Usage
### Visual Studio Code
Download VSCode https://code.visualstudio.com/

Download python https://www.python.org/

After installing VScode and Python, download the extension in VSCode as follow:
* python
* python for vscode
* code runner

Done it and Run code

### Build exe
Using terminal and pyinstaller to build exe
```
$ pyinstaller -F sn_reminder.py -c --icon=logo.ico --noconsole
```
