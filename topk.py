import collections
import re

def get_top_k_words(sentences, k=3):
    # Edge case: Empty input
    if not sentences:
        return []
    
    print(sentences)

    # 1. Initialize a Counter (Hash Map optimized for counting)
    word_counts = collections.Counter()
    
    for sentence in sentences:
        # 2. Normalize: Convert to lowercase
        sentence = sentence.lower()
        
        
        print(sentence)
        
        # 3. Clean: Remove non-alphanumeric characters using Regex
        # r'[^a-z0-9\s]' means "replace anything that IS NOT a letter, number, or space with nothing"
        clean_sentence = re.sub(r'[^a-z0-9\s]', '', sentence)
        
        # 4. Tokenize: Split by whitespace into a list of words
        tokens = clean_sentence.split()
        
        print("token", tokens)
        
        # 5. Update the running count
        word_counts.update(tokens)
        
        
        print(word_counts)
        
    # 6. Return the top k most common elements
    return word_counts.most_common(k)



if __name__ == "__main__":
    test_sentences = [
        "Hello world!",
        "Hello Python world.",
        "Python is great."
    ]
    result = get_top_k_words(test_sentences, k=3)
    print("\nTop 3 words:")
    print(result)