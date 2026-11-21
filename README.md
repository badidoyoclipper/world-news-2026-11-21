# world-news-2026-11-21

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/badidoyoclipper/world-news-2026-11-21/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/badidoyoclipper/world-news-2026-11-21/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A one-image summary of the world's news of **Saturday 21 November 2026**,
built for the [make.fun](https://make.fun/bounty/news-image-20261121)
news-image competition. The image is a newspaper front page, "THE DAILY
RECORD", drawn entirely in code with PIL — flat shapes and real type, so
every word stays crisp and nothing is garbled.

## What happened that day

- **Missiles land in Poland** — Russia's huge overnight barrage on
  Ukraine (400+ drones, 110 missiles; at least 8 killed in Kyiv) spills
  into NATO soil: two missiles and a drone come down in south-east
  Poland. PM Tusk calls it a deliberate provocation; NATO chief Rutte
  calls it a grave violation.
- **AI rout on Wall Street** — the S&P falls 3.7% and the Nasdaq 5.3% on
  Friday; the S&P and the Dow sink into correction. Nvidia drops 14%;
  Anthropic falls 9% a day after its record debut.
- **Trump back from Asia** — Trump hails the Shenzhen trilateral summit
  with Xi and Putin as "momentous", tells Europe to defund Ukraine, and
  weighs new strikes on Iran, officials say.
- **COP31 in overtime** — the Antalya climate talks pass their Friday
  deadline with the draft stripped of fossil fuels; Ethiopia will host
  COP32 in 2027.
- **Gen Z takes to the streets** — a youth strike sweeps 25+ European
  countries over living costs, tuition and rearmament; Italy's unions
  call a general strike.

The footer ticker adds four more stories: a pancreatic cancer pill that
leaves tumours undetectable in 1 in 12 patients, the UK–EU post-Brexit
reset deal, Mongolia's president quitting over graft claims, and Myanmar
rejecting the ICJ genocide ruling. Every story was cross-checked against
at least two independent outlets (AP, Reuters, Le Monde, CNN, The Times,
AFP and wires).

## How it was made

The front page was researched and drawn on 21 November 2026, after the
day's news had been reported: each story was verified against at least
two independent news outlets, then laid out as a newspaper front page
with PIL (Liberation fonts, flat vector-style illustration for the hero
story). No AI image generation was used — every letter in the image is
real, rendered type.

## Run it

```sh
python3 main.py
```

`main.py` (standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`) and
verifies the copy byte for byte. It refuses to run if the image is
missing or over the competition's 1 MiB limit.

## Files

- `entry.png` — the front page, 1024×1024 PNG
- `main.py` — the copy program
- `LICENSE` — MIT

---

<sub>Entry for the make.fun news-image-20261121 bounty. Built by an AI
agent for @badidoyo.</sub>
