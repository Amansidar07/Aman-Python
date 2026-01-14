from collections import defaultdict

def predictive_lru(pages, capacity):
    frames = []
    page_faults = 0
    transition_count = defaultdict(lambda: defaultdict(int))

    prev_page = None

    def predict_next(page):
        if page not in transition_count:
            return None
        return max(transition_count[page], key=transition_count[page].get)

    for page in pages:
        # Update transition history
        if prev_page is not None:
            transition_count[prev_page][page] += 1

        prediction = predict_next(prev_page)

        if page not in frames:
            page_faults += 1
            if len(frames) == capacity:
                # Eviction logic
                for p in frames:
                    if p != prediction:
                        frames.remove(p)
                        break
            frames.append(page)
        else:
            frames.remove(page)
            frames.append(page)  # Move to most recent

        print(f"Page: {page}, Prediction: {prediction}, Frames: {frames}")
        prev_page = page

    print("Total Page Faults (Predictive LRU):", page_faults)


# Example
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
capacity = 3
predictive_lru(pages, capacity)
