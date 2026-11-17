# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

   

  Markdown
# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment used Python dictionaries to demonstrate hash table behavior through a restaurant reservation lookup system.

## Learning Objectives

- Inserted key-value pairs into a hash table structure
- Retrieved values efficiently using key hashing
- Updated existing values in place
- Removed entries while maintaining hash table integrity
- Handled edge cases and analyzed hashing concepts

## Implementation Summary (Past Tense)

1. **Created and Populated a Dictionary:** Initialized an empty Python dictionary (`reservations`) and inserted five guest reservation records mapping guest names (keys) to table assignments and booking times (values).
2. **Demonstrated Lookup Operations:** Retrieved specific reservation details using direct key indexing, demonstrating $O(1)$ average-case access time.
3. **Demonstrated Update Operations:** Modified an existing guest's reservation details by assigning a new value to an existing key, overwriting the previous value without creating duplicate keys.
4. **Demonstrated Delete Operations:** Removed a canceled reservation using `.pop()` and displayed the table state and item count before and after removal.
5. **Tested Edge Cases:** Verified safe handling of missing key lookups using `.get()`, safe deletion attempts on non-existent keys using `.pop()` with a fallback value, and operations on an empty dictionary without triggering `KeyError` exceptions.
6. **Created a Real-World Scenario:** Modeled a peak-hour restaurant host stand reservation system to illustrate fast key-value storage, updates, cancellations, and error handling.