def game():
    # Sample game function - you can replace this with actual logic
    return int(input("Enter your current game score: "))

def update_hiscore():
    current_score = game()
    hiscore_file = "C:\\Users\\Ahmed Kadiwala\\Desktop\\python-oneshot\\09_File_IO\\chapter 9 -PS\\hiscore.txt"

    try:
        # Try reading the existing Hi-score
        with open(hiscore_file, "r") as file:
            content = file.read().strip()
            if content:
                hiscore = int(content)
            else:
                hiscore = 0  # If file is blank
    except FileNotFoundError:
        # If the file doesn't exist, assume no Hi-score
        hiscore = 0

    # Compare and update if current score is greater
    if current_score > hiscore:
        print(f"New Hi-score! Previous: {hiscore}, Now: {current_score}")
        with open(hiscore_file, "w") as file:
            file.write(str(current_score))
    else:
        print(f"No new Hi-score. Your Score: {current_score}, Hi-score: {hiscore}")

# Calling the function
update_hiscore()

    