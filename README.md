# ***Cassava-Leaf-Disease-Detection***

<img src="https://user-images.githubusercontent.com/75840165/110804699-6b38d200-82a6-11eb-85fc-dc4e48dfa249.jpg" height=400, width=500 />  <img src="https://user-images.githubusercontent.com/75840165/110804685-68d67800-82a6-11eb-854b-a6c6711a853b.jpg" height=400, width=500 /> 

## Overview:-
* As the second-largest provider of carbohydrates in Africa, cassava is a key food security crop grown by smallholder farmers because it can withstand harsh conditions.
At least 80% of household farms in Sub-Saharan Africa grow this starchy root, but viral diseases are major sources of poor yields.With the help of data science, it 
may be possible to identify common diseases so they can be treated.
* Existing methods of disease detection require farmers to solicit the help of government-funded agricultural experts to visually inspect and diagnose the plants. This 
suffers from being labor-intensive, low-supply and costly. As an added challenge, effective solutions for farmers must perform well under significant constraints, since
African farmers may only have access to mobile-quality cameras with low-bandwidth.

## Goal:- 
To classify each cassava image into five disease categories  With our help, farmers may be able to quickly 
identify diseased plants, potentially saving their crops before they inflict irreparable damage.

## Data:- 
>* This is dataset from Kaggle competition 
>* We have train set containing  more than 20k images
>* To know more about dataset i have added dataset_info.md file

## ***Approch 1***:-
* In this approch we solved this problem as ***MultiLabel*** classsification 
* Trained 3 models(own created cnn, ResNet50V2, InceptionResNetV2) with Hypertuning on sample dataset of 10k images. Got best accuracy with InceptionREsNet of 70%
* Then trained ***InceptionResNetV2*** on full data and got ***73%*** accuracy
* Here are some result's of this approch

<img src="https://user-images.githubusercontent.com/75840165/111069968-8a796e80-84f5-11eb-8e86-ace38d1431ce.png" height=200, width=400 />   <img src="https://user-images.githubusercontent.com/75840165/111069972-8cdbc880-84f5-11eb-85e0-669223cca16a.png" height=200, width=400 /> 
<img src="https://user-images.githubusercontent.com/75840165/111069976-8fd6b900-84f5-11eb-8aaf-21b01d661098.png" height=200, width=400 />     <img src="https://user-images.githubusercontent.com/75840165/111069974-8f3e2280-84f5-11eb-93a2-03a28da34d5f.png" height=200, width=400 />

  
