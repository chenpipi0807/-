# 图像卦象分析

这是一个基于图像分析的卦象解读工具。它使用 Gradio 创建了一个简单的 Web 界面，允许用户上传图片并获得相应的卦象分析结果。


![微信截图_20241021212553](https://github.com/user-attachments/assets/2badc883-5c27-441d-813c-d1c57351e04d)
![微信截图_20241021212514](https://github.com/user-attachments/assets/41c6e558-93e6-472c-952e-e6a061b36390)
![微信截图_20241021212611](https://github.com/user-attachments/assets/4046eedb-0efc-480f-be8c-919e93960544)


## 功能

- 上传图片并自动分析其对应的卦象
- 支持各种常见图片格式
- 自动调整图片大小，确保最佳分析效果
- 提供卦象名称、二进制表示和详细解释

## 安装

1. 确保您已安装 Python 3.7 或更高版本。
2. 克隆此仓库或下载源代码。
3. 安装所需的依赖项：


## 依赖
pip install gradio opencv-python numpy pillow


## 使用方法

1. 确保 `gua_interpretations.json` 文件与 Python 脚本在同一目录下。
2. 运行 Python 脚本：RUN_GUI.py
3. 脚本将自动在默认浏览器中打开 Web 界面（地址为 http://127.0.0.1:7860）。
4. 在 Web 界面上传一张图片，然后查看分析结果。

## 注意事项

- 上传的图片会被自动调整大小，最长边将被缩放到 512 像素。
- 分析结果包括卦象名称、二进制表示和相应的解释。
- 如果遇到未知卦象，程序将返回"未知卦象"和"无法解释"。

## 贡献

欢迎提出建议和改进意见。如果您发现任何问题，请创建一个 issue 或提交一个 pull request。

## 许可

[在此处添加您的许可信息]
