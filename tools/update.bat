@echo off
cd/d "%~dp0"

move /y ed6_fc_text_update.json ed6_fc_text.json
call gentextbin.py
move /y ed6fc.text "D:\Game\Steam\steamapps\common\Trails in the Sky FC"
start "" "D:\Game\Steam\steamapps\common\Trails in the Sky FC\ed6_win.exe"
