# Helper Functions
def wait_click(image):
    try:
        wait(image, 10)
        click(image)
    except:
        print("Anti anti cheat")
        anti_anti_cheat()
        raise Exception("Anti-cheat hit, reset to beginning")

def try_click(image):
    try:
        click(image)
        return True
    except:
        return False

def cond_click(condition_region, condition, image_region, image):
    if condition_region.exists(condition):
        return try_click(image)
    return False

def full_rewind():
    while exists(rewind):
        try_click(rewind)
        try_click(rewind_confirm)
