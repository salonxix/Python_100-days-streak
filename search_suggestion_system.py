from typing import List

def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    # Step 1: Sort products lexicographically
    products.sort()
    
    res = []
    prefix = ""
    
    # Step 2: For each character typed, filter products starting with prefix
    for ch in searchWord:
        prefix += ch
        # Get only products that start with prefix
        suggestions = [p for p in products if p.startswith(prefix)]
        # Take only first 3 lexicographically
        res.append(suggestions[:3])
    
    return res


# -------------------------
# Example Run
# -------------------------
products1 = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord1 = "mouse"
print(suggestedProducts(products1, searchWord1))
# Expected: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]

products2 = ["havana"]
searchWord2 = "havana"
print(suggestedProducts(products2, searchWord2))
# Expected: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
