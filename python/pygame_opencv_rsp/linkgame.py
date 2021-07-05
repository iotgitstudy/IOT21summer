import single
import cv2
import mediapipe as mp
import numpy as np
import pygame
import os

##############
#pip install mediapipe
#pip install cv2
#pip install pygame
# 필수

#조작법 : 방향키 좌우 이동, 스페이스 바- 무기 발사, 화면에 주먹보이기-무기발사
#####################################################

#기본 초기화 (반드시 해야 하는 것들)



pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정

screen_width = 640 #가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))


#화면 타이틀 설정
pygame.display.set_caption("my_game_pang") # 게임 이름

#FPS
clock = pygame.time.Clock()

#####################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

#배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터 위치하기 위해 사용

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height
#캐릭터 이동속도
character_speed = 5
#캐릭터 이동 방향
character_to_x = 0

#무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기는 한 번에 여러 번 발사 가능
weapons = []
weapon_speed = 10

max_num_hands = 2
gesture = {
    0:'fist', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
    6:'six', 7:'rock', 8:'spiderman', 9:'yeah', 10:'ok',
}
rps_gesture = {0:'rock', 5:'paper', 9:'scissors'}

# MediaPipe hands model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=max_num_hands,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# Gesture recognition model
file = np.genfromtxt('data/gesture_train.csv', delimiter=',')
angle = file[:,:-1].astype(np.float32)
label = file[:, -1].astype(np.float32)
knn = cv2.ml.KNearest_create()
knn.train(angle, cv2.ml.ROW_SAMPLE, label)

cap = cv2.VideoCapture(0)



running = True #게임이 진행중인가?
while running and cap.isOpened():
    dt = clock.tick(7) # 게임화면의 초당 프레임 수를 설정
    
    ret, img = cap.read()
    if not ret:
        continue
        
    img = cv2.flip(img, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    result = hands.process(img)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    if result.multi_hand_landmarks is not None:
        for res in result.multi_hand_landmarks:
            joint = np.zeros((21, 3))
            for j, lm in enumerate(res.landmark):
                joint[j] = [lm.x, lm.y, lm.z]

            # Compute angles between joints
            v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:] # Parent joint
            v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:] # Child joint
            v = v2 - v1 # [20,3]
            # Normalize v
            v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

            # Get angle using arcos of dot product
            angle = np.arccos(np.einsum('nt,nt->n',
                v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
                v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

            angle = np.degrees(angle) # Convert radian to degree

            # Inference gesture
            data = np.array([angle], dtype=np.float32)
            ret, results, neighbours, dist = knn.findNearest(data, 3)
            idx = int(results[0][0])
            print(ret)
            

        # Draw gesture result
            if idx in rps_gesture.keys():
                cv2.putText(img, text=rps_gesture[idx].upper(), org=(int(res.landmark[0].x * img.shape[1]), int(res.landmark[0].y * img.shape[0] + 20)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)

            # Other gestures
            # cv2.putText(img, text=gesture[idx].upper(), org=(int(res.landmark[0].x * img.shape[1]), int(res.landmark[0].y * img.shape[0] + 20)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)

            mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('Game', img)
    if cv2.waitKey(1) == ord('q'):
        break

    
    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #왼쪽
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: #오른쪽
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: #무기 발사
                if len(weapons) > 5:
                    break
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
    


        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    if ret == 5.0:
        character_to_x += character_speed
    if ret == 9.0:
        character_to_x -= character_speed
    if ret ==10.0:
        character_to_x = 0

    if ret == 0.0 and len(weapons) < 6:
        if len(weapons) > 1 and weapons[-1][1] >140:
            pass
        else:
            weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
            weapon_y_pos = character_y_pos
            weapons.append([weapon_x_pos, weapon_y_pos])    

    # 3. 게임 캐릭터 위치 정의 
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    
    #무기 위치 조정
    # 100 200 -> 100/ 180 160 140 ...
    # 500 200 -> 500/ 180 160 140 ...
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]

    #무기 삭제
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]



    # 4. 충돌처리
    
    # 5. 화면에 그리기
    
    screen.blit(background, (0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    screen.blit(stage, (0,screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    


    pygame.display.update() #게임화면을 다시 그리기
    
# pygame 종료

pygame.quit()

