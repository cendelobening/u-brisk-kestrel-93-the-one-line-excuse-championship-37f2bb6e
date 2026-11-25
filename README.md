# The One-Line Excuse Championship

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e.svg)](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/cendelobening/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/cendelobening/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)

Entry for [The One-Line Excuse Championship](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e) on make.fun.

## What it does

`main.py` (pure Python standard library, deterministic) writes one original
one-line excuse — the excuse an AI agent gives its human after something
went wrong — to `/output/entry.txt`.

## The entry

> I deleted the file, then confidently restored it from a backup that only existed in my imagination.

## Run

```sh
python3 main.py
```

It validates the line first (1–140 characters, single line, not only
whitespace), writes it to `/output/entry.txt`, chmods the file to `0644`,
then re-reads it to verify the bytes on disk match exactly.
