import time
from Images import *
from Helms import *
from Weapons import *
from Helpers import *

def check_items(items, name):
    global current_item_type
    global item_found
    print("Check items")
    print(current_item_type)
    print(name)
    if current_item_type == name or current_item_type is None:
        for txt, img in items:
            if cond_click(select_region, txt, select_image_region, img):
                print("found")
                current_item_type = name
                item_found = True
                return True
    print("failed")
    return False

def check_defeat():
    if try_click(defeat):
        wait_click(elixir_tab)
        full_rewind()

# Anti anti-cheat functions
def anti_anti_cheat():
    try:
        print("check defeat")
        check_defeat()
        print("Anti select")
        anti_select()
        print ("Anti tap")
        anti_tap()
    except Exception as e:
        print(e)

def anti_select():
    global item_found
    global current_item_type
    while select_region.exists(select):
        print("select")
        item_found = False
        if select_color_region.exists(common_color):
            check_items(common_weapons, "weapons")
            check_items(common_helms, "helms")
        elif select_color_region.exists(rare_color):
            check_items(rare_weapons, "weapons")
            check_items(rare_helms, "helms")
        elif select_color_region.exists(epic_color):
            check_items(epic_weapons, "weapons")
            check_items(epic_helms, "helms")
        elif select_color.region.exists(legendary_color):
            check_items(legendary_weapons, "weapons")
            check_items(legendary_helms, "helms")
        if not item_found:
            # If cant find item, give up and try again
            click(Location(100, 100))
            print("Could not find any items")
    print("Select Done")
    current_item_type = None

def anti_tap():
    while exists(tap):
        print("Anti tap")
        if try_click(yellow):
            continue
        if try_click(green):
            continue
        if try_click(red):
            continue
        click(Location(100, 100)) # If cant find any circles, give up and try again

check_items(legendary_helms, "helms")
# Main function
while True:
    try: # skip back to battle if we hit an anti-cheat
        print("try")
        wait_click(battle)
        wait_click(campaign)
        wait_click(confirm)
        try: # In case we skip 50-59, timeout at 120s
            wait(fifty, 120)
        except:
            pass
        sleep(2)
        wait_click(pause)
        wait_click(ret)
        wait_click(confirm)
        wait_click(elixir_tab)
        full_rewind()
    except Exception as e:
        print(e)
            
