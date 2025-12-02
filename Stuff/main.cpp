#include <iostream>
#include <cstdlib>
#include <vector>
#include <set>
using namespace std;


void AppendToEnd(string Array[], int &elementIndex, string ToAppend, int LengthOfArray ) { // for appending to the end of the list
    if( elementIndex < LengthOfArray ) {
      Array[ elementIndex ] = ToAppend;
    }
    elementIndex = elementIndex + 1;
}

int main() {
    string Suits[4] = {"H","S","C","D"};
    string Numbers[13] = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};
    string Cards[52];
    set<string> CardsOnPile = {};
    int elementIndex = 0;

    for (int a = 0; a <= 4 ; a++){
        for (int b = 0; b < 13; b++) {
            string Card = Suits[a] + Numbers[b];
            AppendToEnd(Cards, elementIndex ,Card, 52);
            CardsOnPile.insert(Card);
        }
    }
    for (string card : Cards) {
        cout << card << "\n";
    }

    set<string> ComputerCards;
    int Card1Index = rand() % (CardsOnPile.size()+1);
    string ComputerCard1;

    int Card2Index = rand() % (CardsOnPile.size() + 1);
    string ComputerCard2;

    if (Card1Index == Card2Index) {
        while (Card1Index == Card2Index) {
            Card2Index = rand() % (CardsOnPile.size() + 1);
        }
    }

    int Count = 0;
    for (string card : CardsOnPile) {
        if (Count == Card1Index) {
            ComputerCard1 = card;
        } else if (Count == Card2Index) {
            ComputerCard2 = card;
        }
    }
    Card1Index = 0;
    Card2Index = 0;

    for (auto removeCard = CardsOnPile.begin(); removeCard != CardsOnPile.end(); ++removeCard) {
        if (*removeCard == ComputerCard1 || *removeCard == ComputerCard2) {
            CardsOnPile.erase(removeCard);
        }
    }

    ComputerCards.insert(ComputerCard1);

    return 0;
}