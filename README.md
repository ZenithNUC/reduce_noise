# reduce_noise

这个Python脚本可以帮助你去除MP4视频文件中的电流声。它使用`moviepy`库来处理视频和音频，以及`noisereduce`库来消除噪音。

This Python script can help you to reduce the noise in MP4 video file. It use the `moivepy` lib to process the video and audio, and use the `noisereduce` to reduce the noise.

## 克隆仓库

1. 克隆仓库 (Clone the repository)

```bash
git clone git@github.com:ZenithNUC/reduce_noise.git
```

2. 进入项目文件夹 (Enter the project folder)


```bash
cd ./reduce_noise
```

## 安装依赖

在运行脚本之前，请确保已经安装了`moviepy`和`noisereduce`库。可以使用以下命令进行安装：

Before you run the script, pleasure make sure that you have installed the lib of `moviepy` and `noisereduce`, you can use the command to install them.

```bash
pip install -r requirements.txt
```

或者

Or

```bash
pip install moviepy
pip install noisereduce
```

## 使用方法

执行命令

Run the command.

```bash
python remove_noise.py input.mp4 output.mp4
```

脚本会处理输入的MP4文件，并在输出文件中保存去除电流声后的版本。需要注意的是，这个脚本可能无法完全消除电流声，但它应该能大幅度降低噪音。可以需要调整脚本中的prop_decrease参数来获得更好的结果。此外，这个脚本可能会影响音频的质量，因此建议在处理后检查输出文件。

The script will process the input file and output the file had reduced noise.You must know, the script can't reduce the noise to zero.But it can reduce noise mostly. You can change the value named `prop_decrease` to achieve the best output. And the script may effect the quality of audio, so maybe you need to check the output file.

## 许可证 (License)

本项目采用 [MIT 许可证](LICENSE)。

This project is licensed under the [MIT License](LICENSE).
