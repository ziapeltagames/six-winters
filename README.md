# six-winters

*Six Winters* is the *Wrath of the Autarch* boardgame. It combines the kingdom building elements of the role-playing game with a sandbox dice game.

Influences: *Wrath of the Autarch*, *Dicey Dugneons*, *Noctiluca*, *Sagrada*, *Oath*, *Arkham Horror Cardgame*, *That's Pretty Clever*, *Pandemic: Legacy*, and *Kingsburg*.

# How to Play

* [Rules](docs/Six_Winters_Rules.pdf)
* [Character Sheets](docs/Character_Sheets.pdf)

## Where to Play

A restricted beta is on *Tabletop Simulator*, and POD copies are available for blind playtesting.

# Directory Structure

There are three subdirectories for organizing content.

## docs

Files for *Six Winters* documentation. The main docs are the rules and a brainstorming doc. Brainstorming is a massive history of my thoughts as I design, and I make no claim it is easily readable. It will give you some insight into the nightmare of designing a campaign tabletop game, if that's your kink.

## csv

This is the main actively developed area. There are .csv files for all the cards in the game. They get imported into InDesign via Data Merge to quickly create physical card decks for playtesting. There are cards for obstacles, progress, locations, and characters.

## src

Some python code to calculate the probability of different card and dice combinations in the game. I use this to make informed design decisions. There is also some reinforcment learning code to discover optimal play strategies. I made limited use of reinforcement learning to determine how long turns might last. Making a reinforcement learning model for the entire game sounded interesting - but is not practical at the moment.