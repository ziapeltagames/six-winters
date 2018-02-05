# six-winters

*Six Winters* is the current working title for the *Wrath of the Autarch* boardgame. It combines legacy kingdom building elements, a resource dice game, and a push your luck card driven quest system. It's a mix of games like *Incan Gold*, *Tales of the Arabian Nights*, *7th Continent*, and *Kingsburg*.

This branch is for fleshing out the "dual deck" approach to the game. The following goals are part of this approach.

* A set of two decks, one for progress and one for missions.
* A unification of the previous quest / mission ideas unto one ruleset.

## csv

This is currently the main actively developed area. I have .csv files for most of the cards in the game. They get imported into InDesign in order to quickly create physical card decks for playtesting.

# Turn Sequence

* Progress Phase
   * Resolve triggers
      * Left to right
   * If a development is drawn, resolve card and draw again
* Action Phase (one action)
   * Move characters
   * Buy development
   * Play card
   * Trade (once for each faction per season)
* Test Phase
   * Each character may perform one test
   * Required tests must be done first

## Test Types

The test phase could be tricky to figure out. Will need to think about the following sorts of options.

* Optional / Required (default)
   * Maybe tests should default to optional, with required being a modifier used sparingly
   * If there are two required tests in conflict, the player can choose how to resolve them
* Solo / Lowest / Group (default)
   * Solo means any character the player controls, or any character at the location, but only one can make the test per turn!
   * Lowest means the character with the lowest value of a skill
* Ongoing / One-time (default)
   * Ongoing will most likely have progress tracks on the card

## Season Setup

* Gather Resource Dice
* Spotlight Player Rolls Resource Dice
* Draw Threats
* Choose Missions
* Divide Up Characters
* Draw Starting Mission Cards
* Place Characters at Starting Locations

# The Progress Deck

The Progress Deck contains the following elements.

* Character Card (1-4)
* Development (1-N)
* Triggers (20)

## Questions

* Do you need a timer deck at all?
   * Or is it better to just put symbols on those cards and let the mission card decide what it all means?
* What's on the mission cards?
   * Symbols?
      * Seasons (winter, summer, spring, fall), Magic, Environment, Base Attack, Severe Attack, Timers
   * Instructions to draw from a deck (location or encounter)?

# Missions

A mission pack is split into three parts.

* Mission Description
   * Difficulty
   * Relevant Skills
   * Flavor Text
   * Assets Available
* Mission Cards (1-N)
   * The location deck has 1-N cards in a specific ordering
   * Some locations can be marked S for starting locations
* Encounters (usually 12+ or 6+)
   * Types: Challenge, Event, Location
   * Tags: Dweomer, Guard, Obstacle, Environment, Asset
   * Effects: Sticky, Move
   * Triggers: "On Completion", "On Entering Play", "Time's Up", "Return To Red Bank", "Lowest", "Solo", "Group"

The location deck needs a mechanism to progress through it in sequence. It may even just be coupled with an "On Completion" trigger. So, sometimes you move through it, and sometimes a card effect may force a draw.

## Questions

* Should a location be in play at all times?
   * This is probably easiest, so you can do "at this location" sort of effects.
   * It also avoids confusing situations where a location goes away or appears and you have to shuffle characters around.
   * On the downside, it might be nice to have missions with no real fixed locations, or locations that evolve and grow.
* How do you get new mission cards?
   * Could draw them based off of a symbol.
   * Could be part of a trigger from another card.
      * For example, an encounter card could unlock something from the mission deck.
* How do you get new encounters?
   * Could draw them based off of a symbol.
   * Could be part of a trigger from another card.

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
   * Military
   * Diplomacy
   * Autarch
* Fortune
* Conditions
* Character Skills
* Character Cards (levels)