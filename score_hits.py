import math

def calculate_score(hit_positions, center, radius_scores):
    scores = []
    for (x, y, r) in hit_positions:
        distance = math.sqrt((x - center[0])**2 + (y - center[1])**2)
        score = next((score for (radius, score) in radius_scores if distance <= radius), 0)
        scores.append(score)
    return scores
