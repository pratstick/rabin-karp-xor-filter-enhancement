def rabin_karp_xor_search(pattern, text):
    """
    Enhanced Rabin-Karp algorithm using XOR filter.
    Returns a list of starting indices where pattern is found in text.
    """
    if not pattern or not text or len(pattern) > len(text):
        return []

    m, n = len(pattern), len(text)
    base = 256  # Number of possible characters
    prime = 101  # A prime number for modulo

    # Precompute pattern hash and XOR
    pattern_hash = 0
    pattern_xor = 0
    for c in pattern:
        pattern_hash = (base * pattern_hash + ord(c)) % prime
        pattern_xor ^= ord(c)

    # Initial window hash and XOR
    window_hash = 0
    window_xor = 0
    for i in range(m):
        window_hash = (base * window_hash + ord(text[i])) % prime
        window_xor ^= ord(text[i])

    # Precompute base^(m-1) % prime for rolling hash
    h = 1
    for _ in range(m - 1):
        h = (h * base) % prime

    result = []
    for i in range(n - m + 1):
        # Check hash and XOR
        if window_hash == pattern_hash and window_xor == pattern_xor:
            if text[i:i + m] == pattern:
                result.append(i)
        if i < n - m:
            # Update hash: remove leading char, add trailing char
            window_hash = (window_hash - ord(text[i]) * h) % prime
            window_hash = (window_hash * base + ord(text[i + m])) % prime
            window_hash = (window_hash + prime) % prime  # Ensure positive
            # Update XOR: remove leading char, add trailing char
            window_xor ^= ord(text[i])
            window_xor ^= ord(text[i + m])
    return result

# Example usage:
if __name__ == "__main__":
    text = "ababcabcabababd"
    pattern = "ababd"
    print(rabin_karp_xor_search(pattern, text))
