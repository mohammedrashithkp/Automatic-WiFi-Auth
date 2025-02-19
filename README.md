# Automatic-WiFi-Auth
This repo contains a python program which automates logins in to WiFi Captive Portals usually found in Educational Institutes,Restaurants etc saving you the hassle of filling it every time .
> This is made for Firefox Browser in (Tested in Ubuntu 22.04 & Win11).
## How to Use
1. Clone the repo to your Machine.
```bash
 git clone https://github.com/mohammedrashithkp/Automatic-WiFi-Auth.git
&& cd Automatic-WiFi-Auth
``` 
2. Make an .env file with auth_user and auth_password parameters.
   ```env
   auth_user=USERNAME
   auth_password=PASSWORD
   ```
4. Install Necessary Libraries & Run the Python Project
   ```bash
    pip install selenium python-dotenv
    python3 app.py
   ```
## Future Works
- Make a cron job which gets activated when the device is connected to a defined ssid.
## References
- Selenium [Docs](https://www.selenium.dev/documentation/)
- Finding Firefox [Folder](https://www.howtogeek.com/255587/how-to-find-your-firefox-profile-folder-on-windows-mac-and-linux/)
