import sys
import pygame

# 파이게임 초기화
pygame.init()

# 시작 배경
background = pygame.image.load("main.jpg")

# 시계
clock = pygame.time.Clock()

# 화면 만들기
screen_width = 1070
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("근로계약서를 완성하자!")

# 폰트, 이미지 등 요소 설정
# 폰트
font = pygame.font.SysFont("malgungothic", 20)
titleFont = pygame.font.SysFont("malgungothic", 30)
# 색상
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
beige = (255, 249, 227)
deepbrown = (153, 134, 117)
lightbrown = (216, 198, 178)

# 이미지
yellowStar = pygame.image.load("yellowStar.png")
redStar = pygame.image.load("redStar.png")


# 스크린 이미지 설정

# 버튼 만드는 함수
def create_button(x, y, width, height, hovercolor, defaultcolor):
    pos = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pos()
    # Mouse get pressed can run without an integer, but needs a 3 or 5 to indicate how many buttons
    click = pygame.mouse.get_pressed(3)
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hovercolor, (x, y, width, height))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, defaultcolor, (x, y, width, height))


def create_star_button(x, y, image1, image2):
    mouse = pygame.mouse.get_pos()
    # Mouse get pressed can run without an integer, but needs a 3 or 5 to indicate how many buttons
    click = pygame.mouse.get_pressed(3)
    if x + 30 > mouse[0] > x and y + 30 > mouse[1] > y:
        screen.blit(image2, (x, y))
        if click[0] == 1:
            return True
    else:
        screen.blit(image1, (x, y))


def intro():

    start_text = font.render("대학생 1학년 일명 새내기인 주인공", True, black)
    text2 = font.render("인생 첫 알바 출근을 가게 되었다.", True, black)
    text3 = font.render("하지만 첫 알바인 만큼 모르는 부분도 많고,", True, black)
    text4 = font.render("무언가 손해를 보는 느낌도 있지만 부당한 상황인지 인지하지 못하고 있는데 ,, ", True, black)
    text5 = font.render("이 게임을 플레이하는 당신은 주인공이 되어 ", True, black)
    text6 = font.render("부당한 사례를 해쳐 나가는 알바생 역할을 해야합니다! ", True, black)
    text7 = font.render("게임을 플레이 하시겠습니까?", True, deepbrown)

    while True:
        bg = pygame.image.load("첫화면.jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(start_text, ((screen_width - start_text.get_width()) / 2, 2000))
        screen.blit(text2, (((screen_width - start_text.get_width()) / 2), 240))
        screen.blit(text3, (((screen_width - start_text.get_width()) / 2) - 30, 280))
        screen.blit(text4, (((screen_width - start_text.get_width()) / 2) - 140, 320))
        screen.blit(text5, (((screen_width - start_text.get_width()) / 2) - 20, 360))
        screen.blit(text6, (((screen_width - start_text.get_width()) / 2) - 70, 400))
        screen.blit(text7, (((screen_width - start_text.get_width()) / 2) + 20, 500))

        start_button = create_button(((screen_width - start_text.get_width()) / 2) + 20, 630, 120, 40, deepbrown, lightbrown)
        quit_button = create_button(((screen_width - start_text.get_width()) / 2) + 170, 630, 120, 40, deepbrown, lightbrown)

        startbuttontext = titleFont.render("Yes", True, white)
        screen.blit(startbuttontext, (((screen_width - start_text.get_width()) / 2) + 50, 630))

        quitbuttontext = titleFont.render("no", True, white)
        screen.blit(quitbuttontext, (((screen_width - start_text.get_width()) / 2) + 200, 630))

        if start_button:  # True라면, 즉 클릭했다면
            screen01()

        if quit_button:
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # x누르면 종료함
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)  # fps 15로 설정



def screen01():
    start_text = font.render("<알바생>", True, black)
    text1 = font.render("아싸 카페알바 경력도 없는데 한번에 뽑혔다!", True, black)
    text2 = font.render("사장도 완전 멀쩡해 보이고 카페도 마음에 들었는데...!", True, black)
    text3 = font.render("대박이다!", True, black)

    while True:
        bg = pygame.image.load("길거리사진.jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(start_text, (70, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))
        screen.blit(text3, (80, 620))

        next_button_2 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        nextbuttontext = titleFont.render("다음", True, white)
        screen.blit(nextbuttontext, (830, 630))

        if next_button_2:  # True라면, 즉 클릭했다면
            screen02()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen02():
    text4 = font.render("새내기가 되어서 하고싶은 것도, 사고싶은 것도 많아져 알바를 하기로 결심했는데", True, black)
    text5 = font.render("며칠만에 카페알바 붙다니.. 첫 출근인 만큼 힘내자!!", True, black)

    while True:
        bg = pygame.image.load("길거리사진.jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text4, (80, 500))
        screen.blit(text5, (80, 540))

        next_button = create_button(((screen_width - text4.get_width()) / 2) + 500, 600, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text4.get_width()) / 2) + 530, 600))

        if next_button:  # True 라면, 즉 클릭했다면
            name_input()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def name_input():
    startText = font.render(" ", True, deepbrown)
    newUserName = ""
    nameActive = False

    startYourDay = font.render("GAME START", True, deepbrown)

    while True:
        bg = pygame.image.load("근로계약서_이름.jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기

        #start name
        screen.blit(startText, ((screen_width - startText.get_width()) / 2, 110))

        # create the text box
        userNameSurface = font.render(newUserName, True, black)
        userNameBorder = pygame.Rect(((screen_width - userNameSurface.get_width()) / 2) - 10, (screen_height * .20)+280,
                                     userNameSurface.get_width() + 10, 50)

        # UserNameSurface 텍스트 화면에 나타냄
        screen.blit(userNameSurface, ((screen_width - userNameSurface.get_width()) / 2, (screen_height * .20)+280))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Mouse and Keyboard events
            if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 버튼을 눌렀을 때
                if userNameBorder.collidepoint(event.pos):  # ??
                    nameActive = True  # 색상을 흰색으로 바꾸고, 아래에 있는 KEYDOWN에 활용
                else:
                    nameActive = False

            if event.type == pygame.KEYDOWN:
                if nameActive:  # 이전에 마우스로 사각형을 눌러서 활성화 됐을 경우
                    if event.key == pygame.K_BACKSPACE:  # 백스페이스를 누르면
                        newUserName = newUserName[:-1]  # 맨 뒤 한글자씩 삭제
                    else:
                        newUserName += event.unicode  # 키보드로 누른 문자를 newUserName에 추가한다.

        # Handles the click events by swtiching from white, slategrey, and black
        if nameActive:  # True 라면 : userNameBorder 를 마우스로 클릭하여 nameActive를 활성화 시킨 경우
            pygame.draw.rect(screen, beige, userNameBorder)
            userNamePrompt = font.render("Enter your first and last name here", True, deepbrown)
        else:  # False라면
            pygame.draw.rect(screen, deepbrown, userNameBorder)
            userNamePrompt = font.render("Enter your first and last name here", True, deepbrown)

        # "Enter your first and last name here" 이라는 문구를 띄움
        screen.blit(userNamePrompt, ((screen_width - userNamePrompt.get_width()) / 2,
                                     (screen_height * .20) + userNameSurface.get_height() + 100))  # 문구 높이

        screen.blit(userNameSurface,
                    ((screen_width - userNameSurface.get_width()) / 2, (screen_height * .20) + 285))  # 이름 입력 높이
        # 게임 시작 버튼을 만듬
        submitButtton = create_button((screen_width / 2) - (startYourDay.get_width() / 2) - 5, screen_height * .9,
                                      startYourDay.get_width() + 10, startYourDay.get_height(), green, beige)

        screen.blit(startYourDay, ((screen_width / 2) - (startYourDay.get_width() / 2), int(screen_height * .9)))

        if submitButtton:  # StartYourDay 버튼 클릭했다면
            if newUserName != "":  # 이름을 입력하였다면
                screen3(newUserName)
            else:
                warning = font.render("Please write your name", True, deepbrown)
                pygame.draw.rect(screen, black, [0, screen_height / 2, screen_width, 70])
                screen.blit(warning, ((screen_width - warning.get_width()) / 2, screen_height / 2))

        pygame.display.update()
        clock.tick(15)


def screen3(newUserName):
    start_text = font.render("<사장>", True, black)
    text1 = font.render(newUserName + "씨, 앞치마랑 모자 준비해 뒀으니까 복장 갖춰서 나와~", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(사장+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(start_text, (70, 500))
        screen.blit(text1, (80, 540))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen4()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen4():
    text1 = font.render("<알바생>", True, black)
    text2 = font.render("(오 바로 일을 시작하네 ..?) 네 얼른 준비해서 나오겠습니다!!", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(알바생+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text1, (80, 500))
        screen.blit(text2, (80, 540))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 300, 600, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 330, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            cafe_map_1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def cafe_map_1():  # 스크린4와 5사이
    k = 0

    while True:
        cafeMap = pygame.image.load("배경_평면도.jpg")
        screen.blit(cafeMap, (0, 0))  # 배경 그리기
        star1 = pygame.image.load("yellowStar.png")
        star2 = pygame.image.load("yellowStar.png")
        k += 1

        if (k % 13 == 0) or (k % 13 == 1) or (k % 13 == 2):
            screen.blit(star1, (655, 120))
            screen.blit(star2, (800, 450))
            nextStarButton = create_star_button(500, 450, yellowStar, redStar)
            if nextStarButton:
                screen5()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                k = 0

        pygame.display.update()
        clock.tick(15)


def screen5():
    text = font.render("<알바생> ", True, black)
    text1 = font.render("알바생 : 와, 여기는 유니폼도 이쁘네 ..", True, black)
    text2 = font.render("모자도 이쁘고, 앞치마도 이쁘고…  엥, 이게.. 뭐야?", True, black)
    text3 = font.render("(락커 안에 의문의 쪽지가 들어있다.)", True, black)

    while True:
        bg = pygame.image.load("배경_락커실+대화창.jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))
        screen.blit(text3, (80, 620))

        next_button = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button:  # True 라면, 즉 클릭했다면
            locker()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def locker():
    k = 0

    while True:
        bg = pygame.image.load("배경_락커실.jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        star1 = pygame.image.load("yellowStar.png")
        k += 1

        if (k % 13 == 0) or (k % 13 == 1) or (k % 13 == 2):
            screen.blit(star1, (640, 550))
            nextStarButton = create_star_button(640, 550, yellowStar, redStar)
            if nextStarButton:
                locker2()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                k = 0

        pygame.display.update()
        clock.tick(15)


def locker2():
    while True:
        bg = pygame.image.load("단서_쪽지(배경,문구).jpg")
        screen.blit(bg, (0, 0))

        next_button_2 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        nextbuttontext = titleFont.render("다음", True, white)
        screen.blit(nextbuttontext, (830, 630))

        if next_button_2:  # True라면, 즉 클릭했다면
            locker3()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def locker3():
    start_text = font.render("<알바생>", True, black)
    text1 = font.render("...응?? 이게 무슨 소리야…?", True, black)
    text2 = font.render("아니 근데 대머리라니 말이 심하네~ 괜히 심란하게 이런 걸 왜 넣어놓는 거야...버려야겠다", True, black)

    while True:
        bg = pygame.image.load("단서_쪽지(배경,문구+대화창).jpg")
        screen.blit(bg, (0, 0))
        screen.blit(start_text, (70, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))

        next_button = create_button(((screen_width - text1.get_width()) / 2) + 300, 600, 120, 40, deepbrown, lightbrown)
        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 330, 600))

        if next_button:  # True라면, 즉 클릭했다면
            screen7_1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen7_1():
    text = font.render("<사장> ", True, black)
    text1 = font.render("알바생~ 준비 다했어??", True, black)
    text2 = font.render("<알바생>", True, black)
    text3 = font.render(" 네네!! 갑니다!! ", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(사장+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))
        screen.blit(text3, (80, 620))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen7_2()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen7_2():
    text = font.render("<알바생>", True, black)
    text1 = font.render(" 이상한 쪽지를 발견했지만 이런 것 때문에 내 첫 알바를 망칠 순 없지... ", True, black)
    text2 = font.render(" 열심히 일해서 커피 알바 마스터가 되고 말겠어! ", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(알바생+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            screen8()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 근로 계약서 부분 코드입니다.


def screen8():
    text0 = font.render("<알바생>", True, black)
    text1 = font.render("사장님! 저 유니폼 다 갈아입었습니다!", True, black)
    text = font.render("<사장>", True, black)
    text2 = font.render("오 그래! 그럼 지금부터 해야 할 일들을 알려줄게. 일단 포스 보는 법부터 배우자~", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(사장+알바생+대화).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text0, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text, (80, 580))
        screen.blit(text2, (80, 620))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            screen9()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen9():
    text0 = font.render("<알바생>", True, black)
    text1 = font.render("(이게 포스기구나.. 복잡하네. 정신 똑바로 차려야겠다.. 진동벨은 여기 있고.. 근데 뭔가 허전한데..", True, black)
    text2 = font.render(" 아 맞다! 사장님, 저희 근로계약서는..? ", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(알바생+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text0, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen10()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen10():
    text = font.render("<사장> ", True, black)
    text1 = font.render("어? 아….그래..근로계약서.. 자세한 건 내가 채울 테니까 여기에 인적사항 적고 싸인해~ ", True, black)
    text2 = font.render("<알바생>", True, black)
    text3 = font.render("네! (하마터면 근로계약서를 못 받을 뻔 했잖아 ..? 휴, 다행이다!", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(사장+알바생+대화).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))
        screen.blit(text3, (80, 620))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            screen_work()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


# 이미지 -> 근로계약서로 전환

def screen_work():
    text1 = font.render("이 근로계약서는 조건 등이 정확히 명시되지 않은 근로계약서입니다.", True, black)
    text2 = font.render("노란 빈 칸들은 대화 중 알맞은 답변을 고르거나 퀴즈를 통해 단서를 획득하면 하나씩 채워집니다. ", True, black)

    while True:
        bg = pygame.image.load("근로계약서_1 (배경+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text1, (80, 500))
        screen.blit(text2, (80, 540))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen_work2()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen_work2():
    text1 = font.render("세 개의 빈칸을 모두 채우면 이 서류는 완벽하게 작성된 근로계약서가 되어 ", True, black)
    text2 = font.render("후에 부당한 대우를 당했을 때에 보상을 청구할 근거가 됩니다. ", True, black)
    text3 = font.render("단서들을 찾아 주인공을 도와주세요!", True, black)

    while True:
        bg = pygame.image.load("근로계약서_1 (배경+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text1, (80, 500))
        screen.blit(text2, (80, 540))
        screen.blit(text3, (80, 580))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True,white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            screen12_1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 최저 임금 부분 코드입니다.

def screen12_1():
    text1 = font.render("<사장> ", True, black)
    text2 = font.render(" 좋아~ 근데 알바 정직원이 아니고, 우리가 조금 써보고 나서 결정해야 하니까 ", True, black)
    text3 = font.render(" 일주일간 쓸만할지를 볼건데 이걸 수습기간이라고 해~ ", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(사장+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text1, (80, 500))
        screen.blit(text2, (80, 540))
        screen.blit(text3, (80, 580))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen12_2()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen12_2():
    text = font.render("<사장> ", True, black)
    text1 = font.render("수습기간 동안에는 정직원이 아니기 때문에! ", True, black)
    text2 = font.render("최저임금보다 조금, 아주 조금! 덜 받게 될거야. 알겠지??", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(사장+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            screen13()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen13():
    text = font.render("<알바생> ", True, black)
    text1 = font.render("아.. 수습기간은 최저임금보다 더 적은 임금을 받는건가요..?", True, black)
    text2 = font.render("<사장>", True, black)
    text3 = font.render("그럼. 아직 정직원이 아니니까~", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(사장+알바생+대화).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))
        screen.blit(text3, (80, 620))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            question_1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def question_1():
    while True:
        bg = pygame.image.load("배경_카운터(사장+알바생+대화).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기

        choice_button1 = create_button(100, 520, 540, 40, white, (226, 226, 226))
        choice_button1_text = font.render("1. 아, 그렇구나 …  수습기간은 최저임금보다 덜 받나보다.", True, black)
        screen.blit(choice_button1_text, (110, 520))

        choice_button2 = create_button(100, 570, 750, 40, white, (226, 226, 226))
        choice_button2_text = font.render("2. 말도안돼 ! 수습기간도 일하는 기간인데, 최저임금보다 적게 받는다니 이상해.", True, black)
        screen.blit(choice_button2_text, (110, 570))

        choice_button3 = create_button(100, 620, 520, 40, white, (226, 226, 226))
        choice_button3_text = font.render("3. 사장님 말투가 맘에 안드네. 한대 때릴까? <<< ? ^^b", True, black)
        screen.blit(choice_button3_text, (110, 620))

        if choice_button2:  # True 라면, 즉 클릭했다면
            answer_1()
        elif (choice_button1):
            warning = font.render("당신은 사장의 계략에 넘어갔습니다. 선택지를 다시 골라주세요 ", True, white)
            pygame.draw.rect(screen, black, [0, screen_height / 2, screen_width, 70])
            screen.blit(warning, ((screen_width - warning.get_width()) / 2, screen_height / 2))
        elif (choice_button3):
            warning = font.render("당신은 해고 당했습니다. 선택지를 다시 골라주세요.", True, white)
            pygame.draw.rect(screen, black, [0, screen_height / 2, screen_width, 70])
            screen.blit(warning, ((screen_width - warning.get_width()) / 2, screen_height / 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)


def answer_1():
    text = font.render("<알바생>", True, black)
    text1 = font.render("저 , 사장님.. 수습기간에도 최저임금은 정당하게 받을 수 있는거라고 알고있는데요.", True, black)
    text2 = font.render("<사장>", True, black)
    text3 = font.render("(뭐야, 알바 처음이라더니 .. 어떻게 알았지? 젠장!)", True, black)
    text4 = font.render("아,, 하하 그런가 ? 착각을 했나보네 내가...", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(사장+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 480))
        screen.blit(text1, (80, 520))
        screen.blit(text2, (80, 560))
        screen.blit(text3, (80, 600))
        screen.blit(text4, (80, 640))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            contract1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)


# 근로계약서 함수
def contract1():
    text1 = font.render("<SYSTEM>", True, red)
    text2 = font.render("(근로 계약서의 일부분이 추가되었습니다.) -> 다음 단계로 넘어가기!", True, black)
    text3 = font.render("임금 : 시간 당 8720원 (최저임금)", True, black)

    while True:
        bg = pygame.image.load("근로계약서 (배경+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text1, (80, 500))
        screen.blit(text2, (80, 540))
        screen.blit(text3, (350, 250))

        next_button3 = create_button(900, 600, 120, 40, deepbrown,lightbrown)
        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (900, 600))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen14_1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 법정근로시간부분 코드입니다.


def screen14_1():
    text = font.render("<알바생> ", True, black)
    text1 = font.render("아 일한지 10시간은 된 것 같은데 4시간밖에 안지났네 .. 서서 일하니까 더 힘든것 같아..", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(알바생+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            screen14_2()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen14_2():
    text = font.render("<사장> ", True, black)
    text1 = font.render("알바 잘 하고 있나? 에? 손님이 많이오면 얼마나 많이 왔다고 벌써 죽을상이야.", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(사장+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen14_3()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen14_3():
    text1 = font.render("<알바생>", True, black)
    text2 = font.render(" (진짜 바빠서 힘든건데 … 너무하시네) 아..하하.. 근데요, 사장님. 저, 그...", True, black)
    text3 = font.render(" <사장> ", True, black)
    text4 = font.render(" 응? 왜 그러나?", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(사장+알바생+대화).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text1, (80, 500))
        screen.blit(text2, (80, 540))
        screen.blit(text3, (80, 580))
        screen.blit(text4, (80, 620))

        next_button4 = create_button(800, 600, 120, 40, deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (800, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            question_2()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def question_2():
    while True:
        bg = pygame.image.load("배경_카운터(사장+알바생+대화).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기

        choice_button1 = create_button(100, 520, 800, 40, white, (226, 226, 226))
        choice_button1_text = font.render("1. 이 가게에서 정한 쉬는시간은 없는건가요..? 저 너무 힘든데.", True, black)
        screen.blit(choice_button1_text, (110, 520))

        choice_button2 = create_button(100, 570, 800, 40, white, (226, 226, 226))
        choice_button2_text = font.render("2. 야이 손님이 안오긴 뭘 안와4시간내내 논스탑으로 들어오더만 진짜 힘들다고 좀 쉬자", True, black)
        screen.blit(choice_button2_text, (110, 570))

        choice_button3 = create_button(100, 620, 800, 40, white, (226, 226, 226))
        choice_button3_text = font.render("3. 법적으로 정한 근로 휴식시간이 있지 않아요? 저 일 되게 오래 했는데.. 조금 쉬고 싶어요", True, black)
        screen.blit(choice_button3_text, (110, 620))

        if choice_button3:  # True 라면, 즉 클릭했다면
            answer_2()
        elif (choice_button1):
            warning = font.render("당신은 사장의 계략에 넘어갔습니다. 선택지를 다시 골라주세요 ", True, white)
            pygame.draw.rect(screen, black, [0, screen_height / 2, screen_width, 70])
            screen.blit(warning, ((screen_width - warning.get_width()) / 2, screen_height / 2))
        elif (choice_button2):
            warning = font.render("당신은 해고 당했습니다. 선택지를 다시 골라주세요.", True, white)
            pygame.draw.rect(screen, black, [0, screen_height / 2, screen_width, 70])
            screen.blit(warning, ((screen_width - warning.get_width()) / 2, screen_height / 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)

def answer_2():
    text = font.render("<사장>", True, black)
    text1 = font.render(" 아 .. 근로 휴식 시간 말하는건가 ..?", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(사장+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 480))
        screen.blit(text1, (80, 520))

        next_button4 = create_button(800, 600, 120, 40,deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (800, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            answer_2_1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def answer_2_1():
    text = font.render("<알바생>", True, black)
    text1 = font.render("네.제가 알기로는 4시간당 30분 이상, 8시간이면 1시간 이상 정도는 의무적으로 근로 휴식 시간이 있다고", True, black)
    text2 = font.render("하던데 .. 저 4시간 힘들게 일했으니, 30분정도만 쉬어도 될까요?", True, black)
    text3 = font.render("<사장>", True, black)
    text4 = font.render("그.. 그래 .. 그럼 ..30분만 ..쉬고 해 .. ( 아니, 첫알바라면서 뭘 이렇게 자세하게 아는거야!)", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(사장+알바생+대화).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 480))
        screen.blit(text1, (80, 520))
        screen.blit(text2, (80, 560))
        screen.blit(text3, (80, 600))
        screen.blit(text4, (80, 640))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            contract2()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


# 근로계약서 함수
def contract2():
    text1 = font.render("<SYSTEM>", True, red)
    text2 = font.render("(근로 계약서의 일부분이 추가되었습니다) -> 다음 단계로 넘어가기!", True, black)
    text3 = font.render("휴식시간 : 4시간에 30분, 8시간에 1시간", True, black)

    while True:
        bg = pygame.image.load("근로계약서 (배경+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text1, (80, 500))
        screen.blit(text2, (80, 540))
        screen.blit(text3, (350, 250))

        next_button3 = create_button(900, 600, 100, 40, deepbrown, lightbrown)
        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (900, 600))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen15_1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 시간외수당부분 코드입니다.


def screen15_1():
    text = font.render("<알바생> ", True, black)
    text1 = font.render("오늘은 좀 바쁜데 ..? 아 손님이다. 어서오세요~", True, black)
    text2 = font.render("<손님> ", True, black)
    text3 = font.render("아이스 아메리카노 두 잔 주세요.", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(알바생+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))
        screen.blit(text3, (80, 620))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen15_2()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정



def screen15_2():
    text = font.render("<알바생> ", True, black)
    text1 = font.render("아이스 아메리카노 두 잔 맞으시죠? 4000원 입니다!", True, black)
    text2 = font.render("<손님>", True, black)
    text3 = font.render("네. 여기 카드요.", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(손님+알바생+대화).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))
        screen.blit(text3, (80, 620))


        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            screen16_1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen16_1():
    text = font.render("<손님 친구> ", True, black)
    text1 = font.render("아 맞다. 야, 너 주휴수당 그거 점장한테 말 해봤어?", True, black)
    text2 = font.render("<손님> ", True, black)
    text3 = font.render("아, 그런거 모르겠다고 신고할거면 하라고 하더라?", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(손님들).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))
        screen.blit(text3, (80, 620))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen16_2()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen16_2():
    text = font.render("<손님> ", True, black)
    text1 = font.render("완전 어이없어 … 적반하장이 따로 없다니까?", True, black)
    text2 = font.render("<손님 친구> ", True, black)
    text3 = font.render("뭐 그런 미친@#$%#$%@#...", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(손님들).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))
        screen.blit(text3, (80, 620))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            screen17()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen17():
    text = font.render("<알바생> ", True, black)
    text1 = font.render("어우.. 무섭네… 근데 주휴수당이 뭐지..? ", True, black)
    text2 = font.render("점장이라고 하는거 보면 일 하면서 받아야 할 돈 같은데 …", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(알바생+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen18()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen18():
    text = font.render("<사장>", True, black)
    text1 = font.render("안에 들어갈 냅킨이랑 일회용 식기들은 바에 있는데 일회용 식기 포장 좀 해놓을래? ", True, black)
    text2 = font.render("<알바생>", True, black)
    text3 = font.render("네! 알겠습니다!!", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(사장+알바생+대화).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))
        screen.blit(text3, (80, 620))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            cafe_map_2()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def cafe_map_2():  # 스크린 18과 19사이
    k = 0

    while True:
        cafeMap = pygame.image.load("배경_평면도.jpg")
        screen.blit(cafeMap, (0, 0))  # 배경 그리기
        star1 = pygame.image.load("yellowStar.png")
        star2 = pygame.image.load("yellowStar.png")
        k += 1

        if (k % 13 == 0) or (k % 13 == 1) or (k % 13 == 2):
            screen.blit(star1, (655, 120))
            screen.blit(star2, (500, 450))
            nextStarButton = create_star_button(800, 450, yellowStar, redStar)
            if nextStarButton:
                screen19()  # 19 배경을 냅킨 이미지로 바꿀 것

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                k = 0

        pygame.display.update()
        clock.tick(15)


def screen19():
    text = font.render("<알바생> ", True, black)
    text1 = font.render("아니 누가 냅킨에 뭘 적어놨네 … 뭐라고 적혀있는 거지?", True, black)

    while True:
        bg = pygame.image.load("단서_냅킨(배경+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            question_3()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def question_3():
    text1 = font.render("저번에 분명 주휴수당에 대해 알아봤는데..", True, black)
    text2 = font.render("이 중에 하나는 틀린 설명이었던 것 같아...그게 뭘까..?", True, black)

    while True:
        bg = pygame.image.load("단서_냅킨(배경+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text1, (80, 500))
        screen.blit(text2, (80, 540))

        choice_button1 = create_button(200, 150, 500, 40, white, (226, 226, 226))
        choice_button1_text = font.render("정규직, 계약직이 아닌 시간제 근로자도 받을 수 있다.", True, black)
        screen.blit(choice_button1_text, (210, 150))

        choice_button2 = create_button(200, 200, 750, 40, white, (226, 226, 226))
        choice_button2_text = font.render("주휴수당을 받기 위해서는 일주일간 근로시간이 최소 15시간 이상이어야 한다.", True, black)
        screen.blit(choice_button2_text, (210, 200))

        choice_button3 = create_button(200, 250, 850, 40, white, (226, 226, 226))
        choice_button3_text = font.render("일주일간 무단결근이 없어야 한다. 단, 사전 동의를 구한 결근일 경우 결근으로 보지 않는다.", True, black)
        screen.blit(choice_button3_text, (210, 250))

        choice_button4 = create_button(200, 300, 600, 40, white, (226, 226, 226))
        choice_button4_text = font.render("지각이나 조퇴를 해도 주휴수당을 받는 데에는 문제가 없다.", True, black)
        screen.blit(choice_button4_text, (210, 300))

        if choice_button3:  # True 라면, 즉 클릭했다면
            answer_3()
        elif (choice_button2) or (choice_button1) or (choice_button4):
            warning = font.render("정답이 아닙니다 ㅜㅅㅜ 다른 선택지를 골라주세요!", True, white)
            pygame.draw.rect(screen, black, [0, screen_height / 2, screen_width, 70])
            screen.blit(warning, ((screen_width - warning.get_width()) / 2, screen_height / 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)


def answer_3():
    text = font.render("<알바생>", True, black)
    text1 = font.render("이거 아닌가 ..? 괜히 정답이 궁금해지네. 어…? 안쪽에도 글씨가 써 있네?", True, black)

    while True:
        bg = pygame.image.load("단서_냅킨(배경+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 480))
        screen.blit(text1, (80, 520))

        next_button4 = create_button(800, 600, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (800, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            answer_3_1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def answer_3_1():
    text = font.render("정답은 3번입니다!", True, black)
    text1 = font.render("일주일중 무단이든, 사전동의를 구했든 결근이 있었다면", True, black)
    text2 = font.render("주휴수당은 받을 수 없습니다!", True, black)

    while True:
        bg = pygame.image.load("단서_냅킨(배경).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (300, 300))
        screen.blit(text1, (300, 340))
        screen.blit(text2, (300, 380))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            contract3()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


# 근로계약서 함수
def contract3():
    text1 = font.render("[SYSTEM]", True, red)
    text2 = font.render("(근로 계약서의 일부분이 추가되었습니다.) -> 다음 단계로 넘어가기!", True, black)
    text3 = font.render("주휴수당 : 일주일 개근시 주휴수당을 지급", True, black)

    while True:
        bg = pygame.image.load("근로계약서 (배경+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text1, (80, 500))
        screen.blit(text2, (80, 540))
        screen.blit(text3, (350, 250))

        next_button3 = create_button(900, 600, 120, 40, deepbrown,lightbrown)
        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (900, 600))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen20()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ


# 임금 체불부분 코드입니다.
# background 이미지 카운터로 전환

def screen20():
    text = font.render("<알바생> ", True, black)
    text1 = font.render("네, 손님. 안녕히가세요~", True, black)
    text2 = font.render(" .. 이제 오늘 알바만 끝나면 여기서 일한지도 벌써 한달째구나 …", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(알바생+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            screen21()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen21():
    text = font.render("<알바생> ", True, black)
    text1 = font.render(" 휴, 곧 월급날이니까 조금만 참아보자.. 어?.. 무슨 소리지 ..?", True, black)
    text2 = font.render("( !띵동! 어디서 핸드폰 알림 소리가 들렸다.)", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(알바생+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            cafe_map_3()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def cafe_map_3():  # 스크린 21과 22사이
    k = 0

    while True:
        cafeMap = pygame.image.load("배경_평면도.jpg")
        screen.blit(cafeMap, (0, 0))  # 배경 그리기
        star1 = pygame.image.load("yellowStar.png")
        star2 = pygame.image.load("yellowStar.png")
        k += 1

        if (k % 13 == 0) or (k % 13 == 1) or (k % 13 == 2):
            screen.blit(star1, (800, 450))
            screen.blit(star2, (500, 450))
            nextStarButton = create_star_button(655, 120, yellowStar, redStar)
            if nextStarButton:
                screen22()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                k = 0

        pygame.display.update()
        clock.tick(15)


def screen22():
    text = font.render("<알바생> ", True, black)
    text1 = font.render("어? 누가 핸드폰을 두고 갔나보네.. 전화를 드려야겠ㄷ.. ", True, black)
    text2 = font.render("뭐야 이건. 퀴즈..?", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(알바생+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True,white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            question_4()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def question_4():
    text1 = font.render("“부당한 임금체불, 이제는 구분하자 ! 다음중 , 임금체불의 사례가 아닌 것은 무엇일까요?”", True, black)

    while True:
        bg = pygame.image.load("단서_휴대폰(배경+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text1, (80, 500))

        choice_button1 = create_button(200, 150, 700, 40, white, (226, 226, 226))
        choice_button1_text = font.render("1. 정해진 임금 지급일에 임금 전액이나 임금 일부를 지급하지 않은 경우", True, black)
        screen.blit(choice_button1_text, (210, 150))

        choice_button2 = create_button(200, 200, 700, 40, white, (226, 226, 226))
        choice_button2_text = font.render("2. 근로자와 합의하지 않고 사용자가 일방적으로 임금을 추가한 경우", True, black)
        screen.blit(choice_button2_text, (210, 200))

        choice_button3 = create_button(200, 250, 700, 40, white, (226, 226, 226))
        choice_button3_text = font.render("3. 근로자의 동의 없이 상여금 일부를 지급하지 않거나, 상여금을 반환한 경우", True, black)
        screen.blit(choice_button3_text, (210, 250))

        choice_button4 = create_button(200, 300, 700, 40, white, (226, 226, 226))
        choice_button4_text = font.render("4. 만약 퇴직한 근로자의 동의가 없었음에도 지급을 퇴직후 14일까지 미룬 경우", True, black)
        screen.blit(choice_button4_text, (210, 300))

        if choice_button2:  # True 라면, 즉 클릭했다면
            answer_4()
        elif (choice_button3) or (choice_button1) or (choice_button4):
            warning = font.render(" 땡 ! 임금체불 사례가 아닌것을 다시 골라주세요.", True, white)
            pygame.draw.rect(screen, black, [0, screen_height / 2, screen_width, 70])
            screen.blit(warning, ((screen_width - warning.get_width()) / 2, screen_height / 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)


def answer_4():
    text = font.render("정답 ! 잘 맞추셨습니다.", True, black)
    text1 = font.render("임금 ‘추가' 가 아니라 ‘삭감' 이죠.", True, black)

    while True:
        bg = pygame.image.load("단서_휴대폰(배경).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (400, 240))
        screen.blit(text1, (400, 280))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            contract4()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)


# 근로계약서 함수
def contract4():
    text1 = font.render("[SYSTEM]", True, red)
    text2 = font.render("(근로 계약서의 일부분이 추가되었습니다) -> 다음 단계로 넘어가기!", True, black)
    text3 = font.render("임금지급일 :  매월 25일", True, black)

    while True:
        bg = pygame.image.load("근로계약서 (배경+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text1, (80, 500))
        screen.blit(text2, (80, 540))
        screen.blit(text3, (390, 350))

        next_button3 = create_button(900, 600, 120, 40, deepbrown,lightbrown)
        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (900, 600))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen23_1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)
# 아웃트로부분 코드입니다.
# background 이미지 - 카운터로 전환


def screen23_1():
    text = font.render("<사장> ", True, black)
    text1 = font.render("오늘도 알바하느라 수고했어~", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(사장+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen23_2()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen23_2():
    text = font.render("<알바생> ", True, black)
    text1 = font.render("네! 수고하셨어요… 그런데, 사장님! 오늘 월급 들어오는날, 맞죠??", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(알바생+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            screen24_1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen24_1():
    text = font.render("<사장> ", True, black)
    text1 = font.render("어? 어.. 그렇긴 한데.. 그 정말 미안한데, 내가 지금 당장 돈이 없어서 말이야..", True, black)
    text2 = font.render("월급은 일주일정도 뒤에 줘도 될까?", True, black)
    while True:
        bg = pygame.image.load("배경_카운터(사장+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen24_2()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen24_2():
    text = font.render("<알바생> ", True, black)
    text1 = font.render("네? 그게 무슨 소리세요, 사장님. 월급은 지정한 날에 주셔야죠!! ", True, black)
    text2 = font.render("이거, 엄연한 임금 체불이거든요!", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(알바생+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            screen25()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen25():
    text = font.render("<사장>", True, black)
    text1 = font.render("임금 체불이라니, 내가 나중에 꼭 주겠다니까~ 지금 당장 돈이 없어서 그래!!", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(사장+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen26()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen26():
    text = font.render("<알바생> ", True, black)
    text1 = font.render("하,, 제가 그동안 참고 넘어간 것도 많은데, 월급도 제때 안주신다니 할 수 없네요.", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(알바생+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40,deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            screen27_1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen27_1():
    text = font.render("<알바생> ", True, black)
    text1 = font.render("제가 지금까지 당한 부당한 일들 전부! 노동청에 들고 가서 진정서 제출 하겠습니다.", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(알바생+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen27_2()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen27_2():
    text = font.render("<사장> ", True, black)
    text1 = font.render("그게 무슨 소리야. 진정..서? 제출이라니!", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(사장+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40, deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            screen28_1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen28_1():
    text = font.render("<알바생> ", True, black)
    text1 = font.render(" 사장님이 수습기간일때 최저임금보다 적게 주신다고 한거, ", True, black)
    text2 = font.render("근로 기준법에 명시되어 있는 근로 휴식 시간을 모른척 하면서 부려먹으려고 하신거! ", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(알바생+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen28_2()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen28_2():
    text = font.render("<알바생> ", True, black)
    text1 = font.render("그리고 지금처럼, 임금 제때 안 주시려고 하신거 전부 다 노동청에 말하겠다고요!", True, black)
    text2 = font.render("앞으로 제 권리는 제가 지킬거에요", True, red)

    while True:
        bg = pygame.image.load("배경_카운터(알바생+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))

        next_button4 = create_button(((screen_width - text.get_width()) / 2) + 20, 600, 120, 40, deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            screen29()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen29():
    text = font.render("<사장> ", True, black)
    text1 = font.render(" 부,, 부려먹다니. 내가 언제..! 안돼, 가지마!! 학생!!", True, black)

    while True:
        bg = pygame.image.load("배경_카운터(사장+대화창).jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기

        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen30()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# background 이미지 - 바깥사진으로 전환


def screen30():
    text = font.render("<알바생> ", True, black)
    text1 = font.render("꼴좋다. 앞으로 절대 이런 곳에서는 알바 하지 않겠어.", True, black)
    text2 = font.render(".. 생각해보니, 나처럼 알바를 하면서 부당한 일을 겪고 있는 사람들이 참 많을 것 같은데..", True, black)

    while True:
        bg = pygame.image.load("길거리사진.jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))

        next_button4 = create_button(((screen_width - text.get_width()) / 2) + 20, 600, 120, 40, deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (((screen_width - text.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            screen31()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen31():
    text = font.render("<알바생> ", True, black)
    text1 = font.render("노동법 상식 교육 게임 같은걸 만들면 이런 일을 겪는 사람들이 조금이나마 줄어들지 않을까?..", True, black)
    text2 = font.render("좋아. 한번 만들어보자! (그렇게 주인공은 이 게임을 만들었다고 한다......)", True, red)

    while True:
        bg = pygame.image.load("마지막장면.jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text, (80, 500))
        screen.blit(text1, (80, 540))
        screen.blit(text2, (80, 580))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            screen32()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 최종 아웃트로 장면
# 이미지- 까만화면? 으로 전환.(고려중)

def screen32():
    text1 = font.render("[system] ", True, black)
    text2 = font.render(" 축하합니다. 당신은 주인공의 권리를 지켜냈습니다! 만약 현실에서 이러한 부당한 일을 당하신다면,", True, black)
    text3 = font.render(" 이 게임의 주인공처럼 권리를 지켜내세요! 게임을 통해 노동법에 한발짝 가까워졌기를 바랍니다.", True, black)

    while True:
        bg = pygame.image.load("길거리사진.jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text1, (80, 500))
        screen.blit(text2, (80, 540))
        screen.blit(text3, (80, 580))

        next_button4 = create_button(((screen_width - text1.get_width()) / 2) + 20, 600, 120, 40,deepbrown,lightbrown)

        next_button_text = titleFont.render("다음", True,white)
        screen.blit(next_button_text, (((screen_width - text1.get_width()) / 2) + 50, 600))

        if next_button4:  # True 라면, 즉 클릭했다면
            screen33()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def screen33():
    text1 = font.render("< 고용 노동부 고객상담센터 - 국번없이 1350 >", True, black)

    text2 = font.render("소프트웨어와창의적사고 05분반 1조", True, black)
    text3 = font.render("디지털미디어학과 21학번 강영은, 소프트웨어융합학과 16학번 옥유진, 정보보호학과 17학번 이혜민", True, black)
    text4 = font.render("디지털미디어학과 21학번 변혜빈, 디지털미디어학과 21학번 전지현", True, black)

    text5 = font.render("감사합니다.", True, black)

    while True:
        bg = pygame.image.load("첫화면.jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(text1, (320, 220))
        screen.blit(text2, (350, 300))
        screen.blit(text3, (90, 360))
        screen.blit(text4, (250, 420))
        screen.blit(text5, (500, 480))

        next_button3 = create_button(800, 630, 120, 40, deepbrown, lightbrown)

        next_button_text = titleFont.render("다음", True, white)
        screen.blit(next_button_text, (830, 630))

        if next_button3:  # True 라면, 즉 클릭했다면
            outro()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


def outro():
    start_text = font.render(" ", True, deepbrown)
    text1 = titleFont.render("지금까지 플레이 해주셔서 감사합니다.", True, black)
    text2 = font.render("게임을 종료 하시겠습니까?", True, deepbrown)

    while True:
        bg = pygame.image.load("첫화면.jpg")
        screen.blit(bg, (0, 0))  # 배경 그리기
        screen.blit(start_text, ((screen_width - start_text.get_width()) / 2, 20))
        screen.blit(text1, (((screen_width - text1.get_width()) / 2) , 300))
        screen.blit(text2, (((screen_width - text2.get_width()) / 2) , 430))

        start_button = create_button(((screen_width - start_text.get_width()) / 2) + 20, 630, 120, 40, deepbrown, lightbrown)
        quit_button = create_button(((screen_width - start_text.get_width()) / 2) + 170, 630, 120, 40, deepbrown, lightbrown)

        startbuttontext = titleFont.render("다시", True, white)
        screen.blit(startbuttontext, (((screen_width - start_text.get_width()) / 2) + 50, 630))

        quitbuttontext = titleFont.render("종료", True, white)
        screen.blit(quitbuttontext, (((screen_width - start_text.get_width()) / 2) + 200, 630))

        if start_button:  # True라면, 즉 클릭했다면
            intro()

        if quit_button:
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # x누르면 종료함
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)  # fps 15로 설정


# 메인 게임 루프
while True:
    intro()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(15)  # fps 15로 설정