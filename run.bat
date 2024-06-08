@echo off
setlocal

:: Get the current working directory
set cwd=%cd%

:: Define the path to the Streamlit script
set script_path=%cwd%\GROQ.py

:: Command to run the Streamlit script
set command=streamlit run "%script_path%"

:: Print the current directory and script path for debugging
echo Current Directory: %cwd%
echo Script Path: %script_path%

:: Run the Streamlit script
start "" cmd /c %command%

:: End the script
exit
