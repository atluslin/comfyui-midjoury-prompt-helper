
import json
import os

def read_json_file(file_path):
    try:
        # 读取json文件
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            return json_data
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def get_name(json_data):
    # 获得文件名
    if not isinstance(json_data, list):
        print("Error: input data must be a list")
        return None

    names = []

    # Iterate over each item in the data list
    for item in json_data:
        # Check that the item is a dictionary
        if isinstance(item, dict):
            # Check that 'name' is a key in the dictionary
            if 'name' in item:
                # Append the value of 'name' to the names list
                names.append(item['name'])

    return names

def get_prompt(json_data, template_name):
    try:
        # Check if json_data is a list
        if not isinstance(json_data, list):
            raise ValueError("Invalid JSON data. Expected a list of templates.")
            
        for template in json_data:
            # Check if template contains 'name' and 'prompt' fields
            if 'name' not in template or 'prompt' not in template:
                raise ValueError("Invalid template. Missing 'name' or 'prompt' field.")
            
            if template['name'] == template_name:
                prompt = template.get('prompt', "")
                print("Extracted prompt:", prompt)
                return prompt

        # If function hasn't returned yet, no matching template was found
        raise ValueError(f"No template found with name '{template_name}'.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


class midjoury_prompt_helper:

    def __init__(self):
        pass

    @classmethod

    def INPUT_TYPES(self):
        # 获取当前目录
        p = os.path.dirname(os.path.realpath(__file__))

        # JSON文件路径
        style_file_path = os.path.join(p, 'lists/style_list.json')
        background_file_path = os.path.join(p, 'lists/background_list.json')
        theme_file_path = os.path.join(p, 'lists/theme_list.json')
        character_file_path = os.path.join(p, 'lists/character_list.json')
        color_file_path = os.path.join(p, 'lists/color_list.json')
        dynamic_file_path = os.path.join(p, 'lists/dynamic_list.json')
        layout_file_path = os.path.join(p, 'lists/layout_list.json')
        material_file_path = os.path.join(p, 'lists/material_list.json')
        viewport_file_path = os.path.join(p, 'lists/viewport_list.json')
        light_file_path = os.path.join(p, 'lists/light_list.json')
        aspect_file_path = os.path.join(p, 'lists/aspect_list.json')
        version_file_path = os.path.join(p, 'lists/version_list.json')

        # 读取JSON文件
        self.style_data = read_json_file(style_file_path)
        self.background_data = read_json_file(background_file_path)
        self.theme_data = read_json_file(theme_file_path)
        self.character_data = read_json_file(character_file_path)
        self.color_data = read_json_file(color_file_path)
        self.dynamic_data = read_json_file(dynamic_file_path)
        self.layout_data = read_json_file(layout_file_path)
        self.material_data = read_json_file(material_file_path)
        self.viewport_data = read_json_file(viewport_file_path)
        self.light_data = read_json_file(light_file_path)
        self.aspect_data = read_json_file(aspect_file_path)
        self.version_data = read_json_file(version_file_path)

        # Json数据加空和随机选项
        style_list = get_name(self.style_data)
        style_list = ['无', '随机'] + style_list
        background_list = get_name(self.background_data)
        background_list = ['无', '随机'] + background_list
        theme_list = get_name(self.theme_data)
        theme_list = ['无', '随机'] + theme_list
        character_list = get_name(self.character_data)
        character_list = ['无', '随机'] + character_list
        color_list = get_name(self.color_data)
        color_list = ['无', '随机'] + color_list
        dynamic_list = get_name(self.dynamic_data)
        dynamic_list = ['无', '随机'] + dynamic_list
        layout_list = get_name(self.layout_data)
        layout_list = ['无', '随机'] + layout_list
        material_list = get_name(self.material_data)
        material_list = ['无', '随机'] + material_list
        viewport_list = get_name(self.viewport_data)
        viewport_list = ['无', '随机'] + viewport_list
        light_list = get_name(self.light_data)
        light_list = ['无', '随机'] + light_list
        aspect_list = get_name(self.aspect_data)
        aspect_list = ['无', '随机'] + aspect_list
        version_list = get_name(self.version_data)
        version_list = ['无', '随机'] + version_list

        
        
        #max_float_value = 1.75

        return {
            "required": {
                "起始提示词": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "风格": (style_list, {
                    "default": style_list[0],
                }),
                "背景": (background_list, {
                    "default": background_list[0],
                }),
                "主题": (theme_list, {
                    "default": theme_list[0],
                }),
                "角色": (character_list, {
                    "default": character_list[0],
                }),
                "色彩": (color_list, {
                    "default": color_list[0],
                }),
                "动态": (dynamic_list, {
                    "default": dynamic_list[0],
                }),
                "构图": (layout_list, {
                    "default": layout_list[0],
                }),
                "材质": (material_list, {
                    "default": material_list[0],
                }),
                "视角": (viewport_list, {
                    "default": viewport_list[0],
                }),
                "照明": (light_list, {
                    "default": light_list[0],
                }),
                "画幅比例": (aspect_list, {
                    "default": aspect_list[0],
                }),
                "模型版本": (version_list, {
                    "default": version_list[0],
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("提示词文本", )
    FUNCTION = "mjp"
    CATEGORY = '🔥🔥🔥ljeasynode🔥🔥🔥/Midjoury提示词助手'

    def mjp(self, 起始提示词="", 风格="",背景="",主题="",角色="",色彩="",动态="",构图="",材质="",视角="",照明="",画幅比例="",模型版本=""):
        import random
        
        def get_random_prompt(data):
            names = get_name(data)
            if names:
                return get_prompt(data, random.choice(names))
            return ""
            
        style = get_random_prompt(self.style_data) if 风格 == "随机" else get_prompt(self.style_data, 风格)
        background = get_random_prompt(self.background_data) if 背景 == "随机" else get_prompt(self.background_data, 背景)
        theme = get_random_prompt(self.theme_data) if 主题 == "随机" else get_prompt(self.theme_data, 主题)
        character = get_random_prompt(self.character_data) if 角色 == "随机" else get_prompt(self.character_data, 角色)
        color = get_random_prompt(self.color_data) if 色彩 == "随机" else get_prompt(self.color_data, 色彩)
        dynamic = get_random_prompt(self.dynamic_data) if 动态 == "随机" else get_prompt(self.dynamic_data, 动态)
        layout = get_random_prompt(self.layout_data) if 构图 == "随机" else get_prompt(self.layout_data, 构图)
        material = get_random_prompt(self.material_data) if 材质 == "随机" else get_prompt(self.material_data, 材质)
        viewport = get_random_prompt(self.viewport_data) if 视角 == "随机" else get_prompt(self.viewport_data, 视角)
        light = get_random_prompt(self.light_data) if 照明 == "随机" else get_prompt(self.light_data, 照明)
        aspect = get_random_prompt(self.aspect_data) if 画幅比例 == "随机" else get_prompt(self.aspect_data, 画幅比例)
        version = get_random_prompt(self.version_data) if 模型版本 == "随机" else get_prompt(self.version_data, 模型版本)
        
        prompt = []
        
        if 起始提示词 != "":
            prompt.append(f"{起始提示词}")
        
        if 风格 == "无":
            风格 = ""
        else:
            prompt.append(f"{style}")
        
        if 背景 == "无":
            背景 = ""
        else:
            prompt.append(f"{background}")
        
        if 主题 == "无":
            主题 = ""
        else:
            prompt.append(f"{theme}")
        
        if 角色 == "无":
            角色 = ""
        else:
            prompt.append(f"{character}")

        if 色彩 == "无":
            色彩 = ""
        else:
            prompt.append(f"{color}")

        if 动态 == "无":
            动态 = ""
        else:
            prompt.append(f"{dynamic}")
        
        if 构图 == "无":
            构图 = ""
        else:
            prompt.append(f"{layout}")
       
        if 材质 == "无":
            材质 = ""
        else:
            prompt.append(f"{material}")

        if 视角 == "无":
            视角 = ""
        else:
            prompt.append(f"{viewport}")
        
        if 照明 == "无":
            照明 = ""
        else:
            prompt.append(f"{light}")
        
        if 画幅比例 == "无":
            画幅比例 = ""
        else:
            prompt.append(f"{aspect}")
        
        if 模型版本 == "无":
            模型版本 = ""
        else:
            prompt.append(f"{version}")

        prompt = ", ".join(prompt)
        prompt = prompt.lower()

        
        print("Midjoury ptompt helper as generate the prompt:")
        print(prompt)

        return (prompt,)



NODE_CLASS_MAPPINGS = {
    "Midjoury提示词助手": midjoury_prompt_helper
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Midjoury提示词助手": "Midjoury提示词助手"
}
