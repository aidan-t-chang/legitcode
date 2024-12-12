# Given two positive integers n and k, the binary string Sn is formed as follows:

# S1 = "0"
# Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
# Where + denotes the concatenation operation, reverse(x) returns the reversed string x,
# and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

# For example, the first four strings in the above sequence are:

# S1 = "0"
# S2 = "011"
# S3 = "0111001"
# S4 = "011100110110001"
# Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        sequence = "0"

        # Generate sequence until we have enough elements or reach nth iteration
        for i in range(1, n):
            if k <= len(sequence):
                break
            sequence += "1"

            # Append the inverted and reversed part of the existing sequence
            inverted = "".join(
                "1" if bit == "0" else "0" for bit in sequence[:-1]
            )
            sequence += inverted[::-1]

        # Return the kth bit
        return sequence[k - 1]