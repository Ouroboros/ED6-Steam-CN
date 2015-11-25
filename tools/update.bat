@echo off
cd/d "%~dp0"

call gentextbin.py
move /y ed6fc.text "D:\Game\Steam\steamapps\common\Trails in the Sky FC"
start "" "D:\Game\Steam\steamapps\common\Trails in the Sky FC\ed6_win_crack.exe"
