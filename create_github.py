import os
import webbrowser
import pyautogui
import pyperclip
import time
import imagesearch as im


def get_Position(image_list):
    for name in image_list:
        path = "images/" + name + ".png"
        print("image: ", path)
        pyautogui.screenshot("screenshot.png")
        posi = im.imagesearch_v2("screenshot.png",path)
        if posi[0] > 0:
            return posi
    return posi

def step_0():
    webbrowser.open('https://github.com/new')


def step_1(response):
    # response = pyautogui.prompt(text='Introduce Repo nam:', title='Repository name')
    if response:
        print("New Repo name: ", response)
        time.sleep(3)  # time for the page to open
        image_list = [ "repo_name_hd","repo_name"] #"repo_name_hd",
        x, y = get_Position(image_list)
        print("step_1", x, y)
        error_method(x)
        pyautogui.click(x +50 , y +50, duration=0.5)
        pyautogui.typewrite(response, interval=0.12)
        pyautogui.hotkey("tab")
        response = ""


def step_2(response):
    # response = pyautogui.prompt(text='Introduce Description', title='Repository Description')
    if response:
        print("New Repo description: ", response)
        pyautogui.typewrite(response, interval=0.06)


def scroll_and_submit():
    x, y = pyautogui.position()
    print(x, y)
    pyautogui.scroll(-500)
    pyautogui.click(23, 333, duration=0.5)
    # time.sleep(2)  # time for the page to open
    image_list = ["submit_hd", "submit"]
    x, y = get_Position(image_list)
    print("scroll_and_submit", x, y)
    error_method(x)
    pyautogui.click(x + 20, y + 10)


def step_copy_commands():
    # posi = pyautogui.locateOnScreen("images/copy_icon.png")
    image_list = ["copy_icon_hd","copy_icon"]
    x, y = get_Position(image_list)
    print("scroll_and_submit", x, y)
    error_method(x)
    pyautogui.moveTo(x + 50 , y )
    # pyautogui.moveRel(yOffset=55)
    # pyautogui.click()
    gitCommands = pyperclip.paste().strip().split("\n")
    return gitCommands


def step_3(path, gitCommands):
    os.chdir(path)
    for each in gitCommands:
        if "push" not in each:
            os.system(each)
            print(each)


def error_method(x):
    if x < 0:
        pyautogui.alert(text='Web page out of screenShot', title='Error', button='OK')
        exit()


if __name__ == "__main__":
    name = "DemoRepo"
    description = "Just a test, must delete"
    path = r"D:\CA\Pprograms\DemoRepo"

    # step_0() # open web page
    # step_1(name)
    # step_2(description) #add description
    # scroll_and_submit()
    #---------- after sumit --------
    time.sleep(2)
    gitCommands = step_copy_commands()
    step_3(path, gitCommands)

    print("End of Main")
