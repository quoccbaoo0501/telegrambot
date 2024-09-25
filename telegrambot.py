import pyautogui
import time
import win32gui
import win32con

def find_telegram_window():
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and 'Telegram' in win32gui.GetWindowText(hwnd):
            hwnds.append(hwnd)
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    if hwnds:
        print(f"Found Telegram window with handle: {hwnds[0]}")
        return hwnds[0]
    else:
        print("No Telegram window found")
        return None

def activate_telegram():
    print("Attempting to activate Telegram...")
    telegram_hwnd = find_telegram_window()
    if telegram_hwnd:
        win32gui.SetForegroundWindow(telegram_hwnd)
        print("Telegram window activated")
    else:
        print("Telegram window not found, searching for icon...")
        # Try to find and click Telegram icon in taskbar
        telegram_icon = pyautogui.locateOnScreen('telegram_icon.png')
        if telegram_icon:
            pyautogui.click(telegram_icon)
            print("Clicked Telegram icon")
        else:
            print("Couldn't find Telegram window or icon")
            return False
    return True

def select_channel(channel_name):
    print(f"Searching for channel: {channel_name}")
    channel_loc = pyautogui.locateOnScreen(f'{channel_name}.png')
    if channel_loc:
        pyautogui.click(channel_loc)
        print(f"Clicked on channel: {channel_name}")
    else:
        print(f"Couldn't find channel: {channel_name}")
        return False
    return True

def click_play_button():
    print("Searching for Play button...")
    play_button = pyautogui.locateOnScreen('play_button.png')
    if play_button:
        pyautogui.click(play_button)
        print("Clicked Play button")
        time.sleep(2)  # Wait for potential popup
        print("Checking for OK button...")
        ok_button = pyautogui.locateOnScreen('ok_button.png')
        if ok_button:
            pyautogui.click(ok_button)
            print("Clicked OK button")
    else:
        print("Couldn't find Play button")
        return False
    return True

def click_play_game():
    print("Searching for Play Game button...")
    play_game_button = pyautogui.locateOnScreen('play_game_button.png')
    if play_game_button:
        pyautogui.click(play_game_button)
        print("Clicked Play Game button")
    else:
        print("Couldn't find Play Game button")
        return False
    return True

def auto_click_game(duration=60):
    print(f"Starting auto-click for {duration} seconds...")
    start_time = time.time()
    clicks = 0
    while time.time() - start_time < duration:
        pyautogui.click()
        clicks += 1
        time.sleep(0.1)  # Adjust this value to control click frequency
    print(f"Auto-click finished. Total clicks: {clicks}")

def main():
    print("Starting Telegram bot...")
    while True:
        print("\n--- New cycle starting ---")
        if not activate_telegram():
            print("Failed to activate Telegram. Exiting...")
            break
        
        if not select_channel("Binance Moonbix"):
            print("Failed to select channel. Exiting...")
            break
        
        if not click_play_button():
            print("Failed to click Play button. Exiting...")
            break
        
        if not click_play_game():
            print("Failed to click Play Game button. Exiting...")
            break
        
        auto_click_game()
        
        print("Waiting 30 seconds before playing again...")
        time.sleep(30)
    print("Bot has finished execution.")

if __name__ == "__main__":
    main()
