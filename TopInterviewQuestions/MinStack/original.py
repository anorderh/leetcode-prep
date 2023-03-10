class MinStack:
    # Tuple implementation
    def __init__(self):
        self.values = []

    def push(self, val: int) -> None:
        if not self.values: # If empty, min is own value
            self.values.append((val, val))
        else:   # Not empty, min is previous element's min
            min_val = self.values[-1][1]
            self.values.append((val, min(val, min_val))) # Compare val & min
        
    def pop(self) -> None:
        self.values = self.values[:-1]

    def top(self) -> int:
        return self.values[-1][0]
        
    def getMin(self) -> int:
        return self.values[-1][1]
