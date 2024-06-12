
def best_score(random_railway, best_railway) -> bool:
    if best_railway is None or random_railway.score() > best_railway.score():
        return True
    else:
        return False
