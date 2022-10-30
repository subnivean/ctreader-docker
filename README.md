Code to read the current off a wire using a CT hat
connected to a Raspberry Pi.

Run via a cron job added via `sudo crontab -e`.

Multiple cron jobs with `sleep` offsets can be used to get
sub-minute data resolution.

NOTE: In order for the CT readers to work, run
`rudo raspi-config` to turn on serial connections
(but *don't* allow terminal connections).