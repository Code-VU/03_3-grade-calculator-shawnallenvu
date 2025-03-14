def calculateGrade():
    print("Calculating Grade")

    # Grading Criterion
    #  Score   Grade
    # >= 0.9     A
    # >= 0.8     B
    # >= 0.7     C
    # >= 0.6     D
    #  < 0.6     F

    # Try except for bad user input. Takes score from user 
    try:
        score = float(input("Enter score (0.0 - 1.0) "))
        if not 0.0 <= score <= 1.0: # Checks to make sure score is within bounds
            raise ValueError # forces error so we don't have to write extra code 
    except:
        print("Bad score")
        return
    
    # Match case instead of if else. Keeps comparisons to a minimum and keeps code clean
    match score: 
        case _ if score >= 0.9:
            grade = 'A'
        case _ if score >= 0.8:
            grade = 'B'
        case _ if score >= 0.7:
            grade = 'C'
        case _ if score >= 0.6:
            grade = 'D'
        case _: # Default to F if it doesn't meet above scores
            grade = 'F'

    print(grade) # Print grade

    # end assignment

## If you want to test locally before you try to sync
## Run > python calculateGrade.py

if __name__ == "__main__":
    calculateGrade()
