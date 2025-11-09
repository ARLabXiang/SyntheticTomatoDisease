---
title: "Synthetic Tomato Dataset"
---
## Abstract
<div style="overflow:auto; margin:1em 0;">
<img src="/assets/figs/visuals_gimp.png" 
       alt="My Figure Description" 
       style="float: right; width: 40%; margin-left: 20px; margin-bottom: 10px; border-radius: 20px;">

    <p> Plant diseases cause significant global yield losses,
 estimated at around 20% for many crops. Early detection and
 continuous monitoring are critical for implementing timely crop
 protection practices to mitigate losses. Advances in agricultural
 robotics may enable high-throughput, autonomous field monitoring. 
 However, most existing disease datasets consist of close-up
 images collected under controlled conditions for manual diagnosis, 
 resulting in models to generalize poorly to robotic platforms
 with wider field imagery for high-throughput disease monitoring.</p>
 
 <p>To address this limitation, this work presents large, high-fidelity
 3D synthetic tomato field datasets and a data generator based on
 Unreal Engine 5. The framework incorporates a novel parameterized 
 texture overlay function and preprocessing models to adapt
 public tomato disease textures to generate diverse yet realistic 
 disease features within the simulation. We conduct a comprehensive
 sim-to-real transfer analysis, transferring from our synthetic data
 to public tomato disease datasets and unlabeled field imagery.</p>
 
 <p>
 Experimental results show that models trained on our synthetic
 dataset exhibit superior generalization to out-of-distribution real
world data, improving tomato disease detection by 2.54 IoU
 over PlantSeg, fruit detection by 7.36 IoU over ACOD-12K, and
 significantly improving stereo matching quality under low-light
 and dense plant canopy. With unsupervised domain adaptation,
 our dataset achieves performance comparable to manual labels
 in 95th percentile Hausdorff distances.</p>

</div>

## Simulator



## Datasets



## Applications