# Edhy Remote Control Agent
# Compatible target: Python 3.8 on Windows 7. Keep this program running only while needed.
import asyncio
import json
import websockets
import pyautogui

ALLOWED_ORIGINS = ["https://martaedhyx.github.io"]
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.01

async def handler(websocket, path):
    print("Edhy web page connected. Keep this window open.")
    async for raw in websocket:
        try:
            cmd = json.loads(raw)
            action = cmd.get("action")
            width, height = pyautogui.size()
            if action == "click":
                x = max(0, min(width - 1, int(float(cmd.get("x", 0)) * width)))
                y = max(0, min(height - 1, int(float(cmd.get("y", 0)) * height)))
                pyautogui.moveTo(x, y, duration=0)
                button = "right" if cmd.get("button") == "right" else "left"
                pyautogui.click(x, y, button=button)
            elif action == "type":
                text = str(cmd.get("text", ""))[:500]
                # pyautogui.write supports ASCII reliably on older Windows.
                pyautogui.write(text, interval=0.005)
            elif action == "key":
                key = str(cmd.get("key", "")).lower()
                if key in ("enter", "esc", "tab", "backspace", "space", "up", "down", "left", "right"):
                    pyautogui.press(key)
        except Exception as exc:
            print("Command ignored:", exc)

async def main():
    print("EDHY REMOTE AGENT")
    print("Local-only control bridge at 127.0.0.1:8765")
    print("Stop with Ctrl+C. Do not share access codes with strangers.")
    async with websockets.serve(handler, "127.0.0.1", 8765, origins=ALLOWED_ORIGINS, max_size=4096):
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nEdhy agent stopped.")
