'''
    This module auto clear invited stage
'''
import time
import pyautogui
import pyscreeze

class StartStageException(Exception):
    """ Fail to start Stage """

def check_invited():
    """ Check if invited """
    try:
        pyautogui.locateCenterOnScreen('identifyImg/accept.png', confidence=0.7)
        return True
    except pyscreeze.ImageNotFoundException:
        return False

def start_stage():
    """ Start the stage """
    print("Start Stage!")
    try:
        target_x, target_y = pyautogui.locateCenterOnScreen('identifyImg/accept.png', confidence=0.9)
        pyautogui.click(target_x, target_y, duration=0.25)
        time.sleep(1)
    except:
        raise StartStageException

def check_in_stage():
    """ Check is in the stage """
    try:
        pyautogui.locateCenterOnScreen('identifyImg/sameTeam.png', confidence=0.7)
        return True
    except pyscreeze.ImageNotFoundException:
        return False

def check_boss_faught():
    """ Check if boss faught """
    try:
        pyautogui.locateCenterOnScreen('identifyImg/drops.png', confidence=0.7)
        return True
    except pyscreeze.ImageNotFoundException:
        return False

def fight_stage():
    """ Loop and fight the stage """
    print("Fight Stage!")

    is_boss_faught = False
    while True:
        try:
            is_boss_faught = check_boss_faught()

            if is_boss_faught:
                move_x, move_y = pyautogui.locateCenterOnScreen('identifyImg/sameTeam.png', confidence=0.7)
                while True: # Check stage drop
                    try:
                        drop_x, drop_y = pyautogui.locateCenterOnScreen('identifyImg/drops.png', confidence=0.9)
                        pyautogui.click(drop_x, drop_y, duration=0.25)
                        time.sleep(1)
                        pyautogui.click(move_x, move_y, duration=0.25)
                        time.sleep(1)
                    except pyscreeze.ImageNotFoundException:
                        if check_invited():
                            print("Returned to stage page")
                            return

            while True:
                try:
                    end_target_x, end_target_y = pyautogui.locateCenterOnScreen('identifyImg/stageEnd.png', confidence=0.7)
                    position_str = 'End Fight X: ' + str(end_target_x).rjust(4) + ' Y: ' + str(end_target_y).rjust(4)
                    print(position_str)
                    pyautogui.click(end_target_x, end_target_y, duration=0.25)
                    time.sleep(1)
                    break
                except pyscreeze.ImageNotFoundException:
                    if check_in_stage():
                        time.sleep(3)
                        break
                    else:
                        time.sleep(0.5)
                        continue

        except pyscreeze.ImageNotFoundException:
            if check_invited():
                print("Returned to stage page")
                return

def auto_join_stage(continue_half=False):
    """ auto_stage """
    while True:
        if not continue_half:
            try:
                start_stage()
            except StartStageException:
                continue
        fight_stage()
        time.sleep(1)
        continue_half = False

auto_join_stage(False)