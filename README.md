pysnap
======

Dynamic multi monitor manual tiling for Openbox.  

Usage:
------
-a or --offHeight: offset of height (relation to full vertical span)  
-b or --offWidth: offset of width (relation to full horizontal span)  
-x or --offX: offset of x coordinate  
-y or --offY: offset of y coordinate  
-d or --direction: 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT, 4 = UP_RIGHT, 5 = DOWN_RIGHT, 6 = DOWN_LEFT, 7 = UP_LEFT, 8 = ALL  
-h or --help: this screen  

Example:
------
pysnap.py -a -30 -y 30 -d 3  
Tile current focused window to the Left (full vertical, half horizontal),
with an height offset over the full vertical span of -30px (30px horizontal taskbar)
and an x offset of 30 (taskbar at the top of the screen).  

rc.xml
------

Tiling is done via meta + numpad, where the position of the numpad key corresponds
to the desired direction of tiling.  

Snippet of my rc.xml.  

<keyboard>

  ...

  <keybind key="W-KP_6">
      <action name="Unmaximize" />
      <action name="Execute">
          <command>pysnap.py -a -30 -d 1</command>
      </action>
  </keybind>
  <keybind key="W-KP_4">
      <action name="Unmaximize" />
      <action name="Execute">
          <command>pysnap.py -a -30 -d 3</command>
      </action>
  </keybind>
  <keybind key="W-KP_2">
      <action name="Unmaximize" />
      <action name="Execute">
          <command>pysnap.py -a -30 -d 2</command>
      </action>
  </keybind>
  <keybind key="W-KP_8">
      <action name="Unmaximize" />
      <action name="Execute">
          <command>pysnap.py -a -30 -d 0</command>
      </action>
  </keybind>
  <keybind key="W-KP_9">
      <action name="Unmaximize" />
      <action name="Execute">
          <command>pysnap.py -a -30 -d 4</command>
      </action>
  </keybind>
  <keybind key="W-KP_3">
      <action name="Unmaximize" />
      <action name="Execute">
          <command>pysnap.py -a -30 -d 5</command>
      </action>
  </keybind>
  <keybind key="W-KP_1">
      <action name="Unmaximize" />
      <action name="Execute">
          <command>pysnap.py -a -30 -d 6</command>
      </action>
  </keybind>
  <keybind key="W-KP_7">
      <action name="Execute">
          <command>pysnap.py -a -30 -d 7</command>
      </action>
  </keybind>
  <keybind key="W-KP_5">
      <action name="Unmaximize" />
      <action name="Execute">
          <command>pysnap.py -a -30 -d 8</command>
      </action>
  </keybind>

  ...

</keyboard>
