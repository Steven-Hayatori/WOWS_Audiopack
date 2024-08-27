from pydub import AudioSegment
import os

def apply_gain_normalize_recursive(input_folder, output_folder, target_loudness):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_count = 0
    for root, dirs, files in os.walk(input_folder):
        for wav_file in files:
            if wav_file.endswith('.wav'):
                # 构建输入文件的完整路径
                input_path = os.path.join(root, wav_file)

                # 读取音频文件
                audio = AudioSegment.from_wav(input_path)

                # 应用增益效果
                audio_with_gain = audio + gain_dB

                # 归一化处理
                normalized_audio = audio_with_gain.normalize(target_loudness)

                # 构建输出文件的完整路径
                
                output_path = os.path.join(output_folder, wav_file)
                output_folder_path = os.path.dirname(output_path)
                if not os.path.exists(output_folder_path):
                    os.makedirs(output_folder_path)
                normalized_audio.export(output_path, format="wav")
                file_count += 1
    print(f'已处理 {file_count} 个文件')

if __name__ == "__main__":
    input_folder = r".\Audio_list"
    output_folder = r".\Suzakuin_tsubaki\Audio"
    gain_dB = 0  # 你可以根据需要调整增益值
    target_loudness = -5  # 你可以根据需要调整目标响度
    apply_gain_normalize_recursive(input_folder, output_folder, target_loudness)
