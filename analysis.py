import numpy as np

def analyze_hits(hits):
    points = [(x, y) for (x, y, r) in hits]
    if not points:
        return {}

    # Oblicz odległości między punktami
    distances = []
    for i, (x1, y1) in enumerate(points):
        for x2, y2 in points[i+1:]:
            dist = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            distances.append(dist)

    # Analiza wyników
    analysis = {
        'hit_count': len(hits),
        'mean_distance': np.mean(distances) if distances else 0,
        'std_distance': np.std(distances) if distances else 0
    }
    return analysis
