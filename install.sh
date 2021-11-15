export CUDACXX=/usr/local/cuda/bin/nvcc

export PYTHON=python3
pypath=$( dirname `pip3 --version | cut -d " " -f 4` )

pip3 install -r requirements.txt 




(
  cd tools/warp-ctc
  mkdir build
  cd build
  cmake ..
  make
  cd ../pytorch_binding
  $PYTHON setup.py install
)


(
  cd tools/warp-transducer
  mkdir build
  cd build
  cmake ..
  make 
  cd ../pytorch_binding
  $PYTHON setup.py install
)


(
  sudo apt install build-essential cmake libboost-system-dev libboost-thread-dev libboost-program-options-dev libboost-test-dev libeigen3-dev zlib1g-dev libbz2-dev liblzma-dev
  cd tools/kenlm
  mkdir build
  cd build
  cmake ..
  make
  cd ..
  $PYTHON setup.py install 
)


(
 cd tools
 ln -s /opt/kaldi kaldi
)


(
    set -euo pipefail
    cd tools
    cp -rf sctk-2.4.10 sctk
    cd sctk
    make config
    touch .configured
    make all && make install && make doc
)




ln -s `realpath espnet` $pypath/
ln -s `realpath espnet2` $pypath/

