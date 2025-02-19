# 🎨 90cube Grid OPS Resampler

### **정확한 픽셀아트 축소를 위한 Grid-Based Resampler**  
✔ 픽셀아트를 **정사각형 픽셀을 유지하면서** 축소하는 변환기  
✔ **OPS (One Pixel Size)** 값을 조절하여 **정확한 그리드 크기로 변환 가능**  
✔ **Gradio 기반 웹 UI 제공** → 이미지 업로드 & 미리보기 & 변환 결과 다운로드  

---

## **📌 OPS (One Pixel Size)란?**
OPS(One Pixel Size)는 **픽셀 하나가 원본 이미지에서 차지하는 크기**를 의미합니다.  
예를 들어:  
- `OPS = 2` → 원본 이미지의 **2×2 블록이 1픽셀**이 됨 (**50% 크기로 축소**)  
- `OPS = 3` → 원본 이미지의 **3×3 블록이 1픽셀**이 됨 (**1/3 크기로 축소**)  
- `OPS = 0.8` → 원본 크기보다 **1.25배 커짐** (더 세밀한 픽셀 보존)  

✅ **OPS 값을 소수(예: `1.25`, `0.8`, `2.2`)로 설정 가능!**  
✅ **픽셀 왜곡 없이 정사각형 그리드를 유지하여 축소!**  

---

## **📌 설치 방법**
**🚀 Python 3.12가 설치되어 있어야 합니다.**  
📌 [Python 공식 사이트](https://www.python.org/downloads/)에서 Python 3.12을 설치해주세요.  

### **1️⃣ 프로젝트 클론**
```bash
git clone https://github.com/90cube/90cube_grid_OPS_resampler.git
cd 90cube_grid_OPS_resampler
```

### **2️⃣ 가상환경 생성 및 패키지 설치**
Windows의 경우:
```bash
install.bat
```
Mac/Linux의 경우:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## **📌 실행 방법**
### **1️⃣ Gradio 웹 UI 실행**
```bash
start.bat
```
✅ 실행하면 **자동으로 웹 브라우저가 열림**  
✅ UI에서 **이미지 업로드 → `OPS` 값 설정 → 미리보기 → 변환 결과 다운로드 가능!**  

### **2️⃣ 터미널에서 수동 실행**
```bash
call venv\Scripts\activate
python app.py
```

---

## **📌 주요 기능**
✅ **정사각형 픽셀 유지** → 픽셀아트의 품질을 유지하면서 변환  
✅ **OPS 값 조절 (0.5~10, 소수 가능)** → 더 정밀한 크기 조정 가능  
✅ **Gradio 기반 웹 UI 제공** → 간편한 이미지 업로드 & 변환  
✅ **변환된 결과 미리보기 가능** → 다운로드 전에 픽셀아트 확인  

---

## **📌 프로젝트 구조**
```plaintext
90cube_grid_OPS_resampler/
│── input/               # 원본 이미지 저장 폴더 (자동 생성됨)
│── output/              # 변환된 이미지 저장 폴더 (자동 생성됨)
│── src/                 # 핵심 코드 폴더
│   │── grid_sampler.py  # 픽셀 변환 (그리드 기반 변환)
│   │── image_loader.py  # 이미지 로드 & 저장 처리
│── app.py               # Gradio 웹 UI 실행 파일
│── install.bat          # 가상환경 생성 & 패키지 설치 자동화
│── start.bat            # 가상환경 활성화 & Gradio 실행
│── requirements.txt     # 필수 패키지 목록
│── README.md            # 프로젝트 설명서
```

---


🚀 **더 많은 기능이 필요하면 언제든지 피드백 주세요!**  
---

추가 수정할 부분 있으면 말해줘!
