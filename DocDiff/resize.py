import os
import cv2
import yaml


def pad_image(image_path, output_path):
    image = cv2.imread(image_path)
    original_height, original_width = image.shape[:2]

    # 计算较小的一边的长度，调整为8的倍数
    min_side = min(original_height, original_width)
    new_min_side = int((min_side + 7) // 8) * 8

    # 计算填充所需的差值
    delta_h = new_min_side - original_height
    delta_w = new_min_side - original_width

    # 计算填充值
    top = delta_h // 2
    bottom = delta_h - top
    left = delta_w // 2
    right = delta_w - left

    # 进行填充
    padded_image = cv2.copyMakeBorder(image, top, bottom, left, right,
                                      cv2.BORDER_CONSTANT, value=[0, 0, 0])  # 在边界填充黑色像素

    # 保存填充后的图像
    cv2.imwrite(output_path, padded_image)

    return new_min_side


# 处理的图像文件夹和输出文件夹
input_folder = '/DataA/surf23_hongbin_zhang/DocDiff/LR_input'
output_folder = '/DataA/surf23_hongbin_zhang/DocDiff/LR_input'
conf_file = 'conf.yml'

# 遍历输入文件夹中的图片并进行padding
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.png', '.jpeg')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        new_size = pad_image(input_path, output_path)
        print(f'Padded image {filename} and saved to {output_path}')

        # 更新conf.yml中的IMAGE_SIZE字段
        with open(conf_file, 'r') as f:
            conf_data = yaml.safe_load(f)

        conf_data['IMAGE_SIZE'] = [new_size, new_size]

        with open(conf_file, 'w') as f:
            yaml.dump(conf_data, f, default_flow_style=False)

        print(f'Updated IMAGE_SIZE in {conf_file} to [{new_size}, {new_size}]')
