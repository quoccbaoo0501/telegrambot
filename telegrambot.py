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
    return hwnds[0] if hwnds else None

def activate_telegram():
    telegram_hwnd = find_telegram_window()
    if telegram_hwnd:
        win32gui.SetForegroundWindow(telegram_hwnd)
    else:
        # Try to find and click Telegram icon in taskbar
        telegram_icon = pyautogui.locateOnScreen('telegram_icon.png')
        if telegram_icon:
            pyautogui.click(telegram_icon)
        else:
            print("Couldn't find Telegram window or icon")
            return False
    return True

def select_channel(channel_name):
    channel_loc = pyautogui.locateOnScreen(f'{channel_name}.png')
    if channel_loc:
        pyautogui.click(channel_loc)
    else:
        print(f"Couldn't find channel: {channel_name}")
        return False
    return True

def click_play_button():
    play_button = pyautogui.locateOnScreen('play_button.png')
    if play_button:
        pyautogui.click(play_button)
        time.sleep(2)  # Wait for potential popup
        ok_button = pyautogui.locateOnScreen('ok_button.png')
        if ok_button:
            pyautogui.click(ok_button)
    else:
        print("Couldn't find Play button")
        return False
    return True

def click_play_game():
    play_game_button = pyautogui.locateOnScreen('play_game_button.png')
    if play_game_button:
        pyautogui.click(play_game_button)
    else:
        print("Couldn't find Play Game button")
        return False
    return True

def auto_click_game(duration=60):
    start_time = time.time()
    while time.time() - start_time < duration:
        pyautogui.click()
        time.sleep(0.1)  # Adjust this value to control click frequency

def main():
    while True:
        if not activate_telegram():
            break
        
        if not select_channel("Binance Moonbix"):
            break
        
        if not click_play_button():
            break
        
        if not click_play_game():
            break
        
        auto_click_game()
        
        print("Waiting 30 seconds before playing again...")
        time.sleep(30)

if __name__ == "__main__":
    main()
