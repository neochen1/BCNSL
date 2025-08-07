# BCNSL
Medical Image Analysis Under Review

The implementation of "Self-supervised Learning with Adaptive Graph Structure and Function Representation For Cross-Dataset Brain Disorder Diagnosis".

# Abstract
Recent studies in neuroscience highlight the significant potential of brain connectivity networks, which are commonly constructed from functional magnetic resonance imaging (fMRI) data for brain disorder diagnosis. Traditional brain connectivity networks are typically obtained using predefined methods that incorporate manually-set thresholds to estimate inter-regional relationships. However, such approaches often introduce redundant connections or overlook essential interactions, compromising the value of the constructed networks. Besides, the insufficiency of labeled data further increases the difficulty of learning generalized representations of intrinsic brain characteristics. To mitigate those issues, we propose a self-supervised framework to learn an optimal structure and representation for brain connectivity networks, focusing on individualized generation and optimization in an unsupervised manner. We firstly employ two existing whole-brain connectomes to adaptively construct their complementary brain network structure learner, and then introduce a multi-state graph-based encoder with a joint iterative learning strategy to simultaneously optimize both the generated network structure and its representation. By leveraging self-supervised pretraining on large-scale unlabeled brain connectivity data, our framework enables the brain connectivity network learner to generalize effectively to unseen disorders, while requiring only minimal fine-tuning of the encoder for adaptation to new diagnostic tasks. Extensive experiments on cross-dataset brain disorder diagnosis demonstrate that our method consistently outperforms state-of-the-art approaches, validating its effectiveness and generalizability.



# Requirements
'''
numpy
pandas
scipy
matplotlib
pytorch
visdom
networkx
dgl
pickle
tqdm
rdkit
torch_geometric
'''
