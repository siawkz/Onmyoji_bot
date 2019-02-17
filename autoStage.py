'''
    This module auto clear stage by inviting friend or alone.
'''
import time
import pyautogui
import pyscreeze

class StartStageException(Exception):
    """ Fail to start Stage """

def locate_priority_image(img1, img2, confidence):
    """ return location of first image, if not found then second image. """
    try:
        target_x, target_y = pyautogui.locateCenterOnScreen(img1, confidence=confidence)
    except pyscreeze.ImageNotFoundException:
        target_x, target_y = pyautogui.locateCenterOnScreen(img2, confidence=confidence)
    return target_x, target_y

def start_stage(is_team=False):
    """ Start the stage """
    print("Start Stage!")
    try:
        if is_team:
            target_x, target_y = locate_priority_image('identifyImg/confirm.png', 'identifyImg/teamup.png', confidence=0.9)
        else:
            target_x, target_y = pyautogui.locateCenterOnScreen('identifyImg/search.png', confidence=0.9)

        pyautogui.click(target_x, target_y, duration=0.25)
        time.sleep(1)
    except:
        raise StartStageException

def check_at_world():
    """ Check is at world """
    try:
        pyautogui.locateCenterOnScreen('identifyImg/stage28.png', confidence=0.7)
        return True
    except pyscreeze.ImageNotFoundException:
        return False

def check_at_stage_page():
    """ Check is at stage page """
    try:
        pyautogui.locateCenterOnScreen('identifyImg/search.png', confidence=0.7)
        return True
    except pyscreeze.ImageNotFoundException:
        return False

def check_continue_dialog():
    """ Check is at world """
    try:
        pyautogui.locateCenterOnScreen('identifyImg/confirm.png', confidence=0.7)
        return True
    except pyscreeze.ImageNotFoundException:
        return False

def check_in_stage():
    """ Check is in the stage """
    try:
        pyautogui.locateCenterOnScreen('identifyImg/sameTeam.png', confidence=0.7)
        return True
    except pyscreeze.ImageNotFoundException:
        return False

def fight_stage(is_team=False):
    """ Loop and fight the stage """
    print("Fight Stage!")

    boss_faught = False
    target_x, target_y = pyautogui.position()
    while True:
        try:
            move_x, move_y = pyautogui.locateCenterOnScreen('identifyImg/sameTeam.png', confidence=0.7)
            while True: # Check stage drop
                try:
                    drop_x, drop_y = pyautogui.locateCenterOnScreen('identifyImg/drops.png', confidence=0.9)
                    boss_faught = True
                    pyautogui.click(drop_x, drop_y, duration=0.25)
                    time.sleep(1)
                    pyautogui.click(move_x, move_y, duration=0.25)
                    time.sleep(1)
                except pyscreeze.ImageNotFoundException:
                    if boss_faught:
                        if check_at_stage_page():
                            print("Returned to stage page")
                            return
                        elif check_at_world():
                            print("Returned to world")
                            return
                    else:
                        break

            target_x, target_y = locate_priority_image('identifyImg/fightBoss.png', 'identifyImg/fight.png', confidence=0.5)
            position_str = 'Fight X: ' + str(target_x).rjust(4) + ' Y: ' + str(target_y).rjust(4)
            print(position_str)
            pyautogui.click(target_x, target_y, duration=0.25)
            time.sleep(5)

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
                        break
                    else:
                        time.sleep(0.5)
                        continue

        except pyscreeze.ImageNotFoundException:
            if check_in_stage():
                print("Move right for more fights!")
                pyautogui.click(move_x+50, move_y-100)
                time.sleep(2)
                #pyautogui.moveTo(target_x, target_y, duration=0.25)
                #pyautogui.mouseDown(button='left')
                #pyautogui.mouseUp(button='left', x=target_x-150, y=target_y, duration=1.0)
                #pyautogui.drag(-150, 0, duration=3.0, tween=pyautogui.easeInQuad ,button='left')
                continue
            if is_team:
                if check_continue_dialog():
                    print("Returned to team dialog")
                    return
            if check_at_stage_page():
                print("Returned to stage page")
                return
            if check_at_world():
                print("Returned to world")
                return

def auto_stage(is_team=False, continue_half=False):
    """ auto_stage """
    while True:
        if not continue_half:
            if check_at_world():
                stage_x, stage_y = pyautogui.locateCenterOnScreen('identifyImg/stage28.png', confidence=0.9)
                pyautogui.click(stage_x, stage_y, duration=0.25)
                time.sleep(1)
            start_stage(is_team)
            while not check_in_stage():
                continue
        fight_stage(is_team)
        time.sleep(1)
        continue_half = False


auto_stage(True, False)