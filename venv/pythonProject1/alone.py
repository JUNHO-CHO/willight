# - 클래스 : 클래스는 인스턴스의 설계도나 템플릿입니다. 객체의 속성(어트리뷰트)과 행위(메소드)를 정의하는 틀입니다. 예를 들어, 자동차 클래스는 자동차의 속성(색상, 모델 등)과 행위(가속, 정지 등)를 정의합니다.
# - 인스턴스 : 클래스의 정의를 기반으로 실제로 생성된 객체를 인스턴스라고 합니다
# - 메소드 : 클래스 함수라고도 합니다. 클래스 내에서 지정된 함수입니다. 자동차 클래스의 "가속"이나 "정지"와 같은 작업이 메소드의 예시입니다.
# - 어트리뷰트 : 클래스 변수라고도 합니다. 클래스 내에서 변수를 지정할때 사용합니다.  자동차 클래스에서 "색상"이나 "모델"과 같은 특징이 어트리뷰트의 예시입니다.

# 1. **`Member`** 클래스와 **`Post`** 클래스를 정의하세요.
# 2. **`Member`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
#     - 회원 이름 (**`name`**)------------------------------------완료
#     - 회원 아이디 (**`username`**)------------------------------------완료
#     - 회원 비밀번호 (**`password`**)  ------------------------------------완료
# 3. **`Member`** 클래스에는 다음과 같은 메소드를 가지고 있어야 합니다.
#     - 회원 정보를 print해주는 `display` (회원이름과 아이디만 보여주고 비밀번호는 보여줘서는 안됩니다!) -------------완료
# 4. **`Post`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
#     - 게시물 제목 (**`title`**) -----------------------완료
#     - 게시물 내용 (**`content`**)-----------------------완료
#     - 작성자 (**`author`**) : 회원의 `username` 이 저장되어야 함! -----------------------완료
# 5. 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요
#     1. members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요                -----------------------완료????
# 6. 각각의 회원이 게시글을 세개 이상 작성하는 코드를 만들어주세요.(회원이 세명이명 총 9개 이상의 post 인스턴스가 만들어져야 합니다).
#     만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장해주세요
#     1. for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
#     2. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요

# ----- 코드 정의 ------
class Member:            #클래스 맴버 정의
    def __init__(self, name, username, password):   #매직메서드를 이용하여 name, username, password의 인스턴스 설정
        self.name = name                            #객체 name은 name
        self.username = username                    #객체 username은 username
        self.password = password                    #객체 password는 password
    def display(self):                             #display를 이용하여 회원 정보 출력(단 패스워드는 안나오게 출력)
        print(f'Name:{self.name}, ID:{self.username}')   #프린트를 username 까지만 출력)
    def __repr__(self):                            #문자열 객체출력
        return f'{self.name}, {self.username}'     # name,username 객체 값 반환
def display_members():  # 함수 추가
    for member in members:
        member.display()  # display 메소드 호출1


class Post():                                      # post 클래스 정의
    def __init__(self, title, content, author):    # 매직메서드를 통하여 title,content, author 인스턴스를 설정
        self.title = title                         # title은 title
        self.content = content                     # content 는 content
        self.author = author                       # author는 author로 
    def display(self):
        print(f'Title:{self.title}, Content:{self.content}, Author:{self.author}')


    def __repr__(self):
        return f'{self.title},{self.content},{self.author}'

def create_member():
    print("새로운 회원 등록")
    name = input("이름 입력 :")
    username = input("아이디 입력:")
    password = input("비밀번호 입력 :")

    new_member = Member(name, username, password)
    members.append(new_member)

def create_post(posts):  # 함수 추가
    # 특정유저가 작성한 게시글의 제목을 모두 프린트 / # 특정 단어가 content에 포함된 게시글의 제목을 모두 프린트
    for post in posts:
        if post.author.name == '조준호':
            print(post.title)

    keyword = "특정단어"  # keyword 란 변수 선언
    # for in / if in 으로 post.content 에 keyword("특정 단어")가 들어가 있는 것만 반복문으로 출력
    for post in posts:
        if keyword in post.content:
            print(post.title)
def create_content():
    print("새로운 게시글 작성")
    title = input("제목 입력 :")
    content = input("내용 입력 :")
    username = input("작성자명 입력 :")

    new_content = Post(title, content, m1)
    posts.append(new_content)


# ----- 코드 실행 ------
members = []                                                         #멤버리스트 설정
m1 = Member('조준호', 'chojunho', 'a123')    #멤버 1을 호출할 경우 나타낼 멤버의 인스턴스설정
m2 = Member('조준', 'chojun', 'a1234')
m3 = Member('조', 'cho', 'a12345')
members.append(m1)                                                  #members 리스트에 멤버1 추가 아래 추가된 것들도 같음.
members.append(m2)
members.append(m3)

print(members)

posts = []                                              # post 리스트 설정
p1 = Post('제목1', '단어', m1)                           # 멤버 리스트와 같음.
p2 = Post('제목2', '단어', m2)
p3 = Post('제목3', '특정 단어', m3)                      #각 post는 제목, 단어, members의 인스턴스를 가짐
posts.append(p1)
posts.append(p2)
posts.append(p3)

post4 = Post('제목4', '단어', m1)
post5 = Post('제목5', '단어', m2)
post6 = Post('제목6', '특정 단어', m3)
posts.append(post4)
posts.append(post5)
posts.append(post6)

post7 = Post('제목7', '단어', m1)
post8 = Post('제목8', '단어', m2)
post9 = Post('제목9', '특정 단어', m3)
posts.append(post7)
posts.append(post8)
posts.append(post9)

create_member()
create_content()
display_members()
create_post(posts)