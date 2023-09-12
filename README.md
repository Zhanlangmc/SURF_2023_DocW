# Multi-Scale Document Dewarping via an End-to-End Deep Neural Network Approach
![overall.png](imgs%2Foverall.png)

# Introduction
Over the past decade, with the ubiquity of smartphones, digitizing documents by capturing them with phone cameras has become the norm. While this approach has undeniably enhanced convenience, it also means that the procured documents might suffer from poor quality or morphological distortions, posing substantial challenges for subsequent document recognition [1]. Although there have been advancements in document dewarping techniques in recent years, the correction of small-scale document data remains inadequately addressed. To address this gap, our team introduced a novel deep learning-based multi-scale document correction method. Initially, a coarse correction of document images is achieved based on the fully convolutional attention mechanism-based bounding prediction network (FCViT)[1]. Subsequently, we utilized the curvature dewarping technique based on sparse control points prediction from DDCP [2] for further refinement. As a final measure, the corrected images undergo super-resolution enhancement using DocDiff[3], a lightweight model premised on residual prediction, augmenting their usability.

# Dataset
More information about dataset **DocW** could be found in [dataset.md](dataset.md)

# Results
![result1.png](imgs%2Fresult1.png)

![result2.png](imgs%2Fresult2.png)

![result3.png](imgs%2Fresult3.png)
