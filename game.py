import pygame
import random
import os

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("두더지 잡기 게임!")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 두더지 이미지 로드
mole_path = os.path.join(os.getcwd(), "mole.png")
if not os.path.exists(mole_path):
    print("❌ mole.png 파일을 찾을 수 없습니다!")
    pygame.quit()
    exit()

mole_image = pygame.image.load(mole_path)
mole_size = 80
mole_image = pygame.transform.scale(mole_image, (mole_size, mole_size))

# 두더지 초기 위치 설정
mole_x = random.randint(0, WIDTH - mole_size)
mole_y = random.randint(0, HEIGHT - mole_size)

# 폰트 설정
font = pygame.font.Font(None, 36)

# 게임 변수
score = 0
time_limit = 30  # 제한 시간 (초)
start_time = pygame.time.get_ticks()

running = True
while running:
    screen.fill(WHITE)

    # 현재 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    remaining_time = max(0, time_limit - elapsed_time)

    print(f"⏳ Elapsed time: {elapsed_time}, Remaining time: {remaining_time}")

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # 스페이스바를 누르면 게임 종료
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mole_x < mouse_x < mole_x + mole_size and mole_y < mouse_y < mole_y + mole_size:
                score += 1
                mole_x = random.randint(0, WIDTH - mole_size)
                mole_y = random.randint(0, HEIGHT - mole_size)
            else:
                score -= 1

    # 두더지 그리기
    screen.blit(mole_image, (mole_x, mole_y))

    # 점수 표시
    score_text = font.render(f"점수: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # 남은 시간 표시
    time_text = font.render(f"남은 시간: {remaining_time}초", True, BLACK)
    screen.blit(time_text, (10, 40))

    if remaining_time <= 0:
        print("⏳ 게임 종료!")
        running = False
        break

    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(50)

# 게임 종료 화면
print(f"🎯 최종 점수: {score}")  # 콘솔에 최종 점수 출력
screen.fill(WHITE)
end_text = font.render(f"게임 종료! 최종 점수: {score}", True, BLACK)
screen.blit(end_text, (WIDTH // 4, HEIGHT // 2 - 20))
score_text = font.render(f"최종 점수: {score}", True, BLACK)
screen.blit(score_text, (WIDTH // 4, HEIGHT // 2 + 20))
pygame.display.flip()
pygame.time.delay(2000)  # 🔥 2초 후 종료 (너무 오래 기다리지 않도록)

# 🔥 Mac에서도 강제 종료 가능하도록 
pygame.event.post(pygame.event.Event(pygame.QUIT))  
pygame.quit()
exit()
