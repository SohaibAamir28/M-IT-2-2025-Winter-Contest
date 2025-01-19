"""
TODO 1:
- how to adjust for initial slower speed - i.e. jump later
- and then jump earlier when it is speeding up

- need therefore a way to track the speed of the game and dynamically adjust the region to search.
"""

import pyautogui
import subprocess
from PIL import ImageGrab, ImageOps
import numpy as np
import time

# Global Variables

"""UPDATE CHROME BROWSER PATH IF NEEDED"""
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

scaling_factor = 1  # default scaling factor
process = None  # hold open chrome subprocess
info_needed = False
mac_comp = True
dino_page = "chrome://dino"  # page to load dino game

# speed flags
slow = True
medium = False
fast = False


def get_resolution_scaling():
    """Get Resolution scaling between normal and retina pixels scales"""
    global scaling_factor
    screen_size = pyautogui.size()
    screenshot_size = pyautogui.screenshot().size
    scaling_factor = screenshot_size[0] / screen_size.width


def load_page(website=dino_page):
    """
    Loads the chrome dino page.
    Either finds the search bar and clicks or uses key shortcuts to enter in search bar
    """
    try:  # locate search bar
        search_bar = pyautogui.locateOnScreen("./images/search_bar/google_search_bar.png", confidence=0.8)
        if search_bar:
            search_bar_centered = pyautogui.center(search_bar)
            pyautogui.moveTo(search_bar_centered[0] / scaling_factor, search_bar_centered[1] / scaling_factor, duration=0.3)
            pyautogui.click()

    except pyautogui.ImageNotFoundException:  # use command shortcut
        if mac_comp:
            pyautogui.keyDown('command')
            pyautogui.press('l')
            pyautogui.keyUp('command')
        else:
            pyautogui.keyDown('ctrl')
            pyautogui.press('l')
            pyautogui.keyUp('ctrl')

    # search for dino game webpage
    time.sleep(0.3)
    pyautogui.write(website, interval=0.02)
    time.sleep(0.1)
    pyautogui.press('enter')


def activate_browser_dino_game():
    """Loads Chrome browser"""
    global process
    process = subprocess.Popen([CHROME_PATH, "chrome://dino"])
    time.sleep(1)


def disable_wifi():
    """ To search for and deactivate the Wi-fi. Finds the wi-fi on button (Mac), clicks, and turns wi-fi off"""
    time.sleep(1)

    # locate the wi-fi on symbol
    wifi_button_image = "./images/wifi_images/wifi.png"
    try:
        wifi_button = pyautogui.locateOnScreen(wifi_button_image, confidence=0.8)
        if wifi_button:
            centred_coordinates = pyautogui.center(wifi_button)
            pyautogui.moveTo(scaled_coordinate(centred_coordinates[0]), scaled_coordinate(centred_coordinates[1]),
                             duration=1)
            pyautogui.click()
            time.sleep(1)
    except pyautogui.ImageNotFoundException:
        time.sleep(1)
        return

    # locate and turn off wi-fi
    wifi_on_off = "./images/wifi_images/on_off_wifi.png"
    try:
        button_wifi = pyautogui.locateOnScreen(wifi_on_off, confidence=0.7)
        if button_wifi:
            button_centred = pyautogui.center(button_wifi)
            pyautogui.moveTo(scaled_coordinate(button_centred[0]), scaled_coordinate(button_centred[1]), duration=0.5)
            pyautogui.click()
    except pyautogui.ImageNotFoundException:
        pass


def scaled_coordinate(coordinate, decrease=True):
    """calculates the up or down scaled coordinate"""
    value = int(coordinate // scaling_factor) if decrease else int(coordinate * scaling_factor)
    return value


def start_game():
    """
    Gets 3 regions for searching for dino game obstacles, relative to the speed of the game.
    First locates the dino on screen and defines a region relative to its location.
    Returns a smaller region closer to the dino for the slow stage of the game,
    an in-between region for medium speed,
    and a wider region further from the dino for faster stage.
    """
    # Find dino on screen
    dino_img = "./images/dino_images/dino.png"
    dino = pyautogui.locateOnScreen(dino_img, confidence=0.8)

    if dino:  # get the area next to the dino for searching
        # x coordinates
        start_x = int(dino[0] + (dino[2] * 1.8))
        slow_start_x = int(dino[0] + (dino[2] * 1.5))
        # widths
        fast_new_width = int(dino[2] * 3)
        new_width = int(dino[2] * 2.5)
        slow_new_width = int(dino[2] * 1.7)
        # height
        height = dino[3] - 20
        # y coordinate
        start_y = dino[1]

        # create regions
        slow_region = (slow_start_x, start_y, slow_new_width, height)
        normal_region = (start_x, start_y, new_width, height)
        fast_region = (start_x, start_y, fast_new_width, height)

        if info_needed:  # output region info and show on screen with mouse pointer
            print(f"region to search: {slow_region}")
            print(f"region to search: {normal_region}")
            print(f"region to search: {fast_region}")

            for region in [slow_region, normal_region, fast_region]:

                pyautogui.moveTo(scaled_coordinate(region[0]),
                                 scaled_coordinate(region[1]),
                                 duration=0.2)
                pyautogui.moveTo(scaled_coordinate(region[0]),
                                 scaled_coordinate(region[1]) + scaled_coordinate(region[3]),
                                 duration=0.2)
                pyautogui.moveTo(scaled_coordinate(region[0]) + scaled_coordinate(region[2]),
                                 scaled_coordinate(region[1]) + scaled_coordinate(region[3]),
                                 duration=0.2)
                pyautogui.moveTo(scaled_coordinate(region[0]) + scaled_coordinate(region[2]),
                                 scaled_coordinate(region[1]),
                                 duration=0.2)

            pyautogui.move(100, 100)  # move out the way of the game

        return slow_region, normal_region, fast_region


def jump():
    """Jumps the dino"""
    pyautogui.press('up')


def get_total_colours(first_region, second_region=False, third_region=False):
    """
    Retrieves the colours from the pixels for each passed region and identifies the number of colours.
    Used to get the default number of colour for all 3 search obstacle regions,
    and then gets the number of colour for the passed search region during gameplay to detect
    if obstacle in search region (search region number of colours will be different from default - greater than 1).
    """
    regions = [first_region, second_region, third_region] if (second_region and third_region) else [first_region]

    region_number_colours = []
    for region in regions:
        scaled_region = [scaled_coordinate(x) for x in region]  # get the scaled coordinates

        # get the bbox coordinates needed for PIL
        bbox_left = scaled_region[0]
        bbox_top = scaled_region[1]
        bbox_right = scaled_region[0] + scaled_region[2]
        bbox_bottom = scaled_region[1] + scaled_region[3]
        bbox = (bbox_left, bbox_top, bbox_right, bbox_bottom)
        # capture screenshot of region
        search_area = ImageGrab.grab(bbox)

        """below for the sum of the colours"""
        # search_area_greyscale = ImageOps.grayscale(search_area)
        # colours = np.array(search_area_greyscale.getcolors())
        # region_number_colours.append(colours.sum())

        """below for just the len of the get colours. Handles when dino game turns to dark mode."""
        region_number_colours.append(len(search_area.getcolors()))

    # return colour sums
    if not second_region:
        return region_number_colours[0]
    return region_number_colours[0], region_number_colours[1], region_number_colours[2]


def reset_speed_flags():
    """Resets speed flags"""
    global slow, medium, fast
    slow = True
    medium = False
    fast = False


def user_system():
    """Checks the users system"""
    global mac_comp
    computer = input("Running MacOS? 'Y/N'\n")
    if computer.lower() != 'y':
        mac_comp = False


def info_required():
    """check if user wants additional information"""
    global info_needed
    choice = input("Output defined search region coordinates and defined region? 'Y/N'\n")
    if choice.lower() == 'y':
        info_needed = True


def activate_autogui():
    """
    Runs the main game.
    Sets up Browser, game, and updates the search region to check for obstacles as time passes."""
    global slow, medium, fast, process
    user_system()  # check user system
    info_required()  # need info?
    autogui_on()  # failsafe on
    activate_browser_dino_game()  # open Chrome browser
    get_resolution_scaling()  # get screen scaling factor
    load_page()  # load game

    # get the regions to search
    region_slow, region_normal, region_fast = start_game()
    # get the default no. of colours in each region
    slow_area_bg_colours, normal_area_bg_colours, fast_area_bg_colours = get_total_colours(region_slow,
                                                                                           region_normal,
                                                                                           region_fast)

    # set up initial search obstacle region to the slow speed region
    region_selection = region_slow
    area_comparison = slow_area_bg_colours

    # start game
    jump()
    start_time = time.time()  # time flag to change to next search region
    jump_time = time.time()  # time in-between jumps to detect dino collision and to restart game

    while True:
        x, y = pyautogui.position()
        if x == 0 and y == 0:  # exit game if mouse in left corner
            break

        # check if obstacle near dino
        current_search_colour = get_total_colours(region_selection)
        if current_search_colour != area_comparison:
            jump()
            jump_time = time.time()
            time.sleep(0.15)
            if fast:  # press dino down
                pyautogui.keyDown('down')
                time.sleep(0.05)
                pyautogui.keyUp('down')
            continue

        # change to medium region if after 7 seconds
        if slow:
            if (time.time() - start_time) > 10:
                area_comparison = normal_area_bg_colours
                region_selection = region_normal
                slow = False
                medium = True

        # change to fast region if after 14 seconds
        if medium:
            if (time.time() - start_time) > 20:
                area_comparison = fast_area_bg_colours
                region_selection = region_fast
                medium = False
                fast = True

        # restart game and reset region and flags
        if time.time() - jump_time > 7:
            jump()
            reset_speed_flags()
            region_selection = region_slow
            area_comparison = slow_area_bg_colours

        time.sleep(0.1)


def autogui_on():
    pyautogui.FAILSAFE = True  # Enable fail-safe (Mouse at top-left corner)


if __name__ == '__main__':
    activate_autogui()
