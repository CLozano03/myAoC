#ifndef HANDRANKER_HPP
#define HANDRANKER_HPP

#define HAND_SIZE 5

#include <string>
#include <utility>

class handRanker {
public:
    handRanker() = default;
    bool operator()(const std::pair<std::string, int> &a, const std::pair<std::string, int> &b) const;

private:
    /**
    * @brief Every hand is exactly one type. From strongest to weakest, they are:
    *   1 - Five of a kind, where all five cards have the same label: AAAAA
    *   2 - Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    *   3 - Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    *   4 - Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    *   5 - Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    *   6 - One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    *   7 - High card, where all cards' labels are distinct: 23456 
    * 
    * @param hand 
    * @return lower number if hand is stronger
    */
    int hand_type(const std::string& hand) const;
    bool greater_hand(const std::string& handA, const std::string& handB) const;
    int greater_card(const char a, const char b) const;
};

#endif
