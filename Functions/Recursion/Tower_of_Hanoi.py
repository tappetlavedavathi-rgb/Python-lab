def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    # Move the largest disk to destination
    print("Move disk", n, "from", source, "to", destination)
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)
# For n = 3
print("Tower of Hanoi for 3 disks:")
tower_of_hanoi(3, "A", "B", "C")
print("\nTotal moves for 3 disks:", 2**3 - 1)
# For n = 4
print("\nTower of Hanoi for 4 disks:")
tower_of_hanoi(4, "A", "B", "C")
print("\nTotal moves for 4 disks:", 2**4 - 1)
#output:
Tower of Hanoi for 3 disks:
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C

Total moves for 3 disks: 7

Tower of Hanoi for 4 disks:
Move disk 1 from A to B
Move disk 2 from A to C
Move disk 1 from B to C
Move disk 3 from A to B
Move disk 1 from C to A
Move disk 2 from C to B
Move disk 1 from A to B
Move disk 4 from A to C
Move disk 1 from B to C
Move disk 2 from B to A
Move disk 1 from C to A
Move disk 3 from B to C
Move disk 1 from A to B
Move disk 2 from A to C
Move disk 1 from B to C

Total moves for 4 disks: 15

