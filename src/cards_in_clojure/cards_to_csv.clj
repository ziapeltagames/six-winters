(ns cards-in-clojure.cards-to-csv
  (:require [clojure.data.csv :as csv]
            [clojure.edn :as edn]
            [clojure.java.io :as io]
            [clojure.pprint :as pp]))

; General mission card headers
(def csv-headers
  [:title :prerequisite :roll-type :skill :difficulty :success :success-condition
   :failure :failure-condition :result-condition :failure-tag])

; Development card headers
(def development-headers
  [:category :title :food :timber :ore :mana :luxury :text])

(defn get-data-for-headers
  "Get values from card-data for keys corresponding to headers.
   If a value is a keyword, make it a string."
  [headers card-data]
  (->> (map #(get card-data %) headers)
       (map #(if (keyword? %) (name %) %))))

; Get all sightrock exploration cards
(def sightrock-cards (-> (io/resource "sightrock-deck.edn")
                         slurp
                         edn/read-string))
(def sightrock-exploration-cards
  (filter
    #(= (:card-type %) :exploration)
    sightrock-cards))

(def sightrock-csv-data
  (map #(get-data-for-headers csv-headers %) sightrock-exploration-cards))

(with-open [writer (io/writer "sightrock-mission-cards.csv")]
  (csv/write-csv writer
                 (concat [(map name csv-headers)] sightrock-csv-data)))


; Get all gravewood alliance cards
(def gravewood-cards (-> (io/resource "gravewood-deck.edn")
                         slurp
                         edn/read-string))
(def gravewood-alliance-cards
  (filter
    #(= (:card-type %) :alliance)
    gravewood-cards))

(def gravewood-csv-data
  (map #(get-data-for-headers csv-headers %) gravewood-alliance-cards))

(with-open [writer (io/writer "gravewood-mission-cards.csv")]
  (csv/write-csv writer
                 (concat [(map name csv-headers)] gravewood-csv-data)))

; Get all development cards
(def development-cards (-> (io/resource "developments.edn")
                         slurp
                         edn/read-string))

(def development-csv-data
  (map #(get-data-for-headers development-headers %) development-cards))

(with-open [writer (io/writer "developments.csv")]
  (csv/write-csv writer
                 (concat [(map name development-headers)] development-csv-data)))

