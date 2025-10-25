# Synthetic Tomato Disease Datasets

*The paper is being revised with an improved synthetic dataset for generalization in tomato leaf disease and fruit detection. We plan to add the trained weights and second dataset afterwards.*

The paper is avaliable at <arxiv link\>.

The datasets are licensed under a CC-BY-NC-4.0. It is intended for non-generative AI research and non-commercial use due to assets used in simulation.

## Simulator

This is the Unreal Engine simulator repository: [https://github.com/ARLabXiang/AgriRoboSimUE5](https://github.com/ARLabXiang/AgriRoboSimUE5)
This is the ROS2 repository with the data collection: [https://github.com/XingjianL/UE5Sim_colcon_ws/blob/tomato/src/tomato_xarm6/src/tomato_data_gen.cpp](https://github.com/XingjianL/UE5Sim_colcon_ws/blob/tomato/src/tomato_xarm6/src/tomato_data_gen.cpp)

We have packaged applications used for the data collection below, which is generally older versions. We will update the simulation periodically.

## TomatoGeneral

[Simulation (Box)](https://cornell.box.com/s/fd926e2olotm2comes944n3xcrarrvfe)

[Dataset (IEEE DataPort)](https://ieee-dataport.org//documents/synthetic-tomato-disease-and-plant-parts-dataset)

**More Details Coming Soon**

## TomatoCastle

We public the compressed version of the dataset with 16-bit depth and 95\% quality RGB on [HuggingFace (160GB)](https://huggingface.co/datasets/XingjianLi/tomatotest). *Note: 23 pairs were corrupted during data collection or preprocessing, see `corrupted_h5.txt`*

The original rendered 32-bit depth and PNGs is on [Globus (750GB)](https://app.globus.org/file-manager?origin_id=b2e1b583-53be-4933-9d4f-70c83425bb79&origin_path=%2F). Note: The differences between the two is in sub-millimeters.

The packaged UE5 simulator environment is on [Globus (3.84GB)](https://app.globus.org/file-manager?origin_id=4d656862-689a-49e3-b8e8-cb54bcab3767&origin_path=%2F).
