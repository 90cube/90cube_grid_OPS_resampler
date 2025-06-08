import cv2
import numpy as np

def create_resized_grid(image, one_pixel_size):
    """이미지 크기를 변경하되 정사각형 픽셀을 유지합니다.

    Parameters
    ----------
    image : ``numpy.ndarray``
        BGR(A) 형식의 이미지 배열로 3채널 또는 4채널을 모두 지원합니다.
    one_pixel_size : float
        출력 이미지에서 한 픽셀이 원본에서 차지하는 크기입니다.
    """
    original_height, original_width, channels = image.shape
    
    # 새로운 그리드 크기 계산 (one_pixel_size를 이용해 정사각형 유지)
    if one_pixel_size <= 0:
        raise ValueError("one_pixel_size must be greater than 0")

    target_width = max(1, round(original_width / one_pixel_size))
    target_height = max(1, round(original_height / one_pixel_size))
    
    # 정사각형 유지 보정 (block_x == block_y 강제)
    block_size = (original_width / target_width + original_height / target_height) / 2
    
    # 새로운 이미지 생성 (초기화)
    new_image = np.zeros((target_height, target_width, channels), dtype=np.uint8)
    
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