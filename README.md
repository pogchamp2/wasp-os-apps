# [wasp-os](https://www.github.com/daniel-thompson/wasp-os) apps
Some [wasp-os](https://www.github.com/daniel-thompson/wasp-os) apps made for the Pine64 [PineTime](https://pine64.com/product/pinetime-smartwatch-sealed/), but should work elsewhere.

## cookie.py

This is a Cookie Clicker clone for [wasp-os](https://www.github.com/daniel-thompson/wasp-os).
It was initially made for the [PineTime](https://pine64.com/product/pinetime-smartwatch-sealed/), and
here's a screenshot.
<img src=https://github.com/pogchamp2/wasp-os-apps/raw/main/CookieApp.png alt=CookieApp.png/>
<br/>
You'll have to compile it. There's not enough memory to parse the full file.
The number below `FF` is how many 'cookies' tapping adds.
The number below `AC` is how many cookies are added every second.
The square of Cs are supposed to be the cookie.
Tap the FF to upgrade it. (Cost:100)
Tap the AC to upgrade *it*. (Cost:200)
At the bottom is the time and battery percentage.
The game saves its numbers onscreen to `cookie.save`.
The save is triggered when the app is backgrounded for any reason.
