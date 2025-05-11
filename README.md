# video_div (Video Splitter / 동영상 분할 프로그램)

A GUI-based application developed in Python using Tkinter, designed to split video files into smaller segments based on user-specified file sizes. This tool utilizes FFmpeg for the core video processing tasks.

## Functionality and Purpose

This program is a GUI-based video splitting application. Users can perform the following functions through this app:

* **Select Video File:** Users can browse and select a video file they wish to split.
* **Specify Split Size:** Input the desired size for each split segment (e.g., 1 GB, 700 MB). Units can be selected as GB or MB.
* **Specify Output Directory:** Choose a folder where the split video segments will be saved.
* **FFmpeg Path Configuration (Optional):**
    * The application attempts to use FFmpeg from the system's PATH.
    * Users can specify a custom path to the FFmpeg executable folder if it's not in the PATH or if a specific version needs to be used. This path is saved for future sessions.
* **Video Splitting:** The program calculates the number of segments based on the original video's duration and the target segment size. It then uses FFmpeg to split the video into parts.
* **No Re-encoding (`-c copy`):** Splits are performed by copying the original video and audio streams without re-encoding, ensuring fast processing and no quality loss. The actual segment sizes might slightly vary due to this method, as splits occur at keyframes.

This app is useful for breaking down large video files into more manageable pieces, for example, for easier sharing, storage, or to bypass file size limits on certain platforms.

## Prerequisites

Before using this application, ensure you have the following:

1.  **FFmpeg:** This program **requires** FFmpeg to be installed on your system.
    * Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
    * Ensure that the FFmpeg executable is either in your system's PATH environment variable, or you provide the path to its directory within the application.
2.  **Python (for running the script directly):** If you intend to run the Python script (`.py`), you'll need Python 3.x installed. Tkinter is usually included with standard Python installations.

## How to Use

There are two ways to use this application:

**A. Using the Executable (`.exe` file - Recommended for most users):**

1.  Download the latest `.exe` file from the **[Releases](https://github.com/nopigom119/video_div/releases)** page of this repository.
2.  Ensure FFmpeg is installed and accessible (see Prerequisites). If FFmpeg is not in your system PATH, you can either:
    * Place the `ffmpeg.exe` (and other necessary FFmpeg files like `ffprobe.exe`) in the same directory as the `vidoe_div.exe`.
    * Or, specify the path to the FFmpeg installation folder within the application itself.
3.  Run the `vidoe_div.exe` file.
4.  **FFmpeg Path (Optional but Recommended):**
    * The application will try to find FFmpeg automatically.
    * If you have FFmpeg in a custom location, click the "Browse" button next to "FFmpeg Path" and select the folder containing `ffmpeg.exe`. This path will be saved for future use.
5.  **Select Video File:** Click the "Browse" button next to "Video File" to choose the video you want to split.
6.  **Set Split Size:** Enter the desired numerical size for each segment in the "Split Size" field and select the unit (GB or MB) from the dropdown menu.
7.  **Select Output Directory:** Click "Browse" (usually prompted after clicking "Start Splitting") to choose where the split files will be saved.
8.  **Start Splitting:** Click the "Start Splitting" button.
9.  Wait for the process to complete. A message will inform you upon completion or if an error occurs.

**B. Running the Python Script (`.py` file):**

1.  Clone this repository or download the `.py` script.
2.  Ensure Python 3.x and FFmpeg are installed (see Prerequisites).
3.  Open a terminal or command prompt.
4.  Navigate to the directory where you saved the script.
5.  Run the script using the command: `python vidoe_div.py`
6.  Follow steps 4-9 from the "Using the Executable" section above.

## License

This program is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**.

* **Attribution:** You must give appropriate credit, provide a link to the license, and indicate if changes were made.
* **Non-Commercial Use:** You may not use this program for commercial purposes.
* **Modification Allowed:** You can modify this program or create derivative works.
* **Same Conditions for Change Permission:** If you modify or create derivative works of this program, you must distribute your contributions under the same license as the original.

You can check the license details on the Creative Commons website: [https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)

## Contact

For inquiries about this program, please contact [rycbabd@gmail.com].

---

# video_div (동영상 분할 프로그램)

Tkinter를 사용하여 Python으로 개발된 GUI 기반 애플리케이션으로, 사용자가 지정한 파일 크기에 따라 동영상 파일을 작은 세그먼트로 분할하도록 설계되었습니다. 이 도구는 핵심 비디오 처리 작업을 위해 FFmpeg를 활용합니다.

## 기능 및 목적

본 프로그램은 GUI 기반의 동영상 분할 애플리케이션입니다. 사용자는 이 앱을 통해 다음과 같은 기능을 수행할 수 있습니다.

* **동영상 파일 선택:** 사용자는 분할하려는 동영상 파일을 찾아 선택할 수 있습니다.
* **분할 크기 지정:** 각 분할된 세그먼트에 대해 원하는 크기(예: 1GB, 700MB)를 입력합니다. 단위는 GB 또는 MB로 선택할 수 있습니다.
* **출력 디렉토리 지정:** 분할된 동영상 세그먼트가 저장될 폴더를 선택합니다.
* **FFmpeg 경로 설정 (선택 사항):**
    * 애플리케이션은 시스템의 PATH에서 FFmpeg를 사용하려고 시도합니다.
    * PATH에 없거나 특정 버전을 사용해야 하는 경우 사용자가 FFmpeg 실행 파일이 있는 폴더의 사용자 지정 경로를 지정할 수 있습니다. 이 경로는 다음 세션을 위해 저장됩니다.
* **동영상 분할:** 프로그램은 원본 동영상의 길이와 목표 세그먼트 크기를 기준으로 세그먼트 수를 계산합니다. 그런 다음 FFmpeg를 사용하여 동영상을 부분으로 분할합니다.
* **재인코딩 없음 (`-c copy`):** 원본 비디오 및 오디오 스트림을 재인코딩하지 않고 복사하여 분할이 수행되므로 빠른 처리와 품질 손실이 없습니다. 이 방법으로 인해 분할이 키프레임에서 발생하므로 실제 세그먼트 크기는 약간 다를 수 있습니다.

이 앱은 대용량 동영상 파일을 공유, 저장 또는 특정 플랫폼의 파일 크기 제한을 우회하기 쉬운 더 관리하기 쉬운 조각으로 나누는 데 유용합니다.

## 사전 준비 사항

이 애플리케이션을 사용하기 전에 다음 사항을 확인하십시오.

1.  **FFmpeg:** 이 프로그램은 시스템에 FFmpeg가 설치되어 있어야 **필수적으로** 작동합니다.
    * FFmpeg 다운로드: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
    * FFmpeg 실행 파일이 시스템의 PATH 환경 변수에 있거나, 애플리케이션 내에서 해당 디렉토리 경로를 제공해야 합니다.
2.  **Python (스크립트 직접 실행 시):** Python 스크립트(`.py`)를 직접 실행하려면 Python 3.x 버전이 설치되어 있어야 합니다. Tkinter는 일반적으로 표준 Python 설치에 포함되어 있습니다.

## 사용 방법

이 애플리케이션을 사용하는 방법에는 두 가지가 있습니다.

**A. 실행 파일 (`.exe` 파일 사용 - 대부분 사용자에게 권장):**

1.  이 저장소의 **[Releases](https://github.com/nopigom119/video_div/releases)** 페이지에서 최신 `.exe` 파일을 다운로드합니다.
2.  FFmpeg가 설치되어 있고 접근 가능한지 확인합니다 (사전 준비 사항 참조). FFmpeg가 시스템 PATH에 없는 경우 다음 중 하나를 수행할 수 있습니다.
    * `ffmpeg.exe` (및 `ffprobe.exe`와 같은 기타 필요한 FFmpeg 파일)를 `vidoe_div.exe`와 동일한 디렉토리에 배치합니다.
    * 또는 애플리케이션 자체 내에서 FFmpeg 설치 폴더 경로를 지정합니다.
3.  `vidoe_div.exe` 파일을 실행합니다.
4.  **FFmpeg 경로 (선택 사항이지만 권장):**
    * 애플리케이션이 FFmpeg를 자동으로 찾으려고 시도합니다.
    * FFmpeg가 사용자 지정 위치에 있는 경우 "FFmpeg 경로" 옆의 "찾아보기" 버튼을 클릭하고 `ffmpeg.exe`가 포함된 폴더를 선택합니다. 이 경로는 나중에 사용할 수 있도록 저장됩니다.
5.  **동영상 파일 선택:** "동영상 파일" 옆의 "찾아보기" 버튼을 클릭하여 분할할 동영상을 선택합니다.
6.  **분할 크기 설정:** "분할 크기" 필드에 각 세그먼트에 대해 원하는 숫자 크기를 입력하고 드롭다운 메뉴에서 단위(GB 또는 MB)를 선택합니다.
7.  **출력 디렉토리 선택:** ("분할 시작" 클릭 후 프롬프트가 표시됨) 분할된 파일이 저장될 위치를 선택하려면 "찾아보기"를 클릭합니다.
8.  **분할 시작:** "분할 시작" 버튼을 클릭합니다.
9.  프로세스가 완료될 때까지 기다립니다. 완료 시 또는 오류 발생 시 메시지가 표시됩니다.

**B. Python 스크립트 (`.py` 파일 실행):**

1.  이 저장소를 복제하거나 `.py` 스크립트를 다운로드합니다.
2.  Python 3.x 및 FFmpeg가 설치되어 있는지 확인합니다 (사전 준비 사항 참조).
3.  터미널 또는 명령 프롬프트를 엽니다.
4.  스크립트를 저장한 디렉토리로 이동합니다.
5.  명령을 사용하여 스크립트를 실행합니다: `python vidoe_div.py`
6.  위의 "실행 파일 사용" 섹션의 4-9단계를 따릅니다.

## 라이선스

본 프로그램은 **크리에이티브 커먼즈 저작자표시-비영리-동일조건변경허락 4.0 국제 라이선스 (CC BY-NC-SA 4.0)** 에 따라 이용할 수 있습니다.

* **출처 표시:** 본 프로그램의 출처 (작성자 또는 개발팀)를 명시해야 합니다.
* **비상업적 이용:** 본 프로그램을 상업적인 목적으로 이용할 수 없습니다.
* **변경 가능:** 본 프로그램을 수정하거나 2차 저작물을 만들 수 있습니다.
* **동일 조건 변경 허락:** 2차 저작물에 대해서도 동일한 조건으로 이용 허락해야 합니다.

자세한 내용은 크리에이티브 커먼즈 홈페이지에서 확인하실 수 있습니다: [https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ko](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ko)

## 문의

본 프로그램에 대한 문의사항은 [rycbabd@gmail.com] 로 연락주시기 바랍니다.
