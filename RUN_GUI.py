import gradio as gr
import cv2
import numpy as np
from PIL import Image
import json
import webbrowser
import os
import sys

# 设置工作目录为脚本所在目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 设置文件系统编码
if sys.platform.startswith('win'):
    import locale
    locale.setlocale(locale.LC_ALL, 'C')

# 导入卦象解释的JSON数据
try:
    with open('gua_interpretations.json', 'r', encoding='utf-8') as f:
        gua_interpretations = json.load(f)
except FileNotFoundError:
    print("错误：找不到 'gua_interpretations.json' 文件。请确保该文件在脚本同一目录下。")
    sys.exit(1)
except json.JSONDecodeError:
    print("错误：'gua_interpretations.json' 文件格式不正确。请检查JSON格式。")
    sys.exit(1)

# 六十四卦对应表
gua_dict = {
    '000000': '坤', '000001': '剥', '000010': '比', '000011': '观', '000100': '豫', '000101': '晋', '000110': '萃', '000111': '否',
    '001000': '谦', '001001': '艮', '001010': '蹇', '001011': '渐', '001100': '小过', '001101': '旅', '001110': '咸', '001111': '遁',
    '010000': '师', '010001': '蒙', '010010': '坎', '010011': '涣', '010100': '解', '010101': '未济', '010110': '困', '010111': '讼',
    '011000': '升', '011001': '蛊', '011010': '井', '011011': '巽', '011100': '恒', '011101': '鼎', '011110': '大过', '011111': '姤',
    '100000': '复', '100001': '颐', '100010': '屯', '100011': '益', '100100': '震', '100101': '噬嗑', '100110': '随', '100111': '无妄',
    '101000': '明夷', '101001': '贲', '101010': '离', '101011': '革', '101100': '丰', '101101': '家人', '101110': '睽', '101111': '同人',
    '110000': '临', '110001': '损', '110010': '节', '110011': '中孚', '110100': '归妹', '110101': '睽', '110110': '兑', '110111': '履',
    '111000': '泰', '111001': '大畜', '111010': '需', '111011': '小畜', '111100': '大壮', '111101': '大有', '111110': '夬', '111111': '乾'
}

def resize_image(image, max_size=512):
    # 将numpy数组转换为PIL Image对象
    img = Image.fromarray(image)
    # 获取原始尺寸
    width, height = img.size
    # 计算缩放比例
    scale = max_size / max(width, height)
    # 计算新的尺寸
    new_width = int(width * scale)
    new_height = int(height * scale)
    # 缩放图像
    resized_img = img.resize((new_width, new_height), Image.LANCZOS)
    # 将PIL Image对象转换回numpy数组
    return np.array(resized_img)

def analyze_image(image):
    # 缩放图像
    resized_image = resize_image(image)
    
    # 将图像分割成六份
    img = Image.fromarray(resized_image)
    width, height = img.size
    piece_height = height // 6
    pieces = [img.crop((0, i * piece_height, width, (i + 1) * piece_height)) for i in range(6)]

    binary_digits = []
    for piece in pieces:
        # 转换为灰度图像
        gray_piece = piece.convert("L")
        # 转换为二值图像
        bw_piece = gray_piece.point(lambda x: 0 if x < 128 else 255, '1')
        # 计算黑色色块的数量
        bw_array = np.array(bw_piece)
        black_count = np.sum(bw_array == 0)
        # 根据黑色色块的奇偶数生成二进制数字
        binary_digits.append('1' if black_count % 2 == 1 else '0')

    binary_string = ''.join(binary_digits)
    gua = gua_dict.get(binary_string, "未知卦象")
    
    # 获取卦象解释
    interpretation = gua_interpretations.get(binary_string, {"name": "未知", "description": "无法解释"})
    
    result = f"卦象: {gua} ({binary_string})\n"
    result += f"解释: {interpretation['name']} - {interpretation['description']}"
    
    return result

iface = gr.Interface(
    fn=analyze_image,
    inputs=gr.Image(type="numpy", label="上传图片"),
    outputs="text",
    title="卦象分析",
    description="上传一张图片，分析其卦象及其含义。支持各种常见图片格式，图片会自动调整大小。"
)

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:7860")
    iface.launch()
