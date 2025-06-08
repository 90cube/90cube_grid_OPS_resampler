import sys
import os
import cv2
import numpy as np
import gradio as gr

# src 폴더 추가하여 grid_sampler.py 불러오기
sys.path.append(os.path.abspath("src"))
from grid_sampler import create_resized_grid
from image_loader import save_image

# input 및 output 폴더 자동 생성
os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

def process_image(image, one_pixel_size):
    """Gradio에서 업로드된 이미지를 처리하여 변환합니다."""
    np_image = np.array(image)
    if np_image.shape[2] == 4:
        cv_image = cv2.cvtColor(np_image, cv2.COLOR_RGBA2BGRA)
    else:
        cv_image = cv2.cvtColor(np_image, cv2.COLOR_RGB2BGR)

    resized_img = create_resized_grid(cv_image, one_pixel_size)

    output_path = "output/gradio_result.png"
    save_image(resized_img, output_path)

    if resized_img.shape[2] == 4:
        preview = cv2.cvtColor(resized_img, cv2.COLOR_BGRA2RGBA)
    else:
        preview = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)

    return preview, output_path

# Gradio UI 생성
iface = gr.Interface(
    fn=process_image,
    inputs=[
        gr.Image(type="pil"),  # 이미지 업로드
        gr.Slider(minimum=0.5, maximum=10, step=0.1, value=1.0, label="One Pixel Size")  # ✅ OPS 정수/소수 지원
    ],
    outputs=[
        gr.Image(type="numpy", label="Preview"),  # ✅ 실시간 미리보기 추가
        gr.File(label="Download Processed PNG")  # ✅ PNG 다운로드 버튼 유지
    ],
    title="Pixel Art Resizer",
    description="Upload an image, set One Pixel Size, and preview the result before downloading.",
)

if __name__ == "__main__":
    iface.launch(share=False, inbrowser=True)
