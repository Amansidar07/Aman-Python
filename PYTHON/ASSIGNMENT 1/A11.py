# Memory Allocation Simulation
# First Fit, Best Fit, Worst Fit

def first_fit(blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break

    return allocation


def best_fit(blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        best_idx = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if best_idx == -1 or blocks[j] < blocks[best_idx]:
                    best_idx = j

        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx] -= processes[i]

    return allocation


def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        worst_idx = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if worst_idx == -1 or blocks[j] > blocks[worst_idx]:
                    worst_idx = j

        if worst_idx != -1:
            allocation[i] = worst_idx
            blocks[worst_idx] -= processes[i]

    return allocation


# -------- Main Program --------
memory_blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

print("Memory Blocks:", memory_blocks)
print("Processes:", processes)

print("\nFirst Fit Allocation:")
print(first_fit(memory_blocks.copy(), processes))

print("\nBest Fit Allocation:")
print(best_fit(memory_blocks.copy(), processes))

print("\nWorst Fit Allocation:")
print(worst_fit(memory_blocks.copy(), processes))
