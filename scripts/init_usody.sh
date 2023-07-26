stty -echo # Do not show what we type in terminal so it does not meddle with our nice output
setterm -blank 0  # Do not suspend monitor
dmesg -n 1 # Do not report *useless* system messages to the terminal
cd /mnt
python3 /opt/usody/main.py
stty echo
