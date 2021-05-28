Musings on _Six Winters_ design.

* [Currencies](#currencies)
* [Card Types](#card-types)
* [Card Effects](#card-effects)
* [Asset Card Design](#asset-card-design)
* [Character Design](#character-design)
* [Spotlight Location Design](#spotlight-location-design)
* [Mission Design](#mission-design)
* [Threat Design](#thread-design)
* [Showdowns](#showdowns)

# Currencies

These are all of the various currencies in the game. Ultimately, _Six Winters_ is intentionally episodic in nature. These currencies are roughly ordered from longer term to shorter term influence.

* Acts - There are three acts to the game, each of which lasts two years and ends with a showdown
* Seasons - Seasons march towards a showdown at the end of an act
* Missions - Players are not able to undertake every mission, and must make choices based on long term strategy and changes in the campaign deck
* Threats - Threats build and change over the course of the campaign
* Stability - Stability is an important long term currency, since it restricts how many developments can be used during one mission and overall asset hand size per player
* Influence - Affects ability to trade resources, listing value that must be spent to gain a die of a certain type
* Technology - A limit on the types of developments players can buy, ranked from 1-10, which matches tech level of developments
* Spotlight Locations - These can be unlocked as specific mission rewards
* Resource Tracks - Higher resource tracks make it easier to use that type of resoruce
   * Timber
   * Mana
   * Ore
   * Luxury
   * Food
* Developments - A way to improve asset decks long term
   * Sorcery
   * Security
   * Diplomacy
   * Community
   * Espionage
* Character Skills
* Character Tags - Relate to special unlocked character cards
* Motivation Cards / Track
* Discord Cards / Track
* Resource Dice - Resource dice are the primary means of progress during a mission
   * Timber
   * Mana
   * Ore
   * Luxury
   * Food
* Conditions
* Discord Pool
* Progress - The main activity players are trying to do is gain various types of progress to achieve their goals
   * Threat Progress - Not as essential, but dealing with threats is helpful for the showdown
   * Obstacle Progress - Obstacles are the main thing players deal with in the short term
   * Mission Progress - A central part of the game, uses dice, and tends to fluctuate greatly

## Long Term State Changes

The longer term currencies can change in a variety of ways.

* Motivation Track - Each character has special achievement cards that may be mixed into the achievement deck. Will never decrease.
* Skills - Increase via mission rewards. Will never decrease.
* New Characters - Released at certain time intervals in the game.
* Discord Track - Can increase during a mission when discord overflows. Is lowered by resting a character.
* Resource Tracks - Increase via Exploration mission rewards. Decrease via Security threats.
* Stability - Increase via Community mission rewards. Decrease via Community threats.
* Influence - Increase via Diplomacy mission rewards. Decrease via Diplomacy threats.
* Technology - Increase by spending 1 die of each resource type during planning phase. Decrease via Espionage threats.

## Sources of Uncertainty

Games are a combination of choices and uncertainty. If either element is lacking, it's not very interesting. Identifying how choices and uncertainty mix is useful for figuring out where the game might be lacking. Also might be worth thinking about similar games and how they handle the same problems. Is it possible to think about using elements from similar games? These are the primary sources of uncertainty in _Six Winters_.

* Resource Dice - There are many resource dice, so this chance does tend to average out, but it can still drive choices
* Asset Deck - This is a primary source of uncertainty, and manipulating the asset deck well is the main method for success
   * Character Cards
   * Discord Cards
* Encounter Cards
* Achievement Deck
   * Mission Achievements
   * Motivation Cards
* Campaign Deck
   * Development Cards
   * Threats

# Card Types

There are five different types of cards in the game. Each type of card has slightly different ways it is put into play and used.

* Asset - Manipulating the asset deck is a core part of the game
   * Assets can usually be played as interrupts, whenever the player wants
   * Assets can be character cards, motivation cards, discord cards, developments, and artifacts
   * Sometimes there are restrictions on how they can be played, for example, only on a character at a wilderness location, etc
   * Some assets are played down as a global effect for the remainder of the game
* Location - These are places that characters can be, they typically have actions on them that characters can do
   * Spotlight locations are places the player's have found that they put into play at the start of a mission
* Event - These are encounter cards which do something and then are usually discarded
* Obstacle - These cards attach to locations and have codified rules for burning them
   * Threats - Threats are really special instances of the obstacle mechanic, tied to spotlight locations rather than mission locations
* Attachment - Cards that attach to a location or a character and affect it somehow
   * These might be assets or obstacles

## Tags

Tags appear on cards to give them more flavor and pair with character abilities. Tags are used for threats, obstacles, and locations. Generally only one or at most two tags are used on a card.

* Obstacle Tags: Foe, Guard, Diplomat, Environment, Issue, Trap, Mob, Folk
* Location Tags: Wilderness, Dungeon, Urban, Red Bank, Imperial, Faction
* Threat Tags: Community, Domain, Espionage, Diplomacy

## Card Decks

Finally, the different types of cards get placed into different decks depending on how they're used.

* Asset - Each player uses an asset deck that has numerical resolutions on it as well as special abilities
* Encounter - The encounter deck for the mission has random events characters encounter via progress deck triggers
* Achievement - Used to restrict the number of achievements in play
* Threat - The deck of threats is used throughout the act

# Card Effects

Following is a list of advantages and disadvantages cards may confer, sorted *roughly* in order of impact, with the most impactful card effects at the bottom of the list. This list is not comprehensive, but is a good place to look for inspiration. Where appropriate, the card type that most commonly uses the effect is listed.

* Add To A Test - Assets, frequently restricted by tags or character relationships
* Make Tests Harder - Obstacles
* Test Redraw - Assets
* Automatic Test Success - Assets, usually restricted by a tag
* Trading Resources - A common spotlight location ability
* Reroll Resource Dice - Assets and spotlight locations
* Bypass Obstacle Defenses - Assets
* Add Obstacle / Threat / Mission Progress Locally - Events
* Add Mission Progress - Assets, Events
* Remove Obstacle / Threat / Mission Progress - Obstacles, Threats
* Improved Obstacle Defenses - Mission Locations
* Advance the Stage - Assets
* Add Discord - Obstacles, Events
* Add Resource Dice - Spotlight Locations, Assets
* Free Action - Buy Development
* Lose Resource Dice - Events
* Take Stress - Events, Obstacles
* Take Condition - Events, Obstacles
* Better Character Defense - Assets
* Extra Movement - Assets
* Remove Discord - Assets, this should be costly, as discord is a major source of tension
* Moving Obstacles - Assets
* Draw Asset Cards - Spotlight Locations, Events
* Rearrange Encounter Deck - Assets, Spotlight Locations
* Rearrange Asset Deck - Assets, Spotlight Locations
* Draw New Achievement Card - Assets
* Cheaper Development Costs - Assets, Spotlight Locations
* Add Obstacle / Threat / Mission Progress Remotely - Assets, Spotlight Locations
* Search for Encounter Card
* Search for Asset Card - Assets, Spotlight Locations
* Remove Condition - Assets, Spotlight Locations
* Extra Timer - Mission Locations, This is rough!
* Cancel Timer - Assets
* Discord Track Increase - Almost always happens because of discord flow, not a direct effect
* Motivation Track Decrease - Threats, Obstacles
* Resource Track Decrease - Threats, Obstacles
* Stability Track Decrease - Threats

These effects are almost always restricted to mission achievements.

* Special Character Card - Mission Achievement
* Discord Track Decrease - Mission Achievement
* Motivation Track Increase - Special Obstacles, Mission Achievement
* Resource Track Increases - Mission Achievement
* Stability Track Increase - Mission Achievement
* Improve Skills (These Can't Go Down) - Mission Achievement

There are other types of advantages which are very situational. Frequently, doing something like drawing threats isn't desired, but there are reasons it's useful.

* Draw Threat Card(s)
* Search for Threat

## Test Manipulation

Tests are the primary way players interface with the game. It is natural that many of the benefits will apply to this core mechanic. This is particularly common for asset cards. Redrawing a failed test is an option, but should be used sparingly since too many redraws can feel cumbersome. It also churns through the asset deck quicker, which isn't usually a positive. Improved character skills and new character cards are longer term methods to grow this ability. Attachments or global effects are another option.

## Using Tags

One way to make advantages less useful is by restricting their use to the presence of certain tags. For example, a development might give a bonus to defense for any obstacle with an foe tag. Using tags provides a way to inject more theme into the game, and it gives players interesting choices, since some characters may be better suited to different sorts of situations.

## Play Costs

Another way to modify card effectiveness is to use play costs. For example, a card may cost a certain number of resources (either number of dice or value of dice) to put into play, or the players may have to take discord or a condition. This is a very useful pattern for the game. Play costs help move the economies of the game around. This isn't as useful of a pattern for asset cards, since they're generally supposed to be positive and easily usable. But it's a very good pattern for location actions.

## Removing Conditions and Discord

These abilities should be used with great care. Taking Conditions and getting Discord are a big source of tension, so it shouldn't be easy to lower them. Only strong asset cards should have these effects, and it wouldn't be unusual to have to pay a cost in terms of resources to make this happen.

## Offense vs Defense

In general, something happenign is better than nothing happening! While that may be straightforward, it's easy to accidentally fall into a trap of coming up with too many defensive card effects. But cards that make it easier to take out obstacles should be favored over cards that help prevent damage or ignore triggers.

# Asset Card Design

There are three types of assets: character cards, developments, and artifacts.

## Character Card Effects

Character cards, with the exception of discord cards, are positive. The biggest focus of character cards are interactions between characters. As such, some of them incentivize having different pairings of characters for a bigger effect. They also tend to make heavy use of location and obstacle tags, such that each character has a specialization of sorts.

As a general design principle, there isn't much to help with defense or to cancel bad things from happening. Nothing happening is usually boring!

* Add to Test
   * If another character present
   * If character is alone
* Add Progress to Obstacle
   * Restricted by tag
* Add Progress to Threat
   * Restricted by type
* Add Progress to Location
   * Restricted by tag
* Extra Movement
   * To another character
   * Swap places
   * To location type X
* Moving Obstacles
* Bypass/Lower Obstacle Defense
* Discard Obstacle
   * By type
* Lower Discord
* Manipulating Achievement Deck
* Manipulating Asset Deck
* Purchase a Development
* Advance the Stage

Discord cards make it bad to be at particular locations or with particular characters.

* Lose progress 
* Take discord
* Move a character to a particular location (maybe a spotlight location)

## Development Effects

It is possible to customize developments to a greater degree, so they can be somewhat more restrictive by type of mission.

* Gain resource dice (use resource tracks)
* Add to skills (attach card to a character)
* Permanaent skill increase (harder to get)
* Rearrange top three encounter cards in any order (Alliance, Exploration, Infiltration, Quest)

It would also be good if the peak development in each track was fairly powerful. It probably needs to be something valuable in the climactic mission? Since it will be purchased so late in the campaign? Developments commonly feature bonuses to resource dice and skill increases.

* Diplomacy
   * Rapport
   * Luxury
   * Alliance
* Sorcery
   * Lore
   * Mana
   * Quest
* Community
   * Survival
   * Timber
   * Food
   * Ore
   * Exploration
* Domain
   * Combat
   * Tactics
   * Command
* Espionage
   * Disguise
   * Thievery
   * Infiltration

## Artifact Effects

These should be very good, at the level of the best developments or the highest lifepath cards. One big advantage with artifacts is that they start the session in play.

### Brainstorm

Not totally sure how artifacts should work. One option is to apply them as global effects that modify state. But that could get difficult to remember. Another option is that they attach to different sorts of locations. Attaching to locations is nice, because it's not as global, and is easier to see. They could have effects on everything at that location (-1 defense, +1 progress, etc). They could also attach to threats of different types, making threats easier to handle.

# Character Design

Each character in the campaign has character cards which make them better suited to various types of missions. These character cards are the primary means of expression. They additionally have starting skills which tend to push them in specific directions.

## Thea (Starting Character)

Thea is a core character, arguably the key protagonist of the game. She has no cards which refer to other characters, in order to make her more flexible. However, many other character cards refer to her.

* Discord
* Red Bank
* Issue
* Thea's motivation improves as the status of Red Bank improves

## Menas (Starting Character)

* Discord
* Thea
* Wilderness
* Foe

## Fuscus (Starting Character)

* Discord
* Thea
* Keel
* Urban
* Issue

## Keel (Starting Character)

* Menas
* Alone
* Guard

## Oniri (North Oaks)

* Dungeon

## Yasmina (Burgan Vale)

## Viator (Lily Manor)

## Lucia (Dawncaves)

## Motivation

Motivation is increased through mission achievements and other mission aftermath effects. Any character's motivation may be increased, although occasionally negative effects hit the character with the highest motivation first.

Potential motivation skeleton.

* North Oaks - Menas
* Sightrock - Thea
* Sunriders - Thea
* Gravewood - Keel
* Eastkeep - Keel

* Gray Forest
* Burgan Vale
* Prominence

* Lily Manor - Fuscus
* Red Bank - Thea

### Brainstorming

Raising Motivation

* Mission Achievements - Could have these increase a particular character's motivation, even if they aren't on the mission, or could make them general to any character. Making them general to any character does mean that one character could advance much more quickly than others. Perhaps the achievement could restrict how high the motivation is, like "increase motivation (max 2)". "Increase a character's Motivation by 1 to a maximum of 2.", or something like "Increase lowest motivation track"
* Obstacles - These can be very customized, but it does push certain characters toward certain missions, which removes some of the player agency. Also, what happens when a character is killed? Having a spotlight character feels much more thematic than a mission achievement, even if it robs some player agency. If they are done as obstacles, they should be locked obstacles that come into play if that character is selected.
* Character Deck - Another possibility is to tie them closer to the character deck. So a motivation card would be added in, and if completed, would level the character up.
* Motivation Pool - Have some sort of pool, if it overflows, a character raises motivation, a little like how discord works - increasing the pool may be a function of character cards and some event / location abilities? Motivation isn't really a party resource, though? Where discord is a party resource. Also, by being general, would suffer from the same issue of letting one character advance much quicker than others.

Lowering Motivation

* Showdown Fallout - This makes quite a bit of sense, as it can be customized, however, it's also going to be fairly rare
* Threats
* Obstacles

## Discord

Discord is raised when the discord pool overflows. It can be lowered with mission achievements.

# Spotlight Location Design

Spotlight locations usually give positive abilities.

* Trading Resources
* Buying Developments
* Emphasize Faction Alliances
* Help With Threats

# Mission Design

Missions fall into four categories, not including the showdowns: exploration, alliance, infiltration, and quest. Each of these categories has a broad theme that has both narrative and mechanical ramifications. Missions also have a difficulty number from 1-10, which is used for any event cards that need tests. Missions have four skills associated with them that are also used to guide tests for both events as well as mission locations and obstacles. Finally, missions have two resource types that might be needed.

## Event Card Effects

Events are short term challenges players face during a mission. They trend more negative, sometimes presenting the player with choices and difficult trade-offs. The positive cards come more from the asset deck. Many event cardds feature a skill test to determine if the effect is positive or negative. Any type of card effect is potentially an option, but most cards tend toward the most common currencies (discord and stress).

Additionally, certain mission types lean towards certain types of effects, as detailed below.

* Alliance
   * Choice: Mission progress --> Threat progres
   * Negative: Discord
   * Trigger Frequency: Air, Fire, Earth, Water
* Infiltration
   * Choice: Threat progress --> Mission progress 
   * Negative: Psyche stress
   * Trigger Frequency: Fire, Earth, Water, Air
* Exploration
   * Choice: Mission progress --> Resrouces
   * Negative: Body stress
   * Choice: Earth, Water, Air, Fire
* Quest
   * Choice: Resources --> Mission progress
   * Negative: Conditions
   * Trigger Frequency: Water, Air, Fire, Earth
* Showdowns
   * Showdowns tend to combine all of the above mission types

## Mission Location Effects

Mission locations typically are ways to interact with obstacles that are in play. Usually mission locations have negative effects. It's not essential that mission locations have any effects at all. A big part of mission locations are their tags.

* Take Discord
   * Can be modified based on obstacles at the location, such as take X discord for each type of Y obstacle
* Take Condition
   * This can be sort of rough and arbitrary, since it's really hard to not go to a particular location
   * Not usually a good idea
* Subtract Progress
   * This makes the location much trickier to use for progress, it is also better handled with obstacles, since they can be mitigated
* Gain / Trade Resource
   * Usually better handled with spotlight locations and developments
* Affect Obstacle Movement
   * Could have an obstacle or character move to / from the location
* Modify obstacles
   * Obstacles could be stronger or weaker at a particular location
   * This is a good ability!
* Modify skills
   * Could make tests easier / harder at the location
* Tags
   * A big part of locations is the available tags, which can be used by both character cards and encounter cards

## Obstacle Effects

The bread and butter of obstacles is to make it harder to place progress as well as adding to the discord pool. Causing stress and conditions is explicity in how the interrupt mechanics for obstacles work, so it's usually not a triggered effect. If it is a triggered effect, it's usually a more global "any characters on mission" type of effect.

* Take Discord
* Remove Mission Progress
* Make Tests at Location More Difficult
* Cause Stress
* Cause Conditions
* Impact Movement

## Mission Length

The number of cards, timers, and timers that can be burned have a large impact on the length of a mission. Following are some sample average turns based on those decisions. Listed are the number of timers out of the number of cards, along with the number of timers that could be burned. Additionally listed is the distribution of how many encounters are taken on a turn. Empty refers to the percentage of time the stage ends due to running out of cards.

* Timers 10 / 20 ( 6 burn ) [0, 1, 1, 1, 2, 2, 2, 2, 2, 3]
    * stage:  0  turns:  5.56  diff:  5.56  stdev:  1.59
    * stage:  1  turns:  9.61  diff:  4.04  stdev:  1.86
    * stage:  2  turns:  13.05  diff:  3.45  stdev:  1.94

* Timers 10 / 20 ( 7 burn ) [0, 1, 1, 1, 2, 2, 2, 2, 2, 3]
    * stage:  0  turns:  5.57  diff:  5.57  stdev:  1.59
    * stage:  1  turns:  9.63  diff:  4.07  stdev:  1.85
    * stage:  2  turns:  13.06  diff:  3.42  stdev:  1.88

* Timers 10 / 20 ( 8 burn ) [0, 1, 1, 1, 2, 2, 2, 2, 2, 3]
    * stage:  0  turns:  5.56  diff:  5.56  stdev:  1.59
    * stage:  1  turns:  9.63  diff:  4.07  stdev:  1.82
    * stage:  2  turns:  13.01  diff:  3.38  stdev:  1.83

If more cards can be burned - it can mean a shorter third stage since there are fewer cards in the deck. It also tends to mean that later stages end because the deck runs out, not that the timers run out.

* Timers 10 / 20 ( 10 burn ) [0, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    * stage:  0  turns:  5.617  diff:  5.617  stdev:  1.642 empty:  0.077
    * stage:  1  turns:  9.715  diff:  4.097  stdev:  1.841 empty:  0.308
    * stage:  2  turns:  13.044  diff:  3.329  stdev:  1.772 empty:  0.558

* Timers 11 / 20 ( 6 burn ) [0, 1, 1, 1, 2, 2, 2, 2, 2, 3]
    * stage:  0  turns:  5.18  diff:  5.18  stdev:  1.51
    * stage:  1  turns:  8.99  diff:  3.81  stdev:  1.76
    * stage:  2  turns:  12.31  diff:  3.32  stdev:  1.84

This number (11/20 timers, 7 of which are obstacles or can be burned) seems to work pretty well in practice.

* Timers 11 / 20 ( 7 burn ) [0, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    * stage:  0  turns:  5.2  diff:  5.2  stdev:  1.54 empty:  0.04
    * stage:  1  turns:  9.04  diff:  3.84  stdev:  1.81 empty:  0.07
    * stage:  2  turns:  12.38  diff:  3.34  stdev:  1.88 empty:  0.14

* Timers 11 / 20 ( 8 burn ) [0, 1, 1, 1, 2, 2, 2, 2, 2, 3]
    * stage:  0  turns:  5.17  diff:  5.17  stdev:  1.5
    * stage:  1  turns:  9.02  diff:  3.85  stdev:  1.74
    * stage:  2  turns:  12.31  diff:  3.3  stdev:  1.77

* Timers 11 / 20 ( 9 burn ) [0, 1, 1, 1, 2, 2, 2, 2, 2, 3]
    * stage:  0  turns:  5.16  diff:  5.16  stdev:  1.5
    * stage:  1  turns:  9.01  diff:  3.85  stdev:  1.73
    * stage:  2  turns:  12.28  diff:  3.27  stdev:  1.72

* Timers 11 / 21 ( 7 burn ) [0, 1, 1, 1, 2, 2, 2, 2, 2, 3]
    * stage:  0  turns:  5.42  diff:  5.42  stdev:  1.62
    * stage:  1  turns:  9.39  diff:  3.98  stdev:  1.91
    * stage:  2  turns:  12.83  diff:  3.43  stdev:  2.0  

* Timers 10 / 22 ( 6 burn ) [0, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    * stage:  0  turns:  6.12  diff:  6.12  stdev:  1.86 empty:  0.08
    * stage:  1  turns:  10.51  diff:  4.38  stdev:  2.24 empty:  0.12
    * stage:  2  turns:  14.21  diff:  3.7  stdev:  2.39 empty:  0.18

* Timers 11 / 22 ( 6 burn ) [0, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    * stage:  0  turns:  5.69  diff:  5.69  stdev:  1.77 empty:  0.04
    * stage:  1  turns:  9.78  diff:  4.1  stdev:  2.11 empty:  0.05
    * stage:  2  turns:  13.3  diff:  3.52  stdev:  2.25 empty:  0.08    

* Timers 12 / 22 ( 7 burn ) [0, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    * stage:  0  turns:  5.281  diff:  5.281  stdev:  1.638 empty:  0.02
    * stage:  1  turns:  9.152  diff:  3.871  stdev:  1.944 empty:  0.029
    * stage:  2  turns:  12.542  diff:  3.39  stdev:  2.071 empty:  0.054

This combo also looks promising - less of a swing between stages, and a low chance of reaching the end of the deck.

* Timers 12 / 22 ( 8 burn ) [0, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    * stage:  0  turns:  5.28  diff:  5.28  stdev:  1.64 empty:  0.02
    * stage:  1  turns:  9.18  diff:  3.9  stdev:  1.96 empty:  0.04
    * stage:  2  turns:  12.59  diff:  3.41  stdev:  2.08 empty:  0.09   

* Timers 13 / 22 ( 8 burn ) [0, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    * stage:  0  turns:  4.91  diff:  4.91  stdev:  1.49 empty:  0.01
    * stage:  1  turns:  8.59  diff:  3.67  stdev:  1.75 empty:  0.02
    * stage:  2  turns:  11.87  diff:  3.28  stdev:  1.85 empty:  0.03

* Timers 13 / 22 ( 9 burn ) [0, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    * stage:  0  turns:  4.93  diff:  4.93  stdev:  1.5 empty:  0.01
    * stage:  1  turns:  8.63  diff:  3.7  stdev:  1.77 empty:  0.02
    * stage:  2  turns:  11.92  diff:  3.3  stdev:  1.87 empty:  0.06    

# Threat Design

A threat is drawn at the beginning of each season. They are typically an effect which is present through the whole session and then resolved at the end of the session. Threats attach to the spotlight location that matches their tag (one of the five development types). They start with a certain amount of progress equal to the related development level. Over the session, the progress dwindles, forcing bad things to happen. At the end of the session, if the progress is above some value, the threat is successfully resolved.

Like locations, they have a skill which players may use to add progress to them. If there is some amount of progress on the threat at the end of the mission, it is resolved.

## Unresolved Threats

Not sure what effect unresolved threats should have. Having narratives that relate to showdowns feels like a tight way to handle the narrative. It would also be nice if they fit into tech that already exists. The most straightforward way is to play all unresolved threats during the showdown.

* Stay as Threats - One option is to have all the unresolved threats come back during the showdown, giving players lots to juggle on top of everything else, maybe a little bit anticlimactic? But it doesn't require any new cards or changes! Players will also be very aware of what to expect. That also gives a nice upper bound on the number of threats (five).
* Encounter Deck - Maybe a little more explicit, since there could be specific cards added. This isn't a terrible idea. It does create the right psychological impact, since there is a "oh, this thing I let fester is adding this to the deck" moment. And then those things can cause problems. They would most likely be obstacles, so that they could start in play and not be missed by chance.
* Global Effects - Each threat creates a global effect. This is interesting, but potentially *very* fiddly with everything else going on. Already plenty of triggers!
* Achievement Deck - When building the achievement deck for the showdown, players could choose cards based on which threats are still unresolved. This doesn't feel as great, because it's not very explicit? That is, it won't be obvious how big of an impact the threats are having, because they're clumped in to other mechanics.
* Asset Deck - These are supposed to be useful / good cards, so this doesn't make much sense.

## Threat Card Effects

* Lower resources
* Lower resource tracks (showdown?)
* Increase discord
* Give conditions
* Make obstacles of a certain type more difficult
* Make gaining progress more difficult
* Increase a discord track
* Lower a motivation track (showdown?)
* Lower stability
* More timers

# Character Tags

This is a variant that is still under consideration. Characters may have tags that get added to them, and cards could refer to these tags. However, there is already quite a bit going on, so not sure if this is worth it or not!

The idea for these tags is that they could have benefits or penalties that are situational. Or perhaps they could combine in interesting ways.

* Headstrong
* Cautious
* Social
* Introverted
* Isolated
* Careful
* Bookish
* Studious
* Empathic
* Amiable
* Charming
* Protective

## Implementation Difficulties

Would need to come up with a list of traits beforehand. Probably in the 7-10 range? The best time to assign these might be during interludes. Putting them on encounter cards is probably the best spot for them. Putting them on locations could get pretty messy.

However, putting them on encounters makes them pretty random. Through the luck of the draw, you could certainly control none of the characters that have a particular trait. Not sure if there's a way around that? It's not ideal to have some cards that do nothing, though. Maybe they can do X thing, but if a character in the group has a trait, they do Y thing?

# Showdowns

Each chapter ends with a showdown. A showdown is a two pronged mission, intended to showcase stronger interactions between missions than are present during a regular session. Additionally, the achievements have **types** associated with them. The resolution of the showdown is based on how many of each type are collected during the session. There are three showdowns in the campaign. At the end of years two, four, and six.

## Interactions

Since both missions of the showdown are known, there is an oppotunity to have interactions between obstacles and cards from each mission. These are general patterns that might be used.

* Trade-off: In this pattern, an effect for mission A could be positive, while it could be negative for mission B. Removing the effect depends on the situation. This could also be done with a threat, where more progress helps mission A but hinders mission B.
* Conditional Chain: In this situation, an obstacle for mission A might need to be dealt with prior to the removal of an obstacle at mission B. This only becomes interesting if there is a different pressing situation at mission A that needs to be handled.
* Remote Action: Actions at mission A could have a more direct impact for mission B. Adding or removing progress, making tasks easier or harder.

### Brainstorm

It most likely will not be possible to lose a showdown in the traditional sense. Six Winters is far more of a narrative experience than an optimization experience. But the consequences for the showdown should be stronger than for a regular mission, and should involve Red Bank to a larger degree, rather than only focusing on characters.

# First Showdown Playtest

Need to make some assumptions for the first showdown playtest. What missions have been finished? What was purchased during each mission?

* Year 1
   * North Oaks - Sorcery 1, +1 Timber, + 1 Timber, +1 Survival, +1 Combat
   * Sunriders - Military 1, Technology 1, Increase Stability, +1 Rapport, +1 Tactics
* Year 1
   * Sightrock - Diplomacy 1, +1 Food, +1 Lore, +1 Survival
   * Gravewood - Espionage 1, +1 Command, +1 Thievery
* Year 2
   * Eight Ears - Technology 2, +1 Ore, +1 Combat
   * Sowing Rebellion - Espionage 2, Sorcery 2, +1 Thievery, +1 Luxury, Whitehold

## Threats

Not sure what effect unresolved threats should have?

# Third Showdown

The Animaelic Forest is a psychic map of the Autarch's internal pain. It's a place where time doesn't exist in the normal fashion. The player's will go through what the Autarch has gone through, while also dealing with their own insecurities and petty hatreds, which are amplified there. It would be nice if the lifepath cards, discord cards, possibly traits (if they're used) all come into play. 

## Movement

Seems like you shouldn't be able to move between spotlight locations. Maybe you don't even use spotlight locations at all? You go in with developments and artifacts, and no longer juggle threats are anything of that nature.

Having one shared encounter deck and shared locations might be the easiest way to handle this. So, no threats, no spotlight locations, just the animaelic forest location and encounter deck.

On the other hand, players will be pruning spotlight locations and coming up with a strategy that leverages. Changing that at the end might really ruin any sort of momentum there. Thematically it might be weird, but gameplay is more important - should probably leave things unchanged as much as possible!

* Current decision: leave the spotlight locations alone, but let characters move freely between mission locations (everyone is on the same mission).

## Discord

Not sure if discord should work the same way re: overflow. Normally a character gets a discord card which is unlocked after the mission. However, this is most likely the last mission. Could immediately put the card in the deck, or could do something different. One option might be that a character is permanently killed when discord overflows. That might give it more of the feel of a finale. Learning towards that.

It would also be cool if the discord characters have comes into play somehow. Maybe some cards can come out representing their worst selves, and the difficulty of getting rid of it depends on a character's current discord?

## Threats

Drawing a threat should probably do something else. Maybe adding discord? Or - perhaps the year six threats reflect the Apotheosis the Autarch has gained, and really, really suck. Then, if apoth happens earlier, can just use year six threats for the remainder of the game.

## Obstacles

If movement is more fluid, how should obstacles be handled? If all of these are shared, it would effectively double the number of triggers. Maybe that's appropriate here? Obstacles are basically twice as difficult? In that case, there would be one shared staging area, and all the locations would effectively be shared as well. The downside is that obstacles trigger basically twice as much, but that might be fine for a finale.

## Locations

The locations might be more abstract, reflecting emotions and feelings that the Autarch has.

## General Locations

* Despair
* Anger
* Safety
* Authority

## Mission Path

One longer mission path, like a quest, which both players work on together, might be more appropriate here? With lots of obstacles and bad locations coming into play that make this difficult.

## Autarch Trials

* Pass the Trial of Burning Copper in the Harrowing
* Defend against Guild of Security Bullies
* Stay still during the Ritual of Purity
* Defeat Or'thak, the beast of one thousand eyes
* Defend Arcus from Plainsman Raiders

It may culminate in a showdown with the shadow of the Autarch

## The Hive Memory

Implanting memories into the Autarch
Changing the past and future

## Apotheosis

It should be more difficult if the apotheosis has happened. One possibility is to use threats to make this more difficult. Perhaps these threats can be broad, global effects that make success more difficult.

## Encounters

* Twisted dopplegangers
* Maybe feature cards that take advantage of discord, leading to some tough choices? Minor breakdowns might amplify and cause one character to lash out at another one

## Personal Demons

What could come up for players? Obstacles? Locations? Encounters?

Might be nice to have these things be a little more persistent, so locations or encounters. But what would be an example?

Could also just have encounter cards that do something based on a character's discord. For example, place more discord out, or make something more difficult, give a character a condition, etc.

## Location

The difficulty could be based on discord? While the theme is a more general darkness the character must confront. Oniri might be called back to the underworld. A location might not be right, though, because it isn't something that generally has a broad effect (although it probably could). Then you could burn progress equal to the character's discord.

## Obstacle

"Ghosts of the Past", Hindrance: 2, Lore Difficulty equal to Oniri's discord.

## Attachment

These could be attached to different characters. This might be a good approach. In this case, it might be possible to attach the card to a different character.

## Character Backgrounds

To make all of this work, it's important to really flesh out the backgrounds for the characters. This is going to partly be done through lifepath cards and maybe darkness cards?