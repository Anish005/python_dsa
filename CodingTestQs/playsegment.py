'''
A video game developer is developing a game in which the character makes their way through several segments of a level. In each segment, if the character collects a coin, the player scores a point. However, if a segment does not contain a coin, the player loses a point. Player 1 always begins the level, and, at some point, game play is turned over to Player 2 to complete the level. Player 1's goal is to achieve a higher score than Player 2 once the level is completed. Given the status of game segments (whether they contain a coin or not), determine the minimum number of segments Player 1 should play so that, in the end, their score is greater than Player 2's score.

Example

segments = [1, 1, 0, 1]

Player 1 has the following options:

Play O segments. This would give them a score of 0. Player 2 would have a score of 3 - 1 = 2 (because they gain a point for each of the 3 segments with a coin, and lose 1 point for the segment without a coin).

Play 1 segment. This would give them a score of 1. Player 2 would have a score of 2 - 1 = 1.

Play 2 segments. This would give them a score of 2. Player 2 would have a score of 1 - 1 = 0.

A

Only in this last case, by playing 2 segments, would Player 1's score be greater than Player 2's. Therefore, return the answer 2.
'''




def playSegments(coins):
    total_coins = coins.count(1)
    total_segments = len(coins)
    
    player1_score = 0
    player2_score = total_coins
    
    min_segments = total_segments + 1
    
    for i in range(total_segments):
        if coins[i] == 1:
            player1_score += 1
            player2_score -= 1
        
        if player1_score > player2_score:
            min_segments = min(min_segments, i + 1)
    
    return min_segments if min_segments <= total_segments else 0

# Example usage:
segments = [1, 1, 0, 1]
result = playSegments(segments)
print("Minimum segments for Player 1:", result)
