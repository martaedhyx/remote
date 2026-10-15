# Edhy Robot Remote

This project can share a laptop screen to a phone. Remote mouse/keyboard control is an optional experimental feature and requires a local agent on the laptop.

## Setup on the Windows 7 laptop

1. Install Python 3.8 (the last Python series supporting Windows 7) and ensure the Python Launcher `py` is installed.
2. Download this repository to the laptop, or download `remote_agent.py`, `requirements.txt`, and `JALANKAN-AGENT.bat` into the same folder.
3. Double-click `JALANKAN-AGENT.bat` and keep its black command window open. It installs the dependencies and starts the local agent.
4. Open the Edhy website on the laptop, press **Mulai berbagi layar**, choose the screen, and accept the separate mouse/keyboard permission prompt if you want control.
5. On the phone, open the same Edhy website, enter the laptop's six-digit ID and six-letter password, and connect.
6. Tap the displayed video to click; move your finger to move the cursor. Use the text field and buttons to send text, Enter, or Esc.

## Important limitations

- This is an experimental prototype; it has not been tested on the owner's devices yet.
- The laptop must stay on, online, and running both the browser sharing session and the local agent.
- If the agent isn't running, screen viewing may work but remote control will not.
- The typing feature is intended for basic ASCII text. Some non-English characters may not be typed correctly.
- Never run the agent on a computer you do not own or have permission to control. Stop it with Ctrl+C or close its window when finished.
- GitHub Pages only hosts the web interface; it cannot install or start the laptop agent automatically.
