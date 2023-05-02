import moviepy.editor as mp
from moviepy.audio.AudioClip import AudioArrayClip
import noisereduce as nr
import numpy as np
import sys

def remove_noise(input_file, output_file):
    # 从输入文件中加载音频和视频
    video = mp.VideoFileClip(input_file)
    audio = video.audio

    # 将音频转换为numpy数组
    audio_samples = audio.to_soundarray()

    # 获取音频的采样率
    sample_rate = audio.fps

    # 对于立体声音频，处理每个通道
    if audio_samples.ndim == 2:
        reduced_noise_samples = np.zeros_like(audio_samples)
        for channel in range(audio_samples.shape[1]):
            reduced_noise_samples[:, channel] = nr.reduce_noise(y=audio_samples[:, channel], sr=sample_rate, prop_decrease=1.0)
    else:
        reduced_noise_samples = nr.reduce_noise(y=audio_samples, sr=sample_rate, prop_decrease=1.0)

    # 创建一个新的音频剪辑，并使用去噪后的样本替换原始音频
    new_audio = AudioArrayClip(reduced_noise_samples, audio.fps)

    # 将去噪后的音频与原始视频结合
    new_video = video.set_audio(new_audio)

    # 保存输出文件
    new_video.write_videofile(output_file, codec="libx264", audio_codec="aac")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_noise.py input.mp4 output.mp4")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        remove_noise(input_file, output_file)
