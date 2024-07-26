# ----- 코드 정의 ------
class Member:                                                          # 클래스를 이용하여 맴버를 설정
    def __init__(self, name, username, password):                      # name,username,password를
        self.name = name                                               # name의 객체는 name
        self.username = username                                       # username의 객체는 username
        self.password = password                                       # password의 객체는 password 생성한다.
    def display(self):                                                 # 객체의 정보를
        print(f"Name:{self.name}  ID:{self.username}")                 # F-str 을 이용하여 "name: name" "ID:username"으로
                                                                       # 생성한다

class Post:                                                            # 클래스를 이용하여 post를 설정
    def __init__(self, title, content, author):                        # title, content, author를
        self.title = title                                             # title의 객체는 title로
        self.content = content                                         # content의 객체는 content로
        self.author = author                                          # author의 객체는 author로 생성한다.

    def __repr__(self):
        return f"{self.title} - {self.content}"

# ----- 코드 실행 ------
members = []                                                             # 멤버리스트
member1 = Member('조씨', 'cho', 'cho123')          # 멤버1에 멤버정보를 name:조씨 username:cho password: cho123
members.append(member1)                                                  # 멤버 리스트에 각 멤버 123을 출력할 수 있도록

member2 = Member('이씨', 'lee', 'lee123')          #멤버 1이라는 멤버클래스의 인스턴스를
members.append(member2)                                                  #멤버스 리스트에 추가한다.

member3 = Member('김씨', 'kim', 'kim123')          #
members.append(member3)                                                  #

for member in members:
    member.display()


posts = []

post1 = Post('이무진', '청혼하지 않을 이유를 못찾았어', 'member1.name')
posts.append(post1)
post2 = Post('다이나믹듀오', '고백', 'member1.name')
posts.append(post2)
post3 = Post('livingston', 'shadow', 'member1.name')
posts.append(post3)

post4 = Post('livingston', 'architect', 'member2.name')
posts.append(post4)
post5 = Post('livingston','neon', 'member2.name')
posts.append(post5)
post6 = Post('benson boone','beautifil things', 'member2.name')
posts.append(post6)

post7 = Post('christopher', 'bad', 'member3.name')
posts.append(post7)
post8 = Post('bruno mars','when i was your man', 'member3.name')
posts.append(post8)
post9 = Post('charlie puth','dangerously', 'member3.name')
posts.append(post9)

print(posts)

for post in posts:
    if post.author == member1.name:
        print(f"Title: {post.title}, Content: {post.content}, Author: {post.author.name}")




