"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # Create an empty dictionary to model a restaurant reservation hash table.
    # Python dictionaries are implemented under the hood as open-addressed hash tables.
    # When a key-value pair is inserted, Python runs the immutable key through a built-in
    # hash() function to compute a numeric hash code, maps that hash to an internal bucket
    # index, and stores the key-value pair directly at that memory slot in O(1) average time.
    reservations = {}

    # Insert 5 guest reservation records (Key: Guest Name, Value: Reservation Details)
    reservations["Alice Johnson"] = "Table 4 - Party of 2 at 6:30 PM"
    reservations["Marcus Vance"] = "Table 12 - Party of 6 at 7:00 PM"
    reservations["Priya Patel"] = "Booth 2 - Party of 4 at 7:15 PM"
    reservations["David Kim"] = "Table 8 - Party of 2 at 7:30 PM"
    reservations["Elena Rostova"] = "Patio 3 - Party of 5 at 8:00 PM"

    print("Initial Restaurant Reservation Hash Table (5 entries added):")
    for guest, details in reservations.items():
        print(f"  {guest}: {details}")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # When looking up a key, Python hashes the search key again to jump directly
    # to its calculated bucket index instead of scanning entries one by one.
    # This gives hash tables O(1) average-case lookup performance regardless of table size.
    guest_one = "Priya Patel"
    guest_two = "David Kim"

    print(f"Lookup '{guest_one}': {reservations[guest_one]}")
    print(f"Lookup '{guest_two}': {reservations[guest_two]}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    # Because hash table keys must be unique, assigning a new value to an existing key
    # hashes the key to find its existing bucket and overwrites the stored value in place
    # without creating a duplicate key entry.
    print("Before Update (Alice Johnson):", reservations["Alice Johnson"])

    reservations["Alice Johnson"] = "Table 6 - Party of 4 at 6:45 PM (Updated)"

    print("After Update (Alice Johnson): ", reservations["Alice Johnson"])
    print("\nCurrent Reservation Table after update:")
    for guest, details in reservations.items():
        print(f"  {guest}: {details}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    # Deleting a key hashes the target key to locate its bucket in O(1) average time
    # and removes the key-value mapping. Internally, Python leaves a dummy/tombstone marker
    # in the slot so open-addressing probe sequences for other collided keys remain intact.
    print(f"Reservation count before cancellation: {len(reservations)}")
    print("Removing 'Marcus Vance' (Reservation Cancelled)...")

    removed_booking = reservations.pop("Marcus Vance")
    print(f"Removed entry -> Marcus Vance: {removed_booking}")

    print(f"\nReservation count after cancellation: {len(reservations)}")
    for guest, details in reservations.items():
        print(f"  {guest}: {details}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1: Looking up a non-existent key safely.
    # Standard bracket indexing (reservations["Missing"]) raises a KeyError when a key
    # is not found in the table. Using .get() hashes the key, sees no match at the bucket,
    # and safely returns a fallback default message without crashing the program.
    missing_guest = "Jordan Taylor"
    lookup_result = reservations.get(missing_guest, "No reservation found under this name.")
    print(f"Edge Case 1 - Safe lookup for '{missing_guest}': {lookup_result}")

    # Edge Case 2: Deleting a missing key safely.
    # Using 'del reservations[key]' on a missing key raises a KeyError. Passing a default
    # value to .pop(key, default) checks for the key and returns the fallback message
    # safely if the key does not exist in the hash table.
    safe_delete = reservations.pop("NonExistent Guest", "Cannot delete: Key does not exist.")
    print(f"Edge Case 2 - Safe delete for 'NonExistent Guest': {safe_delete}")

    # Edge Case 3: Performing operations on an empty dictionary.
    # An empty dictionary has allocated initial bucket space with zero active entries.
    # Checking membership ('in') or calling .get() executes in O(1) time and safely
    # reports that the key is absent.
    empty_table = {}
    print(f"Edge Case 3 - Empty dictionary length: {len(empty_table)} | Lookup result: {empty_table.get('Guest', 'Table is empty')}")


if __name__ == "__main__":
    main()