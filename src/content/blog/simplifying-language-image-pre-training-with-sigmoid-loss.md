---
title: "Simplifying Language-Image Pre-Training with Sigmoid Loss"
description: "Introduction to Language-Image Pre-Training Language-Image Pre-Training (LIP) has become a popular approach to obtain robust visual and textual representations. It involves alignin…"
pubDate: 'Jul 17 2024'
---

## Introduction to Language-Image Pre-Training

Language-Image Pre-Training (LIP) has become a popular approach to obtain robust visual and textual representations. It involves aligning the representations of paired images and texts, typically using a contrastive objective. This method was revolutionized by large-scale models like CLIP and ALIGN, which demonstrated the viability of this approach at a massive scale [1]. As the field progresses, researchers continue to seek methods to make LIP more efficient and effective, addressing challenges such as large batch sizes and resource constraints.

## The Sigmoid Loss Innovation

### Key Problem with Contrastive Learning

Traditional contrastive learning relies on a softmax-based loss function, which requires normalization over the entire batch of image-text pairs. This approach can be computationally expensive and memory-intensive, often necessitating a complex and numerically unstable implementation [1].

### Introducing Sigmoid Loss

To address these challenges, researchers at Google DeepMind have proposed a simpler alternative: the pairwise Sigmoid loss for Language-Image Pre-Training, termed SigLIP. Unlike the softmax normalization, the Sigmoid loss operates solely on individual image-text pairs, which simplifies the computation significantly [1].

### Benefits of Sigmoid Loss

1. **Memory Efficiency**: The Sigmoid loss requires less memory compared to the softmax-based contrastive loss. This makes it possible to scale up the batch size without increasing computational resources exponentially [1].
2. **Decoupling Batch Size**: By not requiring operations across the full batch, the Sigmoid loss decouples the definition of the task from the batch size, allowing flexibility in training setups [1].

![Table 5: SigLIP zeor-shot accuracy (%) on the ImageNet benchmark. Both the sigmoid loss and the softmax loss baseline are presented. Experiments are performed on multiple train examples seen (3 B, 9 B) and train batch sizes (from 512 to 307 k). When trained for 9 B examples, the peak of the sigmoid loss comes earlier at 32 k than the peak of the softmax loss at 98 k. Together with the memory efﬁcient advantage for the sigmoid loss, it allows one to train the best language-image model with much fewer amount of accelerators.](https://askpandilocal.s3.eu-west-1.amazonaws.com/users/1/documents/23/tables/5.png "Table 5: SigLIP zeor-shot accuracy (%) on the ImageNet benchmark. Both the sigmoid loss and the softmax loss baseline are presented. Experiments are performed on multiple train examples seen (3 B, 9 B) and train batch sizes (from 512 to 307 k). When trained for 9 B examples, the peak of the sigmoid loss comes earlier at 32 k than the peak of the softmax loss at 98 k. Together with the memory efﬁcient advantage for the sigmoid loss, it allows one to train the best language-image model with much fewer amount of accelerators.")

*Table 5: SigLIP zeor-shot accuracy (%) on the ImageNet benchmark. Both the sigmoid loss and the softmax loss baseline are presented. Experiments are performed on multiple train examples seen (3 B, 9 B) and train batch sizes (from 512 to 307 k). When trained for 9 B examples, the peak of the sigmoid loss comes earlier at 32 k than the peak of the softmax loss at 98 k. Together with the memory efﬁcient advantage for the sigmoid loss, it allows one to train the best language-image model with much fewer amount of accelerators.*

### Experimental Validation

A series of experiments demonstrated that SigLIP models outperform their counterparts using softmax loss, particularly in smaller batch sizes. For instance, SigLIP achieved 84.5% zero-shot accuracy on ImageNet with only four TPUv4 chips in two days [1].

## Efficient Training With Locked-Image Tuning

### SigLiT Model

![Table 1: SigLiT and SigLIP results. Sigmoid loss is memory efﬁcient, allows larger batch sizes (BS) that unlocks language image pre-training with a small number of chips. SigLiT model with a frozen public](https://askpandilocal.s3.eu-west-1.amazonaws.com/users/1/documents/23/tables/0.png "Table 1: SigLiT and SigLIP results. Sigmoid loss is memory efﬁcient, allows larger batch sizes (BS) that unlocks language image pre-training with a small number of chips. SigLiT model with a frozen public")

The team also introduced the SigLiT model, combining the Sigmoid loss with Locked-image Tuning (LiT). This method achieved remarkable efficiency, with the SigLiT model reaching 79.7% zero-shot accuracy on ImageNet in just one day using four TPUv4 chips [1].

### Impact on Batch Size and Training Duration

![Table 6: Default hyperparameters across different batch sizes, perform either the best or close to the best hyperparameter from a sweep. Zero-shot accuracy on ImageNet is reported. BS=batch size, LR=learning rate, WD=weight decay.](https://askpandilocal.s3.eu-west-1.amazonaws.com/users/1/documents/23/tables/6.png "Table 6: Default hyperparameters across different batch sizes, perform either the best or close to the best hyperparameter from a sweep. Zero-shot accuracy on ImageNet is reported. BS=batch size, LR=learning rate, WD=weight decay.")

*Table 6: Default hyperparameters across different batch sizes, perform either the best or close to the best hyperparameter from a sweep. Zero-shot accuracy on ImageNet is reported. BS=batch size, LR=learning rate, WD=weight decay.*

Through extensive testing, researchers found that while larger batch sizes do offer some performance benefits, the gains diminish beyond a certain point. Surprisingly, a batch size of 32k appeared to be almost optimal, balancing performance and resource efficiency [1].

## Multilingual and Robust Pre-Training

![Table 2: Multilingual SigLIP results with various batch sizes, pre-trained for 30 billion seen examples. We report zero-shot transfer results on ImageNet (INet-0) and averaged text to image retrieval results across 36 languages on the crossmodal 3600 dataset (XM). The full table on 36 languages can be found in Appendix.](https://askpandilocal.s3.eu-west-1.amazonaws.com/users/1/documents/23/tables/2.png "Table 2: Multilingual SigLIP results with various batch sizes, pre-trained for 30 billion seen examples. We report zero-shot transfer results on ImageNet (INet-0) and averaged text to image retrieval results across 36 languages on the crossmodal 3600 dataset (XM). The full table on 36 languages can be found in Appendix.")

*Table 2: Multilingual SigLIP results with various batch sizes, pre-trained for 30 billion seen examples. We report zero-shot transfer results on ImageNet (INet-0) and averaged text to image retrieval results across 36 languages on the crossmodal 3600 dataset (XM). The full table on 36 languages can be found in Appendix.*

### mSigLIP: Multilingual Adaptation

Expanding the approach to multilingual data, the team pre-trained models on datasets covering over 100 languages. They discovered that a batch size of 32k was also sufficient for effective multilingual training, and going beyond this size didn’t yield significant improvements [1].

### Robustness to Noise

Another notable advantage of the Sigmoid loss is its robustness to data noise. Models trained with Sigmoid loss demonstrated a higher tolerance to various types of corruption (e.g., random noise in images or texts), retaining performance superiority over softmax-trained models even under noisy conditions [1].

## Conclusion

The introduction of Sigmoid loss for Language-Image Pre-Training marks a significant advance in the efficiency and effectiveness of LIP models. By simplifying the loss computation and decoupling it from batch size requirements, SigLIP and SigLiT models offer compelling performance with reduced computational overhead. These innovations not only facilitate better utilization of limited resources but also present a robust framework adaptable to multilingual contexts and resistant to data noise. This development paves the way for more accessible and scalable language-image pre-training, fostering further exploration and improvement in the field.

By integrating Sigmoid loss, researchers and practitioners can achieve high performance in LIP tasks with optimized resource use, making advanced AI more accessible and practical for diverse applications [1].

---

[[1] https://arxiv.org/pdf/2303.15343](https://arxiv.org/pdf/2303.15343)
