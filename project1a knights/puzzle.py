from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
sentence0a = And(AKnight, AKnave)
knowledge0 = And(
    # Or(AKnight, AKnave), # A is either a knight or a knave
    Not(Biconditional(AKnight, AKnave)),

    Implication(AKnight, sentence0a), # when A is knight
    Implication(AKnave, Not(sentence0a)) # when A is knave
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
sentence1a = And(AKnave, BKnave)
knowledge1 = And(
    # Or(AKnight, AKnave), # A is either a knight or a knave
    # Or(BKnight, BKnave), # B is either a knight or a knave
    Not(Biconditional(AKnight, AKnave)),
    Not(Biconditional(BKnight, BKnave)),

    Implication(AKnight, sentence1a),
    Implication(AKnave, Not(sentence1a))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
sentence2a = Or(And(AKnight, BKnight), And(AKnave, BKnave))
sentence2b = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    # Or(AKnight, AKnave), # A is either a knight or a knave
    # Or(BKnight, BKnave), # B is either a knight or a knave
    Not(Biconditional(AKnight, AKnave)),
    Not(Biconditional(BKnight, BKnave)),

    Implication(AKnight, sentence2a),
    Implication(AKnave, Not(sentence2a)),
    Implication(BKnight, sentence2b),
    Implication(BKnave, Not(sentence2b))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
sentence3a = Or(AKnight, AKnave)
sentence3b = And(
    Implication(AKnight, AKnave),
    Implication(AKnight, Not(AKnave)),
    CKnave
)
sentence3c = AKnight
knowledge3 = And(
    # Or(AKnight, AKnave), # A is either a knight or a knave
    # Or(BKnight, BKnave), # B is either a knight or a knave
    # Or(CKnight, CKnave), # C is either a knight or a knave
    Not(Biconditional(AKnight, AKnave)),
    Not(Biconditional(BKnight, BKnave)),
    Not(Biconditional(CKnight, CKnave)),

    Implication(AKnight, sentence3a),
    Implication(AKnave, Not(sentence3a)),
    Implication(BKnight, sentence3b),
    Implication(BKnave, Not(sentence3b)),
    Implication(CKnight, sentence3c),
    Implication(CKnave, Not(sentence3c))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()