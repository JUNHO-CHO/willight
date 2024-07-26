class Node:           #클래스 노드 정의
    def __init__(self, data):          # 데이터 노드 생성
        self.data = data  # 노드가 저장할 데이터
        self.next = None  # 다음 노드를 가리키는 참조, 초기값은 None


class LinkedList:   #연결리스트 클래스 정의
    def __init__(self):
        self.head = None  # 리스트의 첫 노드를 가리키는 헤드

    def append(self, data):
        """리스트의 끝에 새 노드를 추가"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        """리스트의 모든 요소를 출력"""
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

    def prepend(self, data):
        """리스트의 시작 부분에 노드를 추가"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        """키에 해당하는 노드를 찾아 삭제"""
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return  # 키에 해당하는 노드가 없는 경우

        prev_node.next = current_node.next
        current_node = None