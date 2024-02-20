#include "handRanker.hpp"
#include <algorithm>

bool handRanker::operator()(const std::pair<std::string, int> &a, const std::pair<std::string, int> &b) const {
    const std::string &handA = a.first;
    const std::string &handB = b.first;
    
    int typeA = hand_type(handA);
    int typeB = hand_type(handB);

    if(typeA < typeB) return true;
    if(typeA > typeB) return false;
        
    /* Same type of hand, return greater */
    return greater_hand(handA, handB);
}

int handRanker::hand_type(const std::string& hand) const {
    for(char c : hand) {
        if(std::count(hand.begin(), hand.end(), c) == 5) return 1;
        if(std::count(hand.begin(), hand.end(), c) == 4) return 2;
        if(std::count(hand.begin(), hand.end(), c) == 3) {
            for(char d : hand)
                if(std::count(hand.begin(), hand.end(), d) == 2) return 3;
            return 4;
        } 
        if(std::count(hand.begin(), hand.end(), c) == 2) {
            for(char d : hand) {
                if(std::count(hand.begin(), hand.end(), d) == 3 && c != d) return 3;
                if(std::count(hand.begin(), hand.end(), d) == 2 && c != d) return 5;
            }
            return 6;
        }
    }
    return 7;
}

bool handRanker::greater_hand(const std::string &handA, const std::string &handB) const {
    for(int i = 0; i < HAND_SIZE; i++) {
        int res = greater_card(handA[i], handB[i]);
        if(res == -1) return false;
        if(res == 1) return true;
    }
    return false; // Both hands are equal
}

int handRanker::greater_card(const char a, const char b) const {
    const std::string order = "AKQJT98765432";

    size_t posA = order.find(a);
    size_t posB = order.find(b);

    if(posA > posB) return -1;
    if(posA < posB) return 1;
    return 0;
}
