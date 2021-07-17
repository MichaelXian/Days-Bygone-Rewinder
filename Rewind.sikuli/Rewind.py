import time

screen = Region(0,0,1920,1080)
select_region = Region(517,178,897,101)
select_color_region = Region(993,187,266,83)
select_image_region = Region(129,414,1649,237)
elixir_tab = "1626372344232.png"
rewind = Pattern("1626372385701.png").similar(0.90)
rewind_confirm = "rewind_confirm.png"
battle = "battle.png"
campaign = "1626372534941.png"
confirm = "1626372757306.png"
pause = "pause.png"
ret = "return.png"
fifty = Pattern("1626373786717.png").exact()

# Anti anti-cheat
# Select an item
select = "select.png"
common_color = "1626397534033.png"
rare_color = "rare_color.png"
epic_color = "epic_color.png"
legendary_color = "legendary_color.png"
current_item_type = None

# Weapons

bow = ("bow_text.png","bow.png")
sword = ("sword_text.png","1626390522571.png")
glock = ("1626390498465.png","1626390505557.png")
axe = ("1626391035526.png", "1626390929877.png")
pickaxe = ("1626390536141.png","pickaxe.png")
boomerang = ("1626390670128.png","boomerang.png")
shuriken = ("1626390708596.png","shuriken.png")
cleaver = ("1626390693868.png","cleaver.png")
common_weapons = [bow, sword, glock, axe, pickaxe, boomerang, shuriken, cleaver]
wushu_spear = ("1626390625845.png","1626390632441.png")
kunai = ("1626390648430.png","1626390654650.png")
longsword = ("1626391403021.png","1626391394072.png")

crimson_bow = ("crimson_bow_text.png","crimson_bow.png")
grenade = ("1626390951326.png","1626390762386.png")
p90 = ("1626391615562.png","1626390774018.png")
rare_weapons = [wushu_spear, kunai, longsword, crimson_bow, grenade, p90]
harlott = ("1626390798724.png","1626390804726.png")
rhongomiant = ("1626391706207.png","1626391458728.png")
sharanga = ("1626391205826.png","1626391196954.png")
ascalon = ("1626390472430.png", "1626390480217.png")
epic_weapons = [harlott, rhongomiant, sharanga, ascalon]
excalibur = ("1626391132891.png","1626391138708.png")
aldan = ("1626391151645.png","1626391157155.png")
# sword_ground = (,"1626392275777.png")
galatine = ("1626394315914.png","1626391096733.png")
bazooka = ("1626392930918.png","1626391019156.png")
minigun = ("1626392504074.png","1626391572886.png")
mjolnir = ("1626392619412.png","1626392625429.png")
dragunov = ("1626395761714.png","1626391670928.png")
legendary_weapons = [excalibur, aldan, galatine, bazooka, minigun, mjolnir, dragunov]

# Tap
tap = "tap.png"
yellow = Pattern("yellow2.png").similar(0.64)
red = Pattern("red.png").similar(0.57)
green = Pattern("green.png").similar(0.51)

# Helper Functions
def wait_click(image):
    try:
        wait(image, 10)
        click(image)
    except:
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
        click(image)
        return True
    return False

def check_items(items, name):
    for txt, img in items:
        if cond_click(select_region, txt, select_image_region, img):
            current_item_type = name
            return True
    return False

def select_items(common, rare, epic, legendary, name):
    if current_item_type is name or current_item_type is None:
        if select_color_region.exists(common_color):
            check_items(common, name)
        elif select_color_region.exists(rare_color):
            check_items(rare, name)
        elif select_color_region.exists(epic_color):
            check_items(epic, name)
        elif select_color.region.exists(legendary_color):
            check_items(legendary, name)
        else:
            click(Location(100, 100))
            print("Could not find any " + name)

# Anti anti-cheat functions
def anti_anti_cheat():
    anti_select()
    anti_tap()

def anti_select():
    while select_region.exists(select):
        select_items(common_weapons, rare_weapons, epic_weapons, legendary_weapons, "weapons")
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

# Main function
while True:
    try: # skip back to battle if we hit an anti-cheat
        wait_click(battle)
        wait_click(campaign)
        wait_click(confirm)
        try:
            wait(fifty, 120)
        except:
            pass
        sleep(5)
        wait_click(pause)
        wait_click(ret)
        wait_click(confirm)
        wait_click(elixir_tab)
        wait_click(rewind)
        wait_click(rewind_confirm)
    except:
        pass
            
