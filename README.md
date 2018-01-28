# six-winters

*Six Winters* is the current working title for the *Wrath of the Autarch* boardgame. It combines legacy kingdom building elements, a resource dice game, and a push your luck card driven quest system. It's a mix of games like *Incan Gold*, *Tales of the Arabian Nights*, *7th Continent*, and *Kingsburg*.

## csv

This is currently the main actively developed area. I have .csv files for most of the cards in the game. They get imported into InDesign in order to quickly create physical card decks for playtesting.

## doc

Musings on rules, playtests, background setting, and various textual artifacts. My goal is to keep all design artifacts as markdown text for as long as possible.

[Rules](doc/RULES.md)

[Heroes](doc/HEROES.md)

[Stronghold](doc/STRONGHOLD.md)

[Components](doc/COMPONENTS.md)

[Setting](doc/SETTING.md)

[Open Design Questions](doc/QUESTIONS.md)

### Playtests

To-do: Playtests should probably be documented on boardgamegeek. Haven't kept this up at all.

[Sightrock Mission 08_06_17](doc/playtests/170608_SIGHTROCK_ONE.md)

## src

The clojure model simulates the mission card deck for rapid prototyping purposes. This enables various deck builds to be tested quickly without the overhead of physical cards. This code is now out of date. It may be resurrected at some point.

### resources

Contains various card decks I'm experimenting with during playtesting. These are used for the clojure model.
