---
title: "Synthetic Tomato Dataset"
---
<script
  defer
  src="https://cdn.jsdelivr.net/npm/img-comparison-slider@8/dist/index.js"
></script>
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/img-comparison-slider@8/dist/styles.css"
/>

## Abstract
<div style="display: flex; flex-wrap: wrap; align-items: flex-start; gap: 20px; justify-content: flex-end; width: 100%;">
 <p style="flex: 1 1 300px; min-width: 200px;">This work presents large, high-fidelity
 3D synthetic tomato field datasets and a data generator based on
 Unreal Engine 5. The framework incorporates a novel parameterized 
 texture overlay function and preprocessing models to adapt
 public tomato disease textures to generate diverse yet realistic 
 disease features within the simulation.
 Experimental results show that models trained on our synthetic
 dataset exhibit superior generalization to out-of-distribution real
world data, improving tomato disease detection by 2.54 IoU
 over PlantSeg, fruit detection by 7.36 IoU over ACOD-12K, and
 significantly improving stereo matching quality under low-light
 and dense plant canopy. With unsupervised domain adaptation,
 our dataset achieves performance comparable to manual labels</p>
  <div style="flex: 0 0 400px; width: 100%; max-width: 400px;">
      <img slot="first" src="./assets/figs/visuals_gimp.png"
           alt="My Figure Description"
           style="border-radius: 20px;" />

  </div>



</div>

## Brief Background. 
Plant diseases cause significant global yield losses,
 estimated at around 20% for many crops. Early detection and
 continuous monitoring are critical for implementing timely crop
 protection practices to mitigate losses. Advances in agricultural
 robotics may enable high-throughput, autonomous field monitoring. 
 However, most existing disease datasets consist of close-up
 images collected under controlled conditions for manual diagnosis, 
 resulting in models to generalize poorly to robotic platforms
 with wider field imagery for high-throughput disease monitoring.





## Simulator
**Overview.** The simulator is built upon Unreal Engine 5 with ROSIntegration for synthetic image generation. The simulation environment consist of an outdoor tomato field and three robot models (Husky, Benchbot, and Spider). The tomato field can be augmented with real-world leaf disease textures with parameterized height distribution, disease types, and quantity of diseases. 

The most recent version of the simulator for Windows 11 is available at the top of the page. The following information follows the most recent simulator version, but the dataset may not include some of these options.
<div style="overflow:auto; margin:1em 0;">

<img src="./assets/figs/simflowchart-1.jpg" 
       alt="My Figure Description" 
       style="float: right; width: 100%; margin-left: 20px; margin-bottom: 10px; border-radius: 20px;">

</div>

**Environment Parameters.** Aside from the obvioud robot and tomato fields, the environment also includes the time-of-day and cloud systems.

**Field Parameters.** The field follows the row-crop configuration, with adjustable field size and plant gaps in the GUI.

**Robot/Camera Parameters.** 

## Datasets

**TomatoGeneral.** TomatoGeneral is the larger and more varied dataset generated compared to TomatoCastle. The majority of the images have randomized perspectives and uses natural lighting with exposure changes, which are common features across real-world tomato datasets such as LaboroTomato, LeafAndTomato, and TomatOD. In the paper we used this dataset to benchmark out-of-distribution semantic segmentation on the aforementioned datasets and compare to the ACOD-12K dataset. 
<div style="display: flex; flex-wrap: nowrap; align-items: stretch; gap: 20px; width: 100%;">

  <!-- LEFT = 70% -->
  <div style="flex: 0 0 67%;">
    <img-comparison-slider style="width: 100%; height: 100%;">
      <img slot="first" src="./assets/figs/webpage/tmtgeneralrgb.jpg" />
      <img slot="second" src="./assets/figs/webpage/tmtgeneralsemantic.jpg"/>
    </img-comparison-slider>
  </div>

  <!-- RIGHT = 30% -->
  <div style="flex: 0 0 32%;">
    <img-comparison-slider style="width: 100%; height: 100%;">
      <img slot="first" src="./assets/figs/webpage/tmtgeneralrgb2.jpg" />
      <img slot="second" src="./assets/figs/webpage/tmtgeneralsemantic2.jpg" />
    </img-comparison-slider>
  </div>

</div>



**TomatoCastle** TomatoCastle is a more targeted dataset for field robot application, where stereo was also included for stereo matching model training.
  <div style="flex: 0 0 400px; width: 100%; max-width: 400px; ">
    <img-comparison-slider style="width: 100%;">
      <img slot="first" src="./assets/figs/webpage/rgb_68.png"
           alt="My Figure Description"
           style="border-radius: 20px;" />
      <img slot="second" src="./assets/figs/webpage/mapped_semantic.png"
           alt="My Figure Description"
           style="border-radius: 20px;" />
    </img-comparison-slider>
  </div>


## Applications

**Public Datasets**

**Sim2Real**

**Stereo Matching**