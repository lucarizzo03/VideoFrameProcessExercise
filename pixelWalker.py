

def pixelWalker(v1, v2):
    if len(v1) != len(v2):
        return "different length error"
    
    product = 0
    for i in range(len(v1)):
        product += (v1[i] * v2[i])
        
    return product
    
    
if __name__ == "__main__":
    
    # Standard Case: Simple integers or floats
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    # Expected Output: 32 (1*4 + 2*5 + 3*6)

    # Tricky Case: Embeddings (Floats)
    embed_a = [0.1, 0.5, 0.2]
    embed_b = [0.9, 0.4, 0.1]
    # Expected Output: 0.31 (0.09 + 0.2 + 0.02)

    # Edge Case: Different lengths (Should raise error or return 0 depending on logic)
    v3 = [1, 2]
    v4 = [1, 2, 3] 
    # Your code should verify lengths match!
    
    
    
    result = pixelWalker(v3, v4)
    print(result)