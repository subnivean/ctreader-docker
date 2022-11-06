Code to read the current off a wire using a CT hat
connected to a Raspberry Pi.

Run via a cron job added via `sudo crontab -e`.

Multiple cron jobs with `sleep` offsets can be used to get
sub-minute data resolution.

NOTE: In order for the CT readers to work you'll need to:

- `sudo raspi-config`
- Go to `Interface Options`
- Go to `Serial Port`
- Say 'No' to '...login shell...'
- Say 'Yes' to 'Would you like the serial port hardware to be enabled?'
- Exit `raspi-config` (but don't reboot)
- Edit `/boot/config.txt` to add `dtoverlay=disable-bt` at end
- Run `sudo systemctl disable hciuart`
- `sudo reboot`
- Log back in
- Insert the RPICT board on the RPi
- The following lines are for testing only and are *not* required
  to make things work:
  - `stty -echo -F /dev/ttyAMA0 raw speed 38400` (should see `38400`)
  - `cat /dev/ttyAMA0` (should see readings)

- `sudo apt-get install python3-pip`
- `sudo pip install pyserial`

- The following lines are only required if you need/want to make config
  changes to the RPICT board (I did not need to):
  - `wget lechacal.com/RPICT/tools/lcl-rpict-package_latest.deb`
  - `sudo dpkg -i lcl-rpict-package_latest.deb`
  - Test with `lcl-run`
  - `lcl-rpict-config.py -a` (copies the content of the epprom to a local file called /tmp/rpict.conf)
  - `lcl-rpict-config.py -a -w /tmp/rpict.conf` (writes back any edits to `/tmp/rpict.conf`)
  - `/tmp/rpict.conf` is no longer needed.

For more, see http://lechacal.com/wiki/index.php?title=First_Configuration_RPICT:

