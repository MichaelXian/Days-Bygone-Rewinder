import time

screen = Region(0,0,1920,1080)
select_region = Region(517,178,897,101)
select_color_region = Region(1029,192,366,63)
select_image_region = Region(129,414,1649,237)
devastation_region = Region(1031,719,795,126)
gold_region = Region(235,849,786,134)
crit_region = Region(1054,602,751,93)
elixir_tab = "1626372344232.png"
stats_tab = Pattern("stats_tab.png").similar(0.93)
gear_tab = "gear_tab.png"
fifty_percent = Pattern("fifty_percent.png").similar(0.82)
hundred_percent = Pattern("hundred_percent.png").similar(0.82)
 
rewind = Pattern("1626372385701.png").similar(0.90)
rewind_confirm = "rewind_confirm.png"
battle = Pattern("battle.png").exact()
campaign_old = "1626372534941.png"
campaign = "campaign.png"
hunt = "hunt.png"
ok = "1626372757306.png"
pause = "pause.png"
ret = "return.png"
fifty = Pattern("1626373786717.png").exact()
defeat = "defeat.png"
claim = "claim.png"
confirm = "confirm.png"
close_button = "close_button.png"
hand = "1626710284525.png"
buy = "buy.png"
sell = "sell.png"
highest_tier_location = Location(1600, 330)
epic_gear_location = Location(1450, 450)
sell_confirm_region = Region(1412,574,273,155)
double = "double.png"
elixir_mastery = Pattern("elixir_mastery.png").targetOffset(470,16)

# Gear farm

asmodeus = "asmodeus.png"
asmodeus2 = "asmodeus2.png"
helm_tab = "helm_tab.png"
helm_clicks = [asmodeus, asmodeus2, helm_tab]

leviathan = "leviathan.png"
leviathan2 = "leviathan3.png"
plate_tab = "plate_tab.png"
plate_clicks = [leviathan, leviathan2, plate_tab]

belphegor = "belphegor.png"
belphegor2 = "belphegor2.png"
boot_tab = "boot_tab.png"

boot_clicks = [belphegor, belphegor2, boot_tab]

mammon = "mammon.png"
mammon2 = "mammon2.png"
ring_tab = "ring_tab.png"
ring_clicks = [mammon, mammon2, ring_tab]
# Anti anti-cheat
# Select an item
select_old = "select.png"
select = "select.png"
common_color = "1626397534033.png"
rare_color = "rare_color.png"
epic_color = "epic_color.png"
legendary_color = "legendary_color.png"
current_item_type = None
item_found = False

# Weapons

bow = (Pattern("bow_text.png").similar(0.55),"bow.png")
sword = (Pattern("sword_text.png").similar(0.55),"1626390522571.png")
glock = (Pattern("1626390498465.png").similar(0.55),"1626390505557.png")
axe = (Pattern("1626391035526.png").similar(0.56), "1626390929877.png")
pickaxe = (Pattern("1626390536141.png").similar(0.54),"pickaxe.png")
boomerang = (Pattern("1626390670128.png").similar(0.56),"boomerang.png")
shuriken = (Pattern("1626390708596.png").similar(0.56),"shuriken.png")
cleaver = (Pattern("1626390693868.png").similar(0.56),"cleaver.png")
common_weapons = [bow, sword, glock, axe, pickaxe, boomerang, shuriken, cleaver]
wushu_spear = ("1630921792449.png","1626390632441.png")
kunai = ("1630921826919.png","1626390654650.png")
longsword = (Pattern("1626391403021.png").similar(0.50),"1626391394072.png")

crimson_bow = (Pattern("crimson_bow_text.png").similar(0.56),"crimson_bow.png")
grenade = (Pattern("1626390951326.png").similar(0.56),"1626390762386.png")
p90 = (Pattern("1626391615562.png").similar(0.56),"1626390774018.png")
rare_weapons = [wushu_spear, kunai, longsword, crimson_bow, grenade, p90]
harlott = (Pattern("1626390798724.png").similar(0.56),"1626390804726.png")
rhongomiant = (Pattern("1626391706207.png").similar(0.54),"1626391458728.png")
sharanga = (Pattern("1626391205826.png").similar(0.54),"1626391196954.png")
ascalon = (Pattern("1626390472430.png").similar(0.55), "1626390480217.png")
epic_weapons = [harlott, rhongomiant, sharanga, ascalon]
excalibur = (Pattern("1626391132891.png").similar(0.54),"1626391138708.png")
aldan = (Pattern("1626391151645.png").similar(0.58),"1626391157155.png")
# sword_ground = (,"1626392275777.png")
galatine = (Pattern("1626394315914.png").similar(0.56),"1626391096733.png")
bazooka = (Pattern("1626392930918.png").similar(0.56),"1626391019156.png")
minigun = (Pattern("1626392504074.png").similar(0.56),"1626391572886.png")
mjolnir = (Pattern("1626392619412.png").similar(0.54),"1626392625429.png")
dragunov = (Pattern("1626395761714.png").similar(0.56),"1626391670928.png")
legendary_weapons = [excalibur, aldan, galatine, bazooka, minigun, mjolnir, dragunov]

# Hats
propeller_cap = ("1631078434493.png","1626510370622.png")
fez = ("1631078463860.png","1626510516290.png")
strawberry_cone = ("1631078613933.png","1626510565926.png")
graduation_cap = ("1630980859527.png","1626510645056.png")
reading_glasses = ("1631078602200.png","1626510699801.png")
cheap_headphones = ("1631078413540.png","1626510719858.png")
surgical_mask = ("1631078509360.png","1626510764487.png")
top_hat = ("1631078445878.png","1626510989663.png")
common_helms = [propeller_cap, fez, strawberry_cone, graduation_cap, reading_glasses, cheap_headphones, surgical_mask, top_hat]
peaked_cap = (Pattern("1626510776300.png").similar(0.55),"1626510780969.png")
steel_helm = ("1631078520276.png","1626510410274.png")
brown_fedora = (Pattern("1626510445135.png").similar(0.51),"1626510434445.png")
cowboy_hat = ("1631078554907.png","1626510606305.png")
pointy_hat = (Pattern("1626510660465.png").similar(0.51),"1626510665321.png")
hard_hat = (Pattern("1626510821491.png").similar(0.55),"1626510826292.png")
crimson_beak = (Pattern("1626510875975.png").similar(0.55),"1626510880657.png")
transparent_cap = ("1631078473826.png","1626510897670.png")
straw_hat = (Pattern("1626510911562.png").similar(0.55),"1626510916257.png")
panama_hat = ("1631078537363.png","1626510968130.png")
rare_helms = [peaked_cap, steel_helm, brown_fedora, cowboy_hat, pointy_hat, hard_hat, crimson_beak, transparent_cap, straw_hat, panama_hat]
bucket_helm = (Pattern("bucket.png").similar(0.56),"1626510300033.png")
great_helm = ("1631078572945.png","1626510804676.png") 
cozy_hat = ("1631078484721.png","1626510845668.png")
midas_helm = (Pattern("1626510931789.png").similar(0.55),"1626510937305.png")
mushroom_cap = (Pattern("1626513434980.png").similar(0.51),"1626513443118.png")
epic_helms = [bucket_helm, great_helm, cozy_hat, midas_helm, mushroom_cap]
oni_mask = (Pattern("1626510737382.png").similar(0.55),"1626510742869.png")
void_mask = (Pattern("void_mask.png").similar(0.56),"1626511369748.png")
kingsguard_helm = (Pattern("1626511504387.png").similar(0.54),"1626511509382.png")
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

def check_claim():
    if try_click(claim):
        for i in range(10):
            click(Location(100, 100))
            sleep(1)
        while exists(hand):
            try_click(hand)
        while exists(confirm):
            try_click(confirm)
        try_click(close_button)

def buy_item(buy_region, amount):
    try:
        wait_click(stats_tab)
        sleep(2)
        wait_click(amount)
        buy_region.click(buy)
    except:
        pass

# Anti anti-cheat functions
def anti_anti_cheat():
    try:
        print("check claim")
        check_claim()
        try_click(claim)
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

def sell_gear(click_list):
    wait_click(sell)
    sleep(1)
    click(highest_tier_location)
    sleep(1)
    click(epic_gear_location)
    sleep(1)
    sell_confirm_region.click(sell)
    # click specific armor tab
    wait_click(click_list[2])

def elixir_farm(level_elixir):
    buy_item(gold_region, fifty_percent)
    buy_item(crit_region, hundred_percent)
    wait_click(battle)
    wait_click(campaign)
    try:
        wait(double, 10)
        click(double, 10)
    except:
        wait_click(ok)
    try: # In case we skip 50-59, timeout at 120s
        wait(defeat, 3600)
        click(defeat)
    except:
        pass
    sleep(2)
    buy_item(gold_region, hundred_percent)
    wait_click(elixir_tab)
    if (level_elixir):
        try:
            wait_click(elixir_mastery)
            wait_click(ok)
        except:
            pass
    wait_click(rewind)
    wait_click(rewind_confirm)

def rewind_farm():
    wait_click(battle)
    wait_click(campaign)
    wait_click(ok)
    try: # In case we skip 50-59, timeout at 120s
        wait(fifty, 120)
        click(fifty)
    except:
        pass
    if exists(defeat):
        click(defeat)
    else:
        sleep(2)
        wait_click(pause)
        wait_click(ret)
        wait_click(ok)
    wait_click(elixir_tab)
    full_rewind()

def gear_farm(click_list):
    wait_click(gear_tab)
    # Select which armor piece
    wait_click(click_list[2])
    sell_gear(click_list)
    wait_click(battle)
    wait_click(hunt)
    # Select enemy
    wait_click(click_list[0])
    # Select level
    wait_click(click_list[1])
    wait_click(ok)
    sleep(10)
    for i in range (3600):
        try:
            wait(ok, 10)
            break
        except:
            sleep(10)
    wait_click(ok)


# Main function
while True:
    try: # skip back to battle if we hit an anti-cheat
        #gear_farm(ring_clicks)
        elixir_farm(False)
    except Exception as e:
        print(e)
            
