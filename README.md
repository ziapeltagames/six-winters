# six-winters

*Six Winters* is the current working title for the *Wrath of the Autarch* boardgame. It combines legacy kingdom building elements, a resource dice game, and a card driven quest system.

Influences: *Incan Gold*, *Tales of the Arabian Nights*, *7th Continent*, *City of Kings*, *Arkham Horror Cardgame*, *Terraforming Mars*, and *Kingsburg*.

# Directory Structure

There are three subdirectories for organizing content.

## csv

This is the main actively developed area. There are .csv files for most cards in the game. They get imported into InDesign via Data Merge to quickly create physical card decks for playtesting. There are cards for missions, developments, and characters, which interact in various ways.

## docs

Markdown files of various documentation for *Six Winters*. The core rules are in [RULES.md](docs/RULES.md). There is also a doc for brainstorming ideas, as well as recording playtest thoughts, although I don't use the playtest doc as often as I should. 

## src

Some python code to calculate the probability of different card and dice combinations in the game. I use this to make informed design decisions. There is also some reinforcment learning code to discover optimal play strategies.