a = True
import time

while a == True:
        import pygame.cdrom as cdrom
        cdrom.init()
        cd = cdrom.CD(0) # 0 = first cdrom device
        cd.init()
        cd.eject()
        cd.quit()
        cdrom.quit()
        time.sleep(5)
        print "Troll"
