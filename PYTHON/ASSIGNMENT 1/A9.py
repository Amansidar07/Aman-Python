
pages = [7, 0, 1, 2, 0, 3, 0, 4]
capacity = 3

def fifo_page_replacement(pages, capacity):
    frames = []
    page_faults = 0
    for page in pages:
        if page not in frames:
            page_faults += 1
            if len(frames) == capacity:
                frames.pop(0)   # Remove oldest page
            frames.append(page)
        print(f"Page: {page} -> Frames: {frames}")

    print("Total Page Faults (FIFO):", page_faults)
# Example
fifo_page_replacement(pages, capacity)

def lru_page_replacement(pages, capacity):
    frames = []
    page_faults = 0
    for page in pages:
        if page not in frames:
            page_faults += 1
            if len(frames) == capacity:
                frames.pop(0)   # Remove LRU page
        else:
            frames.remove(page)  # Move page to recent position

        frames.append(page)
        print(f"Page: {page} -> Frames: {frames}")

    print("Total Page Faults (LRU):", page_faults)

# Example
lru_page_replacement(pages, capacity)