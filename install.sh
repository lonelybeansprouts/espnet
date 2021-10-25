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


ln -s `realpath espnet` $pypath/
ln -s `realpath espnet2` $pypath/

