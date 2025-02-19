import cv2
import numpy as np

def create_resized_grid(image, one_pixel_size):
    """
    1. 원본 이미지의 크기를 감지하고, 이를 픽셀 블록으로 해석
    2. one_pixel_size를 기준으로 새로운 픽셀아트 생성 (정사각형 유지)
    """
    original_height, original_width, _ = image.shape
    
    # 새로운 그리드 크기 계산 (one_pixel_size를 이용해 정사각형 유지)
    target_width = round(original_width / one_pixel_size)
    target_height = round(original_height / one_pixel_size)
    
    # 정사각형 유지 보정 (block_x == block_y 강제)
    block_size = (original_width / target_width + original_height / target_height) / 2
    
    # 새로운 이미지 생성 (초기화)
    new_image = np.zeros((target_height, target_width, 3), dtype=np.uint8)
    
    for i in range(target_height):
        for j in range(target_width):
            # 각 블록의 중앙 픽셀 좌표 계산
            center_x = int((j + 0.5) * block_size)
            center_y = int((i + 0.5) * block_size)
            
            # 경계값 처리 (이미지 범위를 초과하는 경우 방지)
            center_x = min(center_x, original_width - 1)
            center_y = min(center_y, original_height - 1)
            
            # 색상 샘플링
            new_image[i, j] = image[center_y, center_x]
    
    return new_image