(ns cards-in-clojure.cards-to-csv
  (:require [clojure.data.csv :as csv]
            [clojure.edn :as edn]
            [clojure.java.io :as io]
            [clojure.pprint :as pp]))

; General mission card headers
(def csv-headers
  [:title :prerequisite :roll-type :skill :difficulty :success :on-success :success-condition
   :failure :failure-condition :result-condition :failure-tag :card-type :region])

; Development card headers
(def development-headers
  [:category :title :food :timber :ore :mana :luxury :text])

; Resource card headers
(def resources-headers
  [:region :resource-type])

; Favors card headers
(def favors-headers
  [:faction :favor-type])

; Secrets card headers
(def secrets-headers
  [:faction :secret-type])

; Threats card headers
(def threats-headers
  [:title :faction :category :difficulty :failure :text])

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

(with-open [writer (io/writer "..\\..\\csv\\sightrock-mission-cards.csv")]
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

(with-open [writer (io/writer "..\\..\\csv\\gravewood-mission-cards.csv")]
  (csv/write-csv writer
                 (concat [(map name csv-headers)] gravewood-csv-data)))

; Get all alliance cards
(def alliance-cards (-> (io/resource "alliance.edn")
                         slurp
                         edn/read-string))

(def alliance-csv-data
  (map #(get-data-for-headers csv-headers %) alliance-cards))

(with-open [writer (io/writer "..\\..\\csv\\alliance-cards.csv")]
  (csv/write-csv writer
                 (concat [(map name csv-headers)] alliance-csv-data)))

; Get all exploration cards
(def exploration-cards (-> (io/resource "exploration.edn")
                         slurp
                         edn/read-string))

(def exploration-csv-data
  (map #(get-data-for-headers csv-headers %) exploration-cards))

(with-open [writer (io/writer "..\\..\\csv\\exploration-cards.csv")]
  (csv/write-csv writer
                 (concat [(map name csv-headers)] exploration-csv-data)))

; Get all development cards
(def development-cards (-> (io/resource "developments.edn")
                         slurp
                         edn/read-string))

(def development-csv-data
  (map #(get-data-for-headers development-headers %) development-cards))

(with-open [writer (io/writer "..\\..\\csv\\developments.csv")]
  (csv/write-csv writer
                 (concat [(map name development-headers)] development-csv-data)))

; Get all threats cards
(def threats-cards (-> (io/resource "threats.edn")
                           slurp
                           edn/read-string))

(def threats-csv-data
  (map #(get-data-for-headers threats-headers %) threats-cards))

(with-open [writer (io/writer "..\\..\\csv\\threats.csv")]
  (csv/write-csv writer
                 (concat [(map name threats-headers)] threats-csv-data)))

; Get all resources cards
(def resources-cards (-> (io/resource "resources.edn")
                       slurp
                       edn/read-string))

(def resources-csv-data
  (map #(get-data-for-headers resources-headers %) resources-cards))

(with-open [writer (io/writer "..\\..\\csv\\resources.csv")]
  (csv/write-csv writer
                 (concat [(map name resources-headers)] resources-csv-data)))

; Get all favors cards
(def favors-cards (-> (io/resource "favors.edn")
                         slurp
                         edn/read-string))

(def favors-csv-data
  (map #(get-data-for-headers favors-headers %) favors-cards))

(with-open [writer (io/writer "..\\..\\csv\\favors.csv")]
  (csv/write-csv writer
                 (concat [(map name favors-headers)] favors-csv-data)))

