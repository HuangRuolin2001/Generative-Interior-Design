import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

# 加载CLIP模型和处理器
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")


def compute_clip_similarity(image_path, text_input):
    """
    计算图像与文本的CLIP相似度
    :param image_path: 图像路径（本地文件）
    :param text_input: 文本描述
    :return: 相似度分数（0~1之间）
    """
    image = Image.open(image_path).convert("RGB")
    inputs = processor(text=[text_input], images=image, return_tensors="pt", padding=True)

    with torch.no_grad():
        outputs = model(**inputs)
        image_embeds = outputs.image_embeds
        text_embeds = outputs.text_embeds

        # 归一化
        image_embeds /= image_embeds.norm(dim=-1, keepdim=True)
        text_embeds /= text_embeds.norm(dim=-1, keepdim=True)

        # 计算cosine相似度
        similarity = torch.matmul(image_embeds, text_embeds.T).item()
        return similarity



# 示例用法
image_path = "C:\\Users\\lzx\\Desktop\\01.png"  # 替换成你的图片路径
text_description = "A simple, practical, and cozy children's bedroom for everyday use. The walls are painted in light tones, and the furniture features clean, minimalist lines. There is a pink children's bed, a large wardrobe with ample storage space, a child-sized desk, and a comfortable chair. The floor is finished in a light color to maintain a bright and airy atmosphere."  # 替换成你的文本描述

score = compute_clip_similarity(image_path, text_description)
print(f"CLIP 相似度分数: {score:.4f}")
