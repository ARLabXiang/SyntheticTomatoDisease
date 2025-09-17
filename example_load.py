from datasets import load_dataset
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
# similar to cityscapes for mmsegmentation
# class name, (new_id, img_id)
semantic_map = {
                "bacterial_spot":       (0, 5),
                "early_blight":         (1, 10),
                "late_blight":          (2, 20),
                "leaf_mold":            (3, 25),
                "septoria_leaf_spot":   (4,30),
                "spider_mites":         (5,35),
                "target_spot":          (6,40),
                "mosaic_virus":         (7,45),
                "yellow_leaf_curl_virus":(8,50),
                "healthy_leaf_pv":      (9, 15),  # plant village healthy leaf
                "healthy_leaf_t":       (9, 255), # texture leaf (healthy)
                "background":           (10, 0),
                "tomato":               (11, 121),
                "stem":                 (12, 111),
                "wood_rod":             (13, 101),
                "red_band":             (14, 140),
                "yellow_flower":        (15, 131)
                }

def maj_vote(img,x,y,n=3):
    half = n // 2
    x_min, x_max = max(0, x - half), min(img.shape[1], x + half + 1)
    y_min, y_max = max(0, y - half), min(img.shape[0], y + half + 1)
    
    window = img[y_min:y_max, x_min:x_max].flatten()
    window = window[window != 255]
    
    if len(window) > 0:
        # Perform majority voting
        most_common_label = stats.mode(window, keepdims=True)[0][0]
        return most_common_label
    else:
        return semantic_map["background"][0]
    
def color_to_id(img_semantic, top_k_disease = 10, semantic_map = semantic_map):
    semantic_id_img = np.ones(img_semantic.shape) * 255
    disease_counts = []
    # remap rendered color to semantic id
    for _, id_value_map in semantic_map.items():
        # track disease pixel counts for top_k_disease filtering
        if id_value_map[1] < 60 and id_value_map[1] > 1:        
            disease_counts.append(np.sum(np.where(img_semantic == id_value_map[1], 1, 0)))
        semantic_id_img[img_semantic == id_value_map[1]] = id_value_map[0]
    # filter for most common disease labels
    for i, item_i in enumerate(np.argsort(disease_counts)[::-1]):
        if i >= top_k_disease:
            id_value_map = list(semantic_map.items())[item_i][1]
            semantic_id_img[img_semantic == id_value_map[1]] = 255
            
    # Apply majority voting for unlabeled pixels (needed as the rendering process can blend pixels)
    unknown_mask = (semantic_id_img == 255)
    for y,x in np.argwhere(unknown_mask):
        semantic_id_img[y, x] = maj_vote(semantic_id_img, x, y, 3)
    return semantic_id_img


dataset = load_dataset("xingjianli/tomatotest", 'sample',trust_remote_code=True, num_proc=4)
print(dataset["train"][0])


left_rgb_img = dataset["train"][0]['left_rgb']
right_rgb_img = dataset["train"][0]['right_rgb']
left_semantic_img = np.asarray(dataset["train"][0]['left_semantic'])
left_instance_img = np.asarray(dataset["train"][0]['left_instance'])
left_depth_img = np.asarray(dataset["train"][0]['left_depth'])
right_depth_img = np.asarray(dataset["train"][0]['right_depth'])
plt.subplot(231)
plt.imshow(left_rgb_img)
plt.subplot(232)
plt.imshow(right_rgb_img)
plt.subplot(233)
plt.imshow(color_to_id(left_semantic_img))
plt.subplot(234)
plt.imshow(np.where(left_depth_img>500,0,left_depth_img))
plt.subplot(235)
plt.imshow(np.where(right_depth_img>500,0,right_depth_img))
plt.subplot(236)
plt.imshow(left_instance_img)
plt.show()


