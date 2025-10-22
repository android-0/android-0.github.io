# My i3 Config

Posted: Sun, 22-09-2024.
Edited: Sun, 24-11-2024.

First, I ran this to generate the config file:
```
$ i3-config-wizard
```
Here I chose Windows key as my mod key.

I made bindings to adjust volume and brightness.
```
bindsym $mod+F1 exec amixer sset 'Master' toggle
bindsym $mod+F3 exec amixer sset 'Master' 5%-
bindsym $mod+Shift+F3 exec amixer sset 'Master' 5%+
bindsym $mod+F5 exec xbacklight -0.5
bindsym $mod+Shift+F5 exec xbacklight +0.5
```

I increased the font size for window title and bar.
```
font pango:monospace 10
```

I added wallpaper.
```
exec_always feh --bg-fill +0+0 ~/Pictures/wallpaper.jpg
```

I changed tab bar font color because it is hard to see.
```
client.unfocused #333333 #444444 #ffffff #292d2e #222222
```

I changed the background color of bar.
```
colors {
    background #282A2E
}
```

Disable mouse wheel on bar.
```
bindsym button4 nop
bindsym button5 nop
```

My keyboard seldom not working properly and I cannot exit i3.
This is my temporary solution.
```
bindsym --release button3 exec "i3-nagbar -t warning -m 'Do you really want to exit i3?' -B 'Yes, exit i3' 'i3-msg exit'"
```

I set the default terminal to alacritty.
```
bindsym $mod+Return exec alacritty
```

I added binding to scrot (screen capture).
```
bindsym $mod+F11 exec scrot -F ~/Pictures/SS/'%Y-%m-%d-%H%M%S.png'
```

For i3status, I set the color to false and set the interval to 5 second.
```
general {
        colors = false
        interval = 5
}
```

I used these modules: battery, memory, volume, and tztime.
