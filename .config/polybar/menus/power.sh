#!/bin/bash

selected=$(echo "  Lock
  Exit
  Reboot
  Shutdown" | rofi -dmenu -config ~/.config/rofi/arch-power-config.rasi -format i)

case $selected in
    0) 
        #echo "lock"
        ./.i3/script/lock_bar.sh
        ;;
    1) 
        #echo "exit"
        i3exit logout
        ;;
    2) 
        #echo "reboot"
        i3exit reboot
        ;;
    3) 
        #echo "shutdown"
        i3exit shutdown
        ;;
esac