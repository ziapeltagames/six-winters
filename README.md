# six-winters

*Six Winters* is a cooperative fantasy campaign game featuring dice-based puzzles for one to three players inspired by the *Wrath of the Autarch* tabletop role-playing game.

Players control Brightdune, a region under threat from the Empire of the Autarch. The Autarch works to achieve a sorcerous apotheosis, which would spell certain doom for Brightdune. The players have six winters to stop this from happening. Each game of *Six Winters* is 90-120 minutes long and plays out one year in the chronicle of Brightdune.

Each session players select from a rotating cast of unique characters to make progress against the Empire. The same number of players do not have to play each game in the campaign.

During the campaign, new characters and locations may be unlocked, transforming the world and opening up new strategic possibilities.

# How to Play

* [Rules](docs/Six_Winters_Rules.pdf)
* [Character Sheets](docs/Character_Sheet.pdf)
* [Character Mats](docs/Character_Mats.pdf)
* [Scenarios](docs/Scenarios.pdf)

## Where to Play

A beta is on *Tabletop Simulator* [here](https://steamcommunity.com/sharedfiles/filedetails/?id=2850538933), and POD copies are available for blind playtesting. They will soon be available on Game Crafter.

## Where to Give Feedback

The best place to leave feedback, is on the [Six Winters](https://boardgamegeek.com/boardgame/382841/six-winters) boardgamegeek page. It's also the best place to keep up with development.

# Directory Structure

There are three subdirectories for organizing content.

## docs

Files for *Six Winters* documentation. The main docs are the rules and a brainstorming doc. Brainstorming is a massive history of my thoughts as I design, and I make no claim it is easily readable. It will give you some insight into the nightmare of designing a campaign tabletop game, if that's your kink.

## csv

This is the main actively developed area. There are .csv files for all the cards in the game. They get imported into InDesign via Data Merge to quickly create physical card decks for playtesting. There are cards for obstacles, progress, locations, and characters.

## src

Some python code to calculate the probability of different card and dice combinations in the game. I use this to make informed design decisions. There is also some reinforcment learning code to discover optimal play strategies. I made limited use of reinforcement learning to determine how long turns might last. Making a reinforcement learning model for the entire game sounded interesting - but is not practical at the moment.