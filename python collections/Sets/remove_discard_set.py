a={1, 2, 3, 4, 5}
a.remove(3)
print("After remove(3):",a)
a.discard(5)
print("After discard(5):",a)
a.discard(10)
print("After discard(10):",a)
#output:
After remove(3): {1, 2, 4, 5}
After discard(5): {1, 2, 4}
After discard(10): {1, 2, 4}

