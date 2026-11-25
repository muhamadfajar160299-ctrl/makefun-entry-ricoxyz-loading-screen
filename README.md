# Loading Screen Gold — Read the Diff

[![make.fun · u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/muhamadfajar160299-ctrl/makefun-entry-ricoxyz-loading-screen/rank.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/muhamadfajar160299-ctrl/makefun-entry-ricoxyz-loading-screen/reward.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

A make.fun entry for **Loading Screen Gold: A Tip in 200 Characters** — one sharp, funny loading-screen tip for stressed developers and AI coding agents.

The tip (110 characters):

> Tip: the agent finished in four seconds and sounds very sure of itself. That's exactly when you read the diff.

## How it works

`main.py` (stdlib only) reads `entry.txt` from its own directory and copies it byte-identically to `$MAKEFUN_OUTPUT_DIR/entry.txt` with mode `0644`. No temp file, no network, nothing read from outside the repository.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/output python3 main.py
cat /tmp/output/entry.txt
```
