[module/cpu-frequency]
type = custom/script
exec = cat /proc/cpuinfo | awk -v div=1000 '/cpu MHz/ {printf "%.2fGhz ",$4/div}'
tail = true
format = <label>
format-prefix = " "
format-prefix-foreground = ${colors.foreground-alt}
label = %output%
interval = 1