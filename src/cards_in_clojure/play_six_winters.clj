(ns cards-in-clojure.play-six-winters
  (:require [clojure.pprint :as pp]
            [clojure.edn :as edn]
            [clojure.java.io :as io]))


(defn remove-common-cards
  "Return card keys that are in the common card keys"
  [card-keys common-card-order]
  (loop [k card-keys
         c common-card-order]
    (if (empty? c)
      k
      ; Remove the first of the common card keys from the specified card-keys
      (recur (remove #(= (first c) %) k) (rest c)))))

(defn card-string
  "Given a card (map) and card-keys, create a 'nice' string representation of the selected key-value pairs"
  [card card-keys]
  (map #(str % " " (get card % "-")) card-keys))

(defn play-card
  "'Play' a card (print in according to a specified format with common keys printed first and the rest of the
  keys printed after"
  [card]
  (let [common-card-keys [:card-type :title :skill :roll-type :difficulty :success :failure]
        remaining-card-keys (remove-common-cards (keys card) common-card-keys)
        common-card-output (card-string card common-card-keys)
        remaining-card-output (card-string card remaining-card-keys)]
    (println (-> (conj remaining-card-output common-card-output)
                 flatten))))

(defn draw-cards
  "Draw cards from the deck. User presses enter to draw the next card"
  [deck]
  (loop [d deck]
    (when-not (empty? d)
      (play-card (first d))
      (read-line)
      (recur (rest d)))))


; Mimic what a player would do when building the deck - step by step

; Get all cards
(def cards (-> (io/resource "sightrock-deck.edn")
               slurp
               edn/read-string))

(println "The sightrock deck has" (count cards) "cards")

; Get position cards
(def cards-with-position (filter #(contains? % :position) cards))
(println "There are" (count cards-with-position) "cards with position")

; Separate the position cards into three decks
(def first-position-deck (filter #(= (:position %) :first) cards-with-position))
(println "There are" (count first-position-deck) "position cards that go in the first deck")

(def second-position-deck (filter #(= (:position %) :second) cards-with-position))
(println "There are" (count second-position-deck) "position cards that go in the second deck")

(def third-position-deck (filter #(= (:position %) :third) cards-with-position))
(println "There are" (count third-position-deck) "position cards that go in the third deck")


; Get non-position cards
(def cards-without-position (filter #(not (contains? % :position)) cards))
(println "There are" (count cards-without-position) "cards without position")

; Shuffle cards
(def shuffled-cards (shuffle cards-without-position))
; How many cards are in a third of the shuffled deck
(def third-of-shuffled-deck (/ (count shuffled-cards) 3))

; Divide shuffled cards into three decks
(def first-deck (subvec shuffled-cards 0 third-of-shuffled-deck))
(println "The first deck has" (count first-deck) "cards")

(def second-deck (subvec shuffled-cards third-of-shuffled-deck (* 2 third-of-shuffled-deck)))
(println "The second deck has" (count second-deck) "cards")

(def third-deck (subvec shuffled-cards (* 2 third-of-shuffled-deck)))
(println "The third deck has" (count third-deck) "cards")

(def deck
  (concat
    (shuffle (concat first-position-deck first-deck))
    (shuffle (concat second-position-deck second-deck))
    (shuffle (concat third-position-deck third-deck))))

(draw-cards deck)