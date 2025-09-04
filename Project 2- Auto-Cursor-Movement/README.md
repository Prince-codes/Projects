
# Foreground Window Mouse Mover

This project provides a Python script to automatically move your mouse cursor by smoothly dragging it within the currently active (foreground) window at regular intervals. This helps prevent your computer from going idle or keeps certain applications active.

## Features
- **Auto-install requirements:** The script will automatically install any required dependencies (`pywinauto`, `tkinter`) if they are not already installed.
- **Professional UI:** When you run the script, a modern, cool-looking Tkinter dialog will appear asking you for the interval (in seconds) between cursor moves.
- **Smooth cursor dragging:** The cursor is smoothly dragged from its current position to a random location anywhere on your screen, rather than instantly jumping.

## Usage
1. Run the script:
   ```sh
   python cursor-movement.py
   ```
2. Enter the interval (in seconds) in the dialog box and click OK.
3. The script will move your mouse cursor smoothly anywhere on your screen at your chosen interval.

## Notes
- Works for any screen setup and moves the cursor anywhere on your desktop.
- The cursor movement is animated and visually smooth.
- No Zoom or browser automation is included.
