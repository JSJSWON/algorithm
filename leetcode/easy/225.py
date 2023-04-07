from collections import deque


# queue(선입선출)를 이용한 stack(후입선출) 구현
# 1, 2가 들어갔으면 1이 먼저 나옴 -> stack은 2가 나와야 함 -> 이를 위해 push한 뒤 배열 순서를 뒤집음
class MyStack:
    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        for _ in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())

    def pop(self) -> int:
        return self.stack.popleft() # 선입선출

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0
