# 06/17/21

Working on a pyqt version of the game for rapid prototyping. First step is to mockup the overall layout.

# 05/30/21

## Discord Options

Had one idea of using the discord track as a temporary "heated" meter between two characters. Maybe if two characters gain discord, they can't go on the next mission together? A little fiddly, but could be an interesting way to force different combos of characters together. Rather than always teaming up.

## Trait Options

Watch a video on _Fog of Love_ boardgame. It leans really heavily into the character trait concept, which is cool. However, it's probably not a practical way to handle them for _Six Winters_. There are a number of opposing tracks, like Curiosity or Extroversion, and traits are goals in the game - you want the situation to match your trait. So you steer the game towards situations which reward that trait.

Going along that route, traits would be more like achievements. They're a set of tasks that need to happen.

## Dissonant Trait Mechanics

Part of this process is thinking of what sorts of repercussions the disagreements between characters can have. What mechanical ramifications could there be? Is some new mechanical concept needed?

* Discord increases - this one seems very intuitive and is probably the best reprecussion for dissonant traits
* Characters can't work together - that's pretty heavy handed
* Character takes stress - also a possibility
* Discard cards from hand
* Higher difficulty on tests
* Lower resource track - that's pretty brutal

## Compatible Trait Mechanics

* Commitment increases
* Characters work together better
* Remove/lower stress

## Option A: Simple Trait Cards from Mission Deck

There are good and bad trait cards, which can increase commitment or increase discord. Each character has one of each kind of trait, so four trait cards go into the mission deck. When drawn, the cards remain in the player's hand, and apply toward the hand limit. The only way to get rid of them is to play them when in a scene with another character. The positive cards will add to commitment, and the negative ones will add to discord.

### Pros

Easy to understand and implement. They also have very simple to understand effects.

### Cons

There isn't much nuance here. It would be nice if sometimes a trait could be good in one context, but negative in a different one. Conditional traits seem more fun. There is also a pretty limited diversity of options.

## Option B: Double Trait Cards from Mission Deck

Similar to A, but each trait has two cards: one positive and one negative. Still played for discord/commitment.

## Option C: Double Trait Cards with Conditional Play

Have two trait cards for each trait, and each one is conditional on how its used. Some work for specific kinds of scenes. Some are played when a character is alone, etc. This may be the best idea yet, in the sense that all traits become dual natured.

### Pros

This provides much diversity - but could cause problems if the situation doesn't arise. This has been a problem with player cards. If going this route, it should probably be (Common Effect / Bonus Situational Effect), similar to character cards. Otherwise it's just too hard to play them.

Effectively, then, these cards would be character cards, but get placed in the mission deck. Causing them to take up hand space is a great way to force players to play them, thought.

### Cons

Situational effects are very difficult to tune well. And require more reading/cognitive load.

## Thoughts

Don't want these to be super symmetric, though, because then they're just offsetting randomness.

# 05/22/21

What kind of stories should the scenes tell? Maybe that would help? Also, maybe listing how many scenes are in play would help? The pacing desired?

## Example Fiction

* An audience with Arban the Swift, pledging allegience to him in exchange for military aid.
* A costume ball in the Empire - a fancy dress is made - and secrets are learned.
* Crossing a rushing river in the wilderness, using a makeshift bridge. One character aids another and bonds are formed.
* Mana is drawn from the old rock. It corrupts the character who draws it free.
* A festival in town is ruined by old rivalries and a lovers quarrel.

Not sure all of these can be created in the game, but it's useful to brainstorm how they might.

What about, instead of scenes, if they are more like vows? Or perhaps there are vow cards in the game? And you can give a character a vow?

## Very Freeform Version

Could also go even more freeform, which would probably require creating scenes by writing down details on cards. Maybe a player could write something like a vow, _Irownsworn_ style, and then scenes are ways to make progress on vows.

Vows, Bonds, Twists, Scenes, Assets.

# 05/21/21

In general, the idea of using scene cards that remain in play instead of event cards is interesting. However, if too many cards are in play, the deck will basically empty, and for a game that needs the deck to cycle for triggers, that won't work. Probably still need some number of pure event cards. Maybe they should be simple to resolve, though? Manipulating dice, adding stress, moving obstacles around, operating on threats, etc. No skill tests for events.

Another alternative is to use a limit on scenes, so that if a scene is already in play at a location, the drawn card is ignored.

How can scenes be used to craft a narrative? There's a location, a scene, and characters. There are optionally other obstacles. What other components are useful for a narrative? Relationship? Need? Objects? Maybe brainstorm how these could be used, if they can be used at all. Could possibly have relationship cards, either character cards, or cards from the mission deck. For instance, siblings or lovers or business partners. No idea how/if that would work into the narrative, though. That doesn't feel like something for scenes. Rather, it feels like something that could exist between player characters.

## Option: Specific Scenes

* Scene: Costume Ball
* Location: Secret Gardens
* Need: Impress the Duke, Bake a Cake, Get Information
* Object: Fancy Dress
* Modifier: Raining, At Night, In the Winter, Faux Pas
* Relationship: ?

The relationships don't seem to work so well here. Scenes and locations are pretty obvious. Need/scene is _probably_ the same as well. A scene has a need. Objects make sense, though. Perhaps brainstorm scenes. They can probably come from WotA directly - tons of them there.

### Example Scenes

* Cross a River
* Costume Ball
* Hunting Trip
* Difficult Travel
* Hacking through Vines
* Raging River
* Climbing over Rocky Crags
* Brutal Cold

It's very hard to have scenes like this flexible enough to apply to different mission types.

## Option: Vague Scenes

This option would hew closer to WotA. A scene might be "Risky Escape" or something like that. Scenes could have skills, difficults, and stress. Maybe they could interact with other obstacles and locations present?

What would the success/fail consist of, though? Scenes would probably need triggers to make them interesting. Without triggers, it may be that players never want to deal with them.

There's also the case that having tons of scenes in the progress deck would mean scenes come out _constantly_. And there would basically be a scene at every location, which could get overwhelming. At that point, the other cards really would need to be events or something like that.

If the scenes were vauge, could easily have modifier cards. Objects, conditions, weather, characters, etc. This is more like oracles as well - in games like _Ironsworn_ or _Mythic_.

# 05/19/21

Thinking now about going back to skill tests, but circling in the society stats as well. This would lean heavily into the dice elements. Much of the dice games consists of a system of generators --> modifiers --> receivers, in a loop.

* Generators: skills, resources, achievements, character cards
* Modifiers: character cards
* Receivers: obstacles, achievements, character cards

## Overcome Obstacle

Obstacle Description

* Name
* Type: **Skill + Resource**
* Difficulty: **1-6**
  * Skill dice must be this high to be a success
* Challenge: **1+**
  * How many successes are needed
* Stress Type: <Mental, Physical>
* Stress Amount: **0+**
  * Damage done after every skill test (if not taken out) or to stop trigger
* Trigger (optional)
  * What the obstacle will do if triggered
* Weakness (optional)
  * Special dice combos that will trigger more stress

Working Together  

* If more than one character works together, it still only takes one action - players roll their dice independently
   * However, stress applies to ALL characters making the test

Overcome Procedure

* Roll skill dice
* Apply stress

## Create Advantage

Is something like this possible? Probably not as a separate action. In this game, this just feels like something handled with cards.

## Sample Character Cards

Core Actions:

* Split a die
* Join two dice
* Reroll a die
* Duplicate a die
* Gain a die of a certain type
* Cause stress directly
* Exchange dice
* Trade dice
* Swap out 1 die for other dice
* Defense
* +1
* -1
* Flip die

Bonus Actions:

Most of the above actions could also qualify for bonus actions. The key thing with bonus actions is that they would be tied to specific skills, resources, or characters (including being with another character).

* Draw a card

## Sample Obstacles

Obstacles are things like guards, monsters, issues, scenes. Characters overcome these directly.

## Sample Achievements

# 05/16/21

Character card, fortune-at-the-front options. The current pattern of draw a card and adding it to a skill is kind of boring. Even misses are a little boring, because there are four actions, so it's not even inconvenient. However... missing or losing your turn is a boring complication.

One option is to allow players to play cards directly from their hand. Or, maybe choosing a careful approach from their hand or a risky approach from the deck.

## Option: Careful/risky skills + cards have symbols

In this option, character cards have the following symbols in the upper right hand corner: Success, Mental Stress, Physical Stress, or Discord. They all have at least one of these symbols, but could have more. For isntance, a card could have 2 success symbols.

A player can make a skill test carefully. In this case, they play at least one card from their hand that has a success symbol. The number of success symbols are added to their skill value for the result.

A player can also make a risky test. In this case, they draw cards from the deck up to their skill value (they choose the number before drawing). Every symbol adds one to the skill test, no matter what the symbol is. However! If a mental stress icon comes up, they take mental stress equal to the total number of symbols. If a physical stress symbol comes up, they take physical stress equal to the total number of symbols. And if a discord symbol comes up, they take discord equal to the total number of symbols.

### Pros

It seems more intersting than what's there now. Players can control their destiny more, but there's also an option to really swing for the fences and take lots of consequences in order to get a high result.

### Cons

The risky approach may not be swingy enough. For instance, if there's usually 1 symbol on every card, you kind of know the result. It would be nice if the risky approach could really suck or really be amazing. Also, if the risky card draw is only up to their skill amount, it doesn't open up the really long shot chance with a crappy skill. It would be nice if some really risky skill test is possible, with potentially catastrophic consequences.

Additionally, the conservative approach may not work quite right if you must play a card each time you would like to do a skill test. Skill tests are pretty common: it's possible that multiple times a turn players would like to do a skill test. With limited hand sizes, that becomes tricky. At that point, it's probably necessary to draw up to the hand size each turn. That may make it more feasible?

### Analysis

Hand sizes are based on Stability, but could be from 1-6, most likely around 2 or 3. Skills are currently 0-6. Target numbers should be based on dice ranges: 0 is the lowest result possible, with 12 being the very high end.

### Suboptions

* Spending a card is optional for careful use of skills. That would clearly make it easy to use skills carefully. A character with a skill of 6 could basically grab one die each turn. That does feel a little dry, though.

# 05/15/21

There's always a tension between streamlining systems and offering enough variety that different thematic components in the game feel different. There are various thematic elements in Six Winters: community building, fighting monsters, exploring, breaking into vaults, casting spells, building developments, sneaking past guards, making smalltalk, negotiating.

The key components in the game are the resource dice as well as the deck of character cards.

Dice manipulation options:

* Sets of dice types
* Sets of dice values
* getting specific values of resources
=======
* Specific dice values
* Evens
* Odds
* Totals

Card manipulation options:

* Play cards from hands for numeric totals
* Play cards that match certain symbols/tags
* Use cards as "processing units" for dice types