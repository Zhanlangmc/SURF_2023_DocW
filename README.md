# ScaleDoc: A Two Stage Approach for Scale Aware Document Dewarping

# Introduction
Document dewarping has been researched for many years
but remains unresolved, particularly due to multi-scale document issues
(where the background occupies a large proportion). To enhance the
multi-scale awareness of document dewarping algorithms, we propose a
two-stage framework with explicit scale-aware capabilities, named Scale-
Doc, which consists of a scale-aware stage and a dewarping stage. The
scale-aware stage, a convolutional network based on self-attention mechanisms, is proposed to explicitly remove the document background. The
dewarping stage introduces a lightweight method that dewarps warped
documents by predicting document edges using sparse control points.
Furthermore, to train the scale-aware stage network and validate the
effectiveness of ScaleDoc, a new document dataset, DocW, has been cre-
ated. DocW comprises 1k images of varying scales and warping levels, all
of which are authentically captured rather than generated. Comparative
and ablation studies are conducted on the newly created DocW dataset
and DocUnet benchmark dataset. Dewarping results, measured by the
MS-SSIM and LD metrics, and OCR results, measured by the CER and
ED indicate that the proposed model outperforms the current state-of-
the-art (SOTA) models in dealing with multi-scale document challenges.

# Dataset
More information about dataset **DocW** could be found in [dataset.md](dataset.md)

# Results
![result1.png](imgs%2Fresult1.png)

![result2.png](imgs%2Fresult2.png)

![result3.png](imgs%2Fresult3.png)

# Poster
