def isSpam(message: list[str], bannedWords: list[str]) -> bool:
    count = 0
    for word in message:
        if word in bannedWords:
            count += 1
            if count >= 2:
                return True
    
    return False

message = ["hello", "world", "knixnkk"]
bannedWords = ["world", "hello"]
print("Test 1:", isSpam(message, bannedWords))  
