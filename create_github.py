import os
import webbrowser
import pyautogui
import pyperclip
import time


def step_1(response):
    webbrowser.open('https://github.com/new')
    # response = pyautogui.prompt(text='Introduce Repo nam:', title='Repository name')
    if response:
        print("New Repo name: ", response)
        time.sleep(2)  # time for the page to open
        posi = pyautogui.locateOnScreen("images/repo_name.png")
        print("step_1", posi)
        error_method(posi)
        pyautogui.click(posi)
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
    pyautogui.click(23, 333, duration=1)
    # time.sleep(2)  # time for the page to open
    posi = pyautogui.locateOnScreen("images/sumit.png")
    print("scroll_and_submit", posi)
    error_method(posi)
    pyautogui.click(posi)



def step_3(path, gitCommands):
    os.chdir(path)
    for each in gitCommands:
        if "push" not in each:
            os.system(each)
            print(each)



def step_copy_commands():
    posi = pyautogui.locateOnScreen("images/copy_icon.png")
    print("step_copy_commands", posi)
    error_method(posi)
    pyautogui.moveTo(posi)
    pyautogui.moveRel(yOffset=55)
    pyautogui.click()
    gitCommands = pyperclip.paste().strip().split("\n")
    return gitCommands


def error_method(posi):
    if posi is None:
        pyautogui.alert(text='Web page out of screenShot', title='Error', button='OK')
        exit()


if __name__ == "__main__":
    name = "testRepo"
    description = "Python automation script for creating a new gitHub project."
    path = r"<path>\create_github"

    step_1(name)
    step_2(description)
    scroll_and_submit()
    time.sleep(3)
    gitCommands = step_copy_commands()
    step_3(path, gitCommands)

    print("End of Main")
