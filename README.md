# six-winters

*Six Winters* is the *Wrath of the Autarch* boardgame. It combines the kingdom building elements of the role-playing game with a sandbox dice game.

Influences: *Wrath of the Autarch*, *Incan Gold*, *Dicey Dugneons*, *Noctiluca*, *Sagrada*, *Oath*, *Arkham Horror Cardgame*, *Terraforming Mars*, *That's Pretty Clever*, *Pandemic: Legacy*, *Fantastic Factories*, and *Kingsburg*.

# How to Play

The prototype game is on *Tabletop Simulator* and the current rules are located [here](docs/RULES.md).

# Directory Structure

There are three subdirectories for organizing content.

## docs

Markdown files for *Six Winters* documentation. The main docs are the rules and a brainstorming doc. Brainstorming is a massive history of my thoughts as I design, and I make no claim it is easily readable. It will give you some insight into the nightmare of designing a campaign tabletop game, if that's your kink.

## csv

This is the main actively developed area. There are .csv files for most cards in the game. They get imported into InDesign via Data Merge to quickly create physical card decks for playtesting. There are cards for missions, progress, and locations, which interact in various ways.

## src

Some python code to calculate the probability of different card and dice combinations in the game. I use this to make informed design decisions. There is also some reinforcment learning code to discover optimal play strategies.