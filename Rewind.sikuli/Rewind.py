import time

screen = Region(0,0,1920,1080)
select_region = Region(517,178,897,101)
select_color_region = Region(1029,192,366,63)
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
defeat = "defeat.png"

# Anti anti-cheat
# Select an item
select = "select.png"
common_color = "1626397534033.png"
rare_color = "rare_color.png"
epic_color = "epic_color.png"
legendary_color = "legendary_color.png"
current_item_type = None
item_found = False

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

# Hats
propeller_cap = ("propeller_Cap.png","1626510370622.png")
fez = ("1626510467141.png","1626510516290.png")
strawberry_cone = ("1626510559594.png","1626510565926.png")
graduation_cap = ("1626510639473.png","1626510645056.png")
reading_glasses = ("1626510693258.png","1626510699801.png")
cheap_headphones = ("1626510714331.png","1626510719858.png")
surgical_mask = ("1626510759069.png","1626510764487.png")
top_hat = ("1626510984876.png","1626510989663.png")
common_helms = [propeller_cap, fez, strawberry_cone, graduation_cap, reading_glasses, cheap_headphones, surgical_mask, top_hat]
peaked_cap = ("1626510776300.png","1626510780969.png")
steel_helm = ("1626510403789.png","1626510410274.png")
brown_fedora = ("1626510445135.png","1626510434445.png")
cowboy_hat = ("1626510600320.png","1626510606305.png")
pointy_hat = ("1626510660465.png","1626510665321.png")
hard_hat = ("1626510821491.png","1626510826292.png")
crimson_beak = ("1626510875975.png","1626510880657.png")
transparent_cap = ("1626510893188.png","1626510897670.png")
straw_hat = ("1626510911562.png","1626510916257.png")
panama_hat = ("1626510963345.png","1626510968130.png")
rare_helms = [peaked_cap, steel_helm, brown_fedora, cowboy_hat, pointy_hat, hard_hat, crimson_beak, transparent_cap, straw_hat, panama_hat]
bucket_helm = ("bucket.png","1626510300033.png")
great_helm = ("1626510799326.png","1626510804676.png") 
cozy_hat = ("1626510856586.png","1626510845668.png")
midas_helm = ("1626510931789.png","1626510937305.png")
mushroom_cap = ("1626513434980.png","1626513443118.png")
epic_helms = [bucket_helm, great_helm, cozy_hat, midas_helm, mushroom_cap]
oni_mask = ("1626510737382.png","1626510742869.png")
void_mask = ("void_mask.png","1626511369748.png")
kingsguard_helm = ("1626511504387.png","1626511509382.png")
legendary_helms = [oni_mask, void_mask, kingsguard_helm]
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

def full_rewind():
    while exists(rewind):
        try_click(rewind)
        try_click(rewind_confirm)

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
            print("Could not find any:")
            print(name)
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
            
