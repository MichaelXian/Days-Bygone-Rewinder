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
# Tap
tap = "tap.png"
yellow = Pattern("yellow2.png").similar(0.64)
red = Pattern("red.png").similar(0.57)
green = Pattern("green.png").similar(0.51)