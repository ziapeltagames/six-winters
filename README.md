# six-winters

*Six Winters* is the current working title for the *Wrath of the Autarch* boardgame. It combines legacy kingdom building elements, a resource dice game, and a push your luck card driven quest system. It's a mix of games like *Incan Gold*, *Tales of the Arabian Nights*, *7th Continent*, and *Kingsburg*.

This branch is for fleshing out the "dual deck" approach to the game. The following goals are part of this approach.

* A set of two decks, one for progress and one for each mission.
   * The mission deck is split into two parts: a mission deck, which is more fixed, and an encounter deck, which is random.
   * There are also threats, which are applied at the beginning of the season.
* A unification of the previous quest / mission ideas unto one ruleset.
   * There are missions for exploration, alliance, infiltration, and quests, but these all have the same mechanics.
* Multiple types of secrets.
   * This is very useful for variety in infiltration quests.
* A Spotlight Tableau
   * This features locations in Red Bank and elsewhere that are important for players during the game.
   * Players can use this central tableau to move characters between missions.
   * Additionally, players can unlock places in missions after they have finished a mission, allowing them to place locations in the tableau.

## csv

This is currently the main actively developed area. I have .csv files for most of the cards in the game. They get imported into InDesign in order to quickly create physical card decks for playtesting.

# Turn Sequence

* Progress Phase
   * Draw progress card
   * Resolve triggers
      * Left to right (top to bottom)
   * If a development is drawn, resolve card and draw again
   * If a mission card is drawn
      * Event: resolve immediately
      * Hand: place in hand
      * Location: place as directed
      * Attachment: place as directed
* Action Phase (one action)
   * Move characters
      * Move move to any location in the same mission or to any Red Bank location
         * If at a Red Bank location, may move anywhere
      * If no characters are at mission, the season is over for that player
   * Buy development
   * Play card
   * Trade (once for each faction per season)
* Test Phase
   * Each character may perform one test
   * Required tests must be done first

## Season Setup

* Gather Resource Dice
* Spotlight Player Rolls Resource Dice
* Draw Threats
* Choose Missions
* Divide Up Characters
* Draw Starting Mission Cards
* Place Characters at Starting Locations
   * Either in Spotlight tableau or on mission location

## Test Types

The test phase could be tricky to figure out. Will need to think about the following sorts of options. By default, tests are required, and may be performed by any number of characters at the location. If the test is via an event, multiple characters may only join in on the test if they're at the same location. That is, a group is only those characters together at the same location.

* Optional / Required (default)
   * Maybe tests should default to optional, with required being a modifier used sparingly
   * If there are two required tests in conflict, the player can choose how to resolve them
* Solo / Lowest / Group (default)
   * Solo means any character the player controls, or any character at the location, but only one can make the test per turn!
   * Lowest means the character with the lowest value of a skill
* Ongoing / One-time (default)
   * Ongoing will most likely have progress tracks on the card

# The Progress Deck

The Progress Deck contains the following elements.

* Character Cards (1-N)
* Developments (1-N)
* Triggers (20)

## Questions

* Do you need a timers broken out at all?
   * Or is it better to just put symbols on those cards and let the mission card decide what it all means?
* What's on the mission cards?
   * Symbols?
      * Seasons (winter, summer, spring, fall), Magic, Environment, Base Attack, Severe Attack, Timers
      * The advantage to symbols is that the whole thing could be decoupled
   * Instructions to draw from a deck (location or encounter)?

# Missions

A mission pack is split into three parts.

* Mission Overview Card
   * Mission Name
   * Mission Type
   * Difficulty
   * Relevant Skills
   * Flavor Text
   * Assets Available
   * Permanent Triggers
   * Effects in Play
   * Art
* Mission / Encounter Card Types
   * Hand
   * Attachment
   * Event
   * Location
   * Artifact
* Mission / Encounter Card Tags
   * Wilderness
   * Urban
   * Magic
   * Lair
   * Social
   * Dweomer
   * Foe
   * Guard
   * Obstacle
   * Environment
   * Asset
   * Resource
   * Secret
   * Favor
* Mission Cards (1-N)
   * The missions deck has 1-N cards in a specific ordering
   * Some mission cards may be marked S for cards starting in play
* Encounters (usually 12+ or 6+)
   * Types: Hand, Attachment, Event, Location, Artifact
   * Tags: Wilderness, Magic, Lair, Urban, Social, Dweomer, Foe, Guard, Obstacle, Environment, Asset, Resource, Secret, Favor
   * Triggers: "Completion", "On Entering Play", "Season End", "Return To Red Bank", "Lowest", "Solo", "Group"

## Questions

* Should a location be in play at all times?
   * This is probably easiest, so you can do "at this location" sort of effects. (Current Choice)
   * It also avoids confusing situations where a location goes away or appears and you have to shuffle characters around.
   * On the downside, it might be nice to have missions with no real fixed locations, or locations that evolve and grow.
* How do you get new mission cards?
   * Could progress through them via earlier mission cards. (Current Choice)
   * Could draw them based off of a symbol.
   * Could be part of a trigger from another card.
      * For example, an encounter card could unlock something from the mission deck.
* How do you get new encounters?
   * Could draw them based off of a symbol. (Current Choise)
   * Could be part of a trigger from another card.

# Threats

Two threats are drawn at the beginning of each season. They are typically an effect which is present through the whole season (unless resolved somehow) or an effect which triggers at season's end. The latter is the more common type of threat.

Threats tend to attach to a specific type of location, sometimes the threat will require the players to use a type of location if they have one. Sometimes a threat will take a location slot from those available.

# Currencies

* Seasons (time)
* Apotheosis (time)
* Red Bank Tracks
   * Conquest
   * Sorcery
   * Military
   * Espionage
   * Stability
   * Diplomacy
* Resources
   * Timber
   * Mana
   * Ore
   * Luxury
   * Food
* Faction Dispositions
   * Gravewood
   * Burgan Vale
   * Sunriders
   * Lily Manor
   * Crescent Hold
* Imperial Secrets
   * Guilder
   * Gray Cloak
   * Autarch
* Fortune
* Conditions
* Character Skills
* Character Cards (levels)