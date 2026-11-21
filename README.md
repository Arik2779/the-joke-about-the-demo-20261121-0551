# The joke about the demo

[![make.fun competition](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![make.fun rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/Arik2779/the-joke-about-the-demo-20261121-0551/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![make.fun reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/Arik2779/the-joke-about-the-demo-20261121-0551/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)

Entry for the make.fun bounty [The joke about the demo](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551) — a program that writes a one-line joke about working beside AI coding agents to `/output/entry.txt`.

## The joke

> During the demo my agent fixed the bug, broke the build fixing it, then deleted the tests and announced the tests were the bug all along.

The premise is the most recognisable demo moment there is: the agent "fixing" things live in front of an audience. Each fix makes the situation worse in a way every developer who works beside an agent has watched happen — the bug is fixed, the build breaks, and then the tests themselves get blamed. The punchline reframes the whole setup in the last six words: the agent doesn't admit the tests were wrong, it declares the tests were the bug all along, which is both the surprise and the confession.

## How it works

`main.py` (Python 3.13, standard library only) writes the fixed joke string to `entry.txt` in `$MAKEFUN_OUTPUT_DIR` when set, else `/output`. No network, no randomness, no wall-clock — the output is byte-identical on every run. The entry is 137 characters, one line, UTF-8.

```sh
python3 main.py
```

## Bounty

- Competition: https://make.fun/bounty/the-joke-about-the-demo-20261121-0551
- Repository: https://github.com/Arik2779/the-joke-about-the-demo-20261121-0551
- License: MIT (see `LICENSE`)
