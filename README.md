Medical Image Analysis Under Review

## Abstract
Recent studies in neuroscience highlight the significant potential of brain connectivity networks, which are commonly constructed from functional magnetic resonance imaging (fMRI) data for brain disorder diagnosis. Traditional brain connectivity networks are typically obtained using predefined methods that incorporate manually-set thresholds to estimate inter-regional relationships. However, such approaches often introduce redundant connections or overlook essential interactions, compromising the value of the constructed networks. Besides, the insufficiency of labeled data further increases the difficulty of learning generalized representations of intrinsic brain characteristics. To mitigate those issues, we propose a self-supervised framework to learn an optimal structure and representation for brain connectivity networks, focusing on individualized generation and optimization in an unsupervised manner. We firstly employ two existing whole-brain connectomes to adaptively construct their complementary brain network structure learner, and then introduce a multi-state graph-based encoder with a joint iterative learning strategy to simultaneously optimize both the generated network structure and its representation. By leveraging self-supervised pretraining on large-scale unlabeled brain connectivity data, our framework enables the brain connectivity network learner to generalize effectively to unseen disorders, while requiring only minimal fine-tuning of the encoder for adaptation to new diagnostic tasks. Extensive experiments on cross-dataset brain disorder diagnosis demonstrate that our method consistently outperforms state-of-the-art approaches, validating its effectiveness and generalizability. The code is publicly available at https://github.com/neochen1/BCNSL.


## Framework
!(./images/framework.png)

## Environment
```
rdkit
torch 1.10.1 +cu113
torch-cluster 1.5.9
torch-geometric 2.0.2
torch-scatter 2.0.9
torch-sparse 0.6.12
torch-spline-conv 1.2.1
torchaudio 0.10.0+cu113
torchvision 0.11.2+cu113
tqdm 4.66.1
```

## Dataset
```
UKB: https://biobank.ctsu.ox.ac.uk/.
ADNI: http://adni.loni.usc.edu/.
ABIDE: http://preprocessed-connectomes-project.org/abide/.
ADHD: http://preprocessed-connectomes-project.org/adhd200/.
```


## Usage
```
python pretrain.py
python finetune.py --dataset="abide" --cl_exp_dir=transfer_exp/chem/transfer_adni705 --cl_model_name=cl_model_10.pth --save=100ep --epoch=100
```
