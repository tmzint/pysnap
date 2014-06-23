__author__ = 'timo merlin zint'

import sys, getopt
import gtk
import Xlib.display

class Direction:
    NONE = -1
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP_RIGHT = 4
    DOWN_RIGHT = 5
    DOWN_LEFT = 6
    UP_LEFT = 7
    ALL = 8

def usage():
    print "see -h or --help"

def help():
    print "-a or --offHeight: offset of height"
    print "-b or --offWidth: offset of width"
    print "-x or --offX: offset of x coordinate"
    print "-y or --offY: offset of y coordinate"
    print "-d or --direction: 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT, 4 = UP_RIGHT, 5 = DOWN_RIGHT, 6 = DOWN_LEFT, 7 = UP_LEFT, 8 = ALL"
    print "-h or --help: this screen"

def main():
    offHeight = 0;
    offWidth = 0;
    offX = 0;
    offY = 0;
    dir = Direction.NONE

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hx:y:d:a:b",["offHeight=","offWidth=", "offX=", "offY=","direction=", "help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            help()
            sys.exit()
        elif opt in ('-a', "--offHeight"):
            offHeight = int(arg)
        elif opt in ('-b', "--offWidth"):
            offWidth = int(arg)
        elif opt in ('-x', "--offX"):
            offX = int(arg)
        elif opt in ('-y', "--offY"):
            offY = int(arg)
        elif opt in ('-d', "--direction"):
            dir = int(arg)

    window = gtk.Window()

    # the screen contains all monitors
    screen = window.get_screen()

    # collect data about each monitor
    curMon = screen.get_monitor_at_window(screen.get_active_window())
    currMonX,  currMonY,  currMonWidth,  currMonHeight = screen.get_monitor_geometry(curMon)

    display = Xlib.display.Display()
    fcsWin = display.get_input_focus().focus

    fcsWinNude = None
    fcsWinNudeGeo = None
    fcsWinHolder = fcsWin
    # find the window with decoration and without
    while fcsWinNude is None:
        fcsWinHolderGeo = fcsWinHolder.get_geometry()

        if fcsWinHolderGeo.width <= 1 or fcsWinHolderGeo.height <= 1:
            fcsWinHolder = fcsWinHolder.query_tree().parent
            continue

        fcsWinNude = fcsWinHolder
        fcsWinNudeGeo = fcsWinHolderGeo

    fcsWinClthd = fcsWinNude.query_tree().parent
    fcsWinClthdGeo = fcsWinClthd.get_geometry()

    # print "screen.get_monitor_geometry(curMon): %s" % screen.get_monitor_geometry(curMon)
    # print "fcsWinGeo: %s" % fcsWin.get_geometry()
    # print "fcsWinNudeGeo: %s" % fcsWinNudeGeo
    # print "fcsWinClthdGeo: %s" % fcsWinClthdGeo

    clthHeight = fcsWinClthdGeo.height - fcsWinNudeGeo.height
    clthWidth = fcsWinClthdGeo.width - fcsWinNudeGeo.width

    # print "--------------------------------"
    # print "clthWidth: %s" % clthWidth
    # print "clthHeight: %s" % clthHeight

    if dir == Direction.NONE:
        print "no direction given"
        sys.exit(2)

    if dir > 8 or dir < 0:
        print "not acceptable direction given"
        sys.exit(2)

    # halfs
    if dir == Direction.UP:
        newX = currMonX
        newY = currMonY
        newWidth = currMonWidth + offWidth
        newHeight = currMonHeight/2 - clthHeight + offHeight/2
    elif dir ==  Direction.LEFT:
        newX = currMonX
        newY = currMonY
        newWidth = currMonWidth/2 + offWidth/2
        newHeight = currMonHeight - clthHeight + offHeight
    elif dir == Direction.RIGHT:
        newX = currMonX + currMonWidth/2 + offWidth/2
        newY = currMonY
        newWidth = currMonWidth/2 + offWidth/2
        newHeight = currMonHeight - clthHeight + offHeight
    elif dir == Direction.DOWN:
        newX = currMonX
        newY = currMonY +currMonHeight/2 +offHeight/2
        newWidth = currMonWidth + offWidth
        newHeight = currMonHeight/2 - clthHeight + offHeight/2

    # quarters
    elif dir ==  Direction.UP_RIGHT:
        newX = currMonX + currMonWidth/2 + offWidth/2
        newY = currMonY
        newWidth = currMonWidth/2 + offWidth/2
        newHeight = currMonHeight/2 - clthHeight + offHeight/2
    elif dir ==  Direction.DOWN_RIGHT:
        newX = currMonX + currMonWidth/2 + offWidth/2
        newY = currMonY +currMonHeight/2 +offHeight/2
        newWidth = currMonWidth/2 + offWidth/2
        newHeight = currMonHeight/2 - clthHeight + offHeight/2
    elif dir ==  Direction.DOWN_LEFT:
        newX = currMonX
        newY = currMonY +currMonHeight/2 +offHeight/2
        newWidth = currMonWidth/2 + offWidth/2
        newHeight = currMonHeight/2 - clthHeight + offHeight/2
    elif dir ==  Direction.UP_LEFT:
        newX = currMonX
        newY = currMonY
        newWidth = currMonWidth/2 + offWidth/2
        newHeight = currMonHeight/2 - clthHeight + offHeight/2

    # max size
    elif dir ==  Direction.ALL:
        newX = currMonX
        newY = currMonY
        newWidth = currMonWidth + offWidth
        newHeight = currMonHeight - clthHeight + offHeight

    # default
    else:
        # should not be possible
        sys.exit(2)

    newX += offX
    newY += offY

    # print "--------------------------------"
    # print "newWidth: %s" % newWidth
    # print "newHeight: %s" % newHeight
    # print "newX: %s" % newX
    # print "newY: %s" % newY

    fcsWinNude.configure(width = newWidth, height = newHeight, x = newX, y = newY)
    display.sync()

if __name__ == "__main__":
    main()
