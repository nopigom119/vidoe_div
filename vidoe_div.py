import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox
import os
import subprocess
import json  # 동영상 정보 파싱을 위해 추가
import re

# FFmpeg 경로를 저장할 파일 이름
FFMPEG_PATH_FILE = "ffmpeg_path.txt"

def load_ffmpeg_path():
    if os.path.exists(FFMPEG_PATH_FILE):
        with open(FFMPEG_PATH_FILE, "r") as f:
            return f.readline().strip()
    return ""

def save_ffmpeg_path(path):
    with open(FFMPEG_PATH_FILE, "w") as f:
        f.write(path)

def browse_ffmpeg_path():
    folder_path = filedialog.askdirectory(title="FFmpeg 실행 파일이 있는 폴더 선택")
    if folder_path:
        ffmpeg_path_entry.delete(0, tk.END)
        ffmpeg_path_entry.insert(0, folder_path)
        save_ffmpeg_path(folder_path)

def get_ffmpeg_command(ffmpeg_dir):
    ffmpeg_executable = "ffmpeg"
    if ffmpeg_dir:
        ffmpeg_executable = os.path.join(ffmpeg_dir, "ffmpeg")
        if os.name == 'nt':  # Windows
            ffmpeg_executable += ".exe"
    return [ffmpeg_executable]

def get_video_info(video_path, ffmpeg_command):
    """FFmpeg을 사용하여 동영상 정보를 가져옵니다 (stderr 파싱)."""
    try:
        command = ffmpeg_command + [
            '-i', video_path
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=False, encoding='utf-8', errors='surrogateescape') # 오류 코드를 체크하지 않음

        stderr_output = result.stderr
        duration_match = re.search(r"Duration: (\d{2}:\d{2}:\d{2}\.\d{2})", stderr_output)
        if duration_match:
            duration_str = duration_match.group(1)
            # HH:MM:SS.ms 형태를 초 단위로 변환
            parts = duration_str.split(':')
            hours = int(parts[0])
            minutes = int(parts[1])
            seconds_ms = float(parts[2])
            total_seconds = hours * 3600 + minutes * 60 + seconds_ms
            return {'format': {'duration': str(total_seconds)}}
        else:
            messagebox.showerror("오류", "동영상 길이를 찾을 수 없습니다.")
            return None

    except FileNotFoundError:
        messagebox.showerror("오류", "FFmpeg을 찾을 수 없습니다.")
        return None
    except Exception as e:
        messagebox.showerror("오류", f"알 수 없는 오류 발생 (get_video_info):\n파일: {video_path}\n오류: {e}")
        return None
    
def split_video(video_path, split_size_gb, output_dir, ffmpeg_dir=""):
    """FFmpeg을 사용하여 동영상을 지정된 크기로 분할합니다 (시간 기반)."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_name, file_ext = os.path.splitext(os.path.basename(video_path))
    split_size_bytes = int(split_size_gb * 1024 * 1024 * 1024)  # GB를 바이트로 변환

    ffmpeg_command = get_ffmpeg_command(ffmpeg_dir)
    video_info = get_video_info(video_path, ffmpeg_command)

    if not video_info or 'format' not in video_info or 'duration' not in video_info['format']:
        messagebox.showerror("오류", "동영상 정보를 가져올 수 없습니다.")
        return

    total_duration_seconds = float(video_info['format']['duration'])
    total_size_bytes = os.path.getsize(video_path)

    if split_size_bytes <= 0:
        messagebox.showerror("오류", "분할 크기는 0보다 커야 합니다.")
        return

    num_segments = int(total_size_bytes / split_size_bytes)
    if total_size_bytes % split_size_bytes != 0:
        num_segments += 1

    if num_segments <= 1:
        messagebox.showinfo("알림", "분할할 필요가 없습니다.")
        return

    segment_duration_seconds = total_duration_seconds / num_segments

    try:
        for i in range(num_segments):
            start_time = i * segment_duration_seconds
            output_file = os.path.join(output_dir, f"{file_name}_part_{i+1}{file_ext}")
            command = ffmpeg_command + [
                '-i', video_path,
                '-ss', str(start_time),
                '-to', str(start_time + segment_duration_seconds),
                '-c', 'copy',
                output_file
            ]
            subprocess.run(command, check=True, capture_output=True, encoding='utf-8', errors='surrogateescape')

        messagebox.showinfo("완료", f"'{os.path.basename(video_path)}' 파일이 {split_size_gb}GB 단위로 (대략적으로) 분할되어 '{output_dir}'에 저장되었습니다.")

    except subprocess.CalledProcessError as e:
        stderr_utf8 = e.stderr.decode('utf-8', errors='surrogateescape')
        messagebox.showerror("오류", f"동영상 분할 중 오류 발생:\n파일: {video_path}\n명령: {' '.join(command)}\n오류:\n{stderr_utf8}")
    except FileNotFoundError:
        messagebox.showerror("오류", "FFmpeg을 찾을 수 없습니다. 시스템 PATH에 등록되어 있거나, FFmpeg 경로를 지정해주세요.")
    except Exception as e:
        messagebox.showerror("오류", f"알 수 없는 오류 발생 (split_video):\n파일: {video_path}\n오류: {e}")

def browse_file():
    file_path = filedialog.askopenfilename(
        title="동영상 파일 선택",
        filetypes=(("동영상 파일", "*.mp4;*.avi;*.mkv;*.mov;*.wmv"), ("모든 파일", "*.*"))
    )
    if file_path:
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, file_path)

def start_splitting():
    video_path = file_path_entry.get()
    split_size_str = size_entry.get()
    unit = unit_combobox.get()
    ffmpeg_dir = ffmpeg_path_entry.get()

    if not video_path:
        messagebox.showerror("오류", "동영상 파일을 선택해주세요.")
        return

    if not split_size_str:
        messagebox.showerror("오류", "분할할 크기를 입력해주세요.")
        return

    try:
        split_size = float(split_size_str)
        if unit == "MB":
            split_size_gb = split_size / 1024
        elif unit == "GB":
            split_size_gb = split_size
        else:
            messagebox.showerror("오류", "올바른 용량 단위를 선택해주세요.")
            return

        if split_size_gb <= 0:
            messagebox.showerror("오류", "분할 크기는 0보다 커야 합니다.")
            return

        output_dir = filedialog.askdirectory(title="저장할 폴더 선택")
        if output_dir:
            split_video(video_path, split_size_gb, output_dir, ffmpeg_dir)

    except ValueError:
        messagebox.showerror("오류", "분할 크기는 숫자로 입력해야 합니다.")
    except Exception as e:
        messagebox.showerror("오류", f"오류 발생: {e}")

# 메인 윈도우 생성
root = tk.Tk()
root.title("동영상 분할 프로그램")

# FFmpeg 경로 설정
ffmpeg_path_label = tk.Label(root, text="FFmpeg 경로 (선택):")
ffmpeg_path_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

ffmpeg_path_entry = tk.Entry(root, width=50)
ffmpeg_path_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
ffmpeg_path_entry.insert(0, load_ffmpeg_path())  # 저장된 경로 로드

browse_ffmpeg_button = tk.Button(root, text="찾아보기", command=browse_ffmpeg_path)
browse_ffmpeg_button.grid(row=3, column=2, padx=10, pady=10, sticky="e")

# 파일 경로 선택
file_path_label = tk.Label(root, text="동영상 파일:")
file_path_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

file_path_entry = tk.Entry(root, width=50)
file_path_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

browse_button = tk.Button(root, text="찾아보기", command=browse_file)
browse_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")

# 분할 크기 입력
size_label = tk.Label(root, text="분할 크기:")
size_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

size_entry = tk.Entry(root, width=10)
size_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

unit_values = ["GB", "MB"]
unit_combobox = Combobox(root, values=unit_values, width=5)
unit_combobox.set("GB")  # 기본 단위 설정
unit_combobox.grid(row=1, column=1, padx=(70, 10), pady=10, sticky="w")

unit_label = tk.Label(root, text="단위:")
unit_label.grid(row=1, column=1, padx=(40, 10), pady=10, sticky="w")

# 분할 시작 버튼
split_button = tk.Button(root, text="분할 시작", command=start_splitting)
split_button.grid(row=4, column=0, columnspan=3, padx=10, pady=20)

# Grid 레이아웃 설정 (창 크기 조절 시 위젯도 함께 조절되도록)
root.grid_columnconfigure(1, weight=1)

root.mainloop()