Set WshShell = CreateObject("WScript.Shell")
WshShell.Run """" & "C:\PATH TO BAT FILE.bat" & """", 0, False
Set WshShell = Nothing

' Put this in your startup if you want it to startup with PC. this is a vbs trick to hide console (cmd) while the python script runs.