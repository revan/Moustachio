# Moustachio
## Revan Sopher
### HackRU F2014

A Chrome extension / Flask server duo which silently adds a grandiose moustache to the portraits on Wikipedia pages.

![Obama](https://raw.githubusercontent.com/revan/Moustachio/master/examples/1.png)
![Bush](https://raw.githubusercontent.com/revan/Moustachio/master/examples/2.png)
![Zuckerberg](https://raw.githubusercontent.com/revan/Moustachio/master/examples/3.png)

The extension injects Javascript to redirect the image sources to the server, which passes them through
[SkyBiometry](https://www.skybiometry.com/) and uses [Pillow](https://github.com/python-pillow/Pillow) to size and paste on the 'stache.

## Installing
Chrome extension has no requirements (duh).

Server depends on the following python packages:

```
flask
requests
urllib2
Pillow
```
