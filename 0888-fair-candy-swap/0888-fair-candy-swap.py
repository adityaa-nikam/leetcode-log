class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)
        difference = (alice_total - bob_total) // 2
        bob_set = set(bobSizes)
        for alice_box in aliceSizes:
            bob_box = alice_box - difference
            if bob_box in bob_set:
                return [alice_box, bob_box]