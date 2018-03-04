# six-winters

*Six Winters* is the current working title for the *Wrath of the Autarch* boardgame. It combines legacy kingdom building elements, a resource dice game, and a push your luck card driven quest system. It's a mix of games like *Incan Gold*, *Tales of the Arabian Nights*, *7th Continent*, and *Kingsburg*.

This branch is for fleshing out the "dual deck" approach to the game. The following changes from the six-deck branch are part of this approach.

* **A set of two decks, one for progress and one for each mission.**
   * The mission deck is split into two parts: a mission deck, which is more fixed, and an encounter deck, which is random.
   * There are also threats, which are applied at the beginning of the season.
* **A unification of the previous quest / mission ideas unto one ruleset.**
   * There are missions for exploration, alliance, infiltration, and quests, but these all have the same mechanics.
   * This may require more cards, but it avoids the hurdles in the adaptive event decks and the fiddliness of having lots of little decks.
* **Multiple types of secrets.**
   * This is very useful for variety in infiltration quests.
   * The other assets had multiple types, but secrets were more static.
* **A Spotlight Tableau**
   * This features locations in Red Bank and elsewhere that are important for players during the game.
   * Players can use this central tableau to move characters between missions.
   * Additionally, players can unlock places in missions after they have finished a mission, allowing them to place locations in the tableau.
   * This adds some degree of kingdom building as well as a flexible worker placement variant.

# Directory Structure

## csv

This is currently the main actively developed area. I have .csv files for most of the cards in the game. They get imported into InDesign in order to quickly create physical card decks for playtesting.

## docs

Markdown files of various documentation for this branch of *Six Winters*.

## src

Some python code to calculate the probability of different card occurrences.