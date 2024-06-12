
def best_score(new_railway, best_railway) -> bool:
    if best_railway is None or new_railway.score() > best_railway.score():
        return True
    else:
        return False
