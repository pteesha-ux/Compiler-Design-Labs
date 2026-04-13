# Stack Storage Allocation Strategy Simulation

class StackAllocator:

    def __init__(self):
        self.stack = []
        self.address = 1000  # Starting memory address
        self.memory_map = {}

    def allocate(self, variable):
        self.memory_map[variable] = self.address
        self.stack.append(variable)

        print(f"Allocated '{variable}' at address {self.address}")

        self.address += 4  # assuming 4 bytes per variable

    def deallocate(self):
        if self.stack:
            variable = self.stack.pop()
            address = self.memory_map.pop(variable)

            print(f"Deallocated '{variable}' from address {address}")

            self.address -= 4
        else:
            print("Stack Underflow")

    def display_stack(self):
        print("\nCurrent Stack:")
        print(self.stack)


allocator = StackAllocator()

allocator.allocate("a")
allocator.allocate("b")
allocator.allocate("c")

allocator.display_stack()

allocator.deallocate()

allocator.display_stack()
