import cv2
import os

def save_image(image, save_path="output/processed.png"):
    """
    변환된 이미지를 저장하는 함수
    - 기본 저장 경로는 'output/processed.png'
    - 필요하면 다른 경로도 지정 가능
    """
    # 출력 폴더가 없으면 생성
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # 이미지 저장
    cv2.imwrite(save_path, image)
    print(f"✅ 이미지 저장 완료: {save_path}")

