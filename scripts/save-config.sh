# ~/
cp ~/.bashrc ./home/hick/
cp ~/.profile ./home/hick/

# ~/.local/share/code-server/User/settings.json
mkdir -p ./home/hick/.local/share/code-server/User/
cp ~/.local/share/code-server/User/settings.json ./home/hick/.local/share/code-server/User/

# ~/.config
mkdir -p ./home/hick/.config/htop/
mkdir -p ./home/hick/.config/btop/
cp ~/.config/htop/htoprc ./home/hick/.config/htop/
cp ~/.config/btop/btop.conf ./home/hick/.config/btop/