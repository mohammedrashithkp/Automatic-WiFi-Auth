# Automatic-WiFi-Auth
This repo contains a python program which automates logins in to WiFi Captive Portals usually found in Educational Institutes,Restaurants etc saving you the hassle of filling it every time .
> This is made for Firefox Browser in (Tested in Ubuntu 22.04 & Win11).
## How to Use
1. Clone the repo to your Machine.
```bash
 git clone https://github.com/mohammedrashithkp/Automatic-WiFi-Auth.git
&& cd Automatic-WiFi-Auth
``` 
2. Make an .env file with auth_user and auth_password parameters in the project root folder.
   ```env
   auth_user=USERNAME
   auth_password=PASSWORD
   ```
3. Install Necessary Libraries & Run the Python Project
   ```bash
    pip install selenium python-dotenv
    python3 app.py
   ```
## Automatically Run the Program when connected to specified  network
### Linux
> Find the SSID of desired Wifi Network by running `nmcli dev status`Look for wifi in TYPE column.
1. Follow the instructions and make suitable changes in [bash script](Templates/wifi_checktemp.sh)
2. Make the script executable by running `chmod +x wifi_checktemp.sh`
3. Replace the username and path to your script in [Service File](Templates/Automatic-WiFi-Authtemp.service) and run 
`sudo cp Automatic-WiFi-Authtemp.service /etc/systemd/system/` to copy the file to the Systemd service folder.
4. Enabling the service 

```bash
sudo systemctl daemon-reload
sudo systemctl enable Automatic-WiFi-Authtemp.service
sudo systemctl start Automatic-WiFi-Authtemp.service
```

## Future Works
- Make a psi script for windows  which gets activated when the device is connected to a defined ssid.
## References
- Selenium [Docs](https://www.selenium.dev/documentation/)
- Finding Firefox [Folder](https://www.howtogeek.com/255587/how-to-find-your-firefox-profile-folder-on-windows-mac-and-linux/)
