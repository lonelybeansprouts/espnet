#!/usr/bin/env bash

# Copyright 2017 Johns Hopkins University (Shinji Watanabe)
#  Apache 2.0  (http://www.apache.org/licenses/LICENSE-2.0)

. ./path.sh || exit 1;
. ./cmd.sh || exit 1;

# general configuration
decode_config=conf/tuning/transducer/decode_default.yaml
backend=pytorch
example_feat_json=dump/test/deltafalse/split32utt/data.1.json
model_path=exp/train_sp_pytorch_rnnt/results/model.loss.best


rnnt_export.py \
    --config ${decode_config} \
    --backend ${backend} \
    --recog-json  $example_feat_json  \
    --model ${model_path}


  
