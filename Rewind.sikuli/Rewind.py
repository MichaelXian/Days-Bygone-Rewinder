import time
time.sleep(0)
screen = Region(0,0,1920,1080)
elixir_tab = "1626372344232.png"
rewind = Pattern("1626372385701.png").similar(0.90)
rewind_confirm = "rewind_confirm.png"
battle = "battle.png"
campaign = "1626372534941.png"
confirm = "1626372757306.png"
pause = "pause.png"
ret = "return.png"
fifty = Pattern("1626373786717.png").exact()

def wait_click(image):
    wait(image, 3600)
    click(image)
while True:
    wait_click(battle)
    wait_click(campaign)
    wait_click(confirm)
    try:
        wait(fifty, 180)
    except:
        pass
    wait_click(pause)
    wait_click(ret)
    wait_click(confirm)
    wait_click(elixir_tab)
    wait_click(rewind)
    wait_click(rewind_confirm)
            
