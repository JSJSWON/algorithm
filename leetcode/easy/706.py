from collections import defaultdict


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


# 개별 체이닝 방식을 이용한 해시 테이블 구현
class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        # key를 hash 값으로
        index = key % self.size # 단순하게 size의 개수만큼 modulo 연산을 한 나머지를 해시값으로 정함

        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            # defaultdict는 존재하지 않는 index로 조회할 경우 에러를 발생하지 않고 바로 디폴트 객체를 생성
            # 그렇기 때문에 if문의 조건을 self.table[index] is None으로 하면 안됨
            self.table[index] = ListNode(key, value)
            return

        # 인덱스에 노드가 있다면 연결 리스트 처리
        p = self.table[index]
        while p:
            # key가 동일한 쌍이 들어온다면 key에 대한 value가 바뀌고 끝
            # 예를 들어 a[1] = 100인데 a[1] = 50이라고 하면 value가 바뀜
            if p.key == key:
                p.value = value
                return

            # p를 연결 리스트의 끝까지 이동 후 while문 밖에서 노드 추가
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        p = self.table[index]
        # 제일 처음 값이 지울 값일 때
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        prev = p  # 여기서 처음에는 prev와 p가 같다. 바로 위 코드(제일 처음 값이 지울 값일 때)가 없다면 이상한게 맞음
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next  # 두 번째부터 prev와 p가 달라짐
