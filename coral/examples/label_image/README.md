# TensorFlow Lite Python image classification demo on Edge TPU

It starts with [label_image.py example](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/examples/python) and [Run inference with TensorFlow Lite in Python](https://coral.ai/docs/edgetpu/tflite-python/)

## Project Structure

```sh
frankchen@:label_image$ tree --du -h
.
├── [ 347]  convert.py
├── [919K]  grace_hopper.bmp
├── [3.4K]  label_image.py
├── [ 25K]  labels.txt
├── [ 16M]  mobilenet_v1_1.0_224_frozen.pb
├── [4.3M]  mobilenet_v1_1.0_224_quant_edgetpu.tflite
├── [4.1M]  mobilenet_v1_1.0_224_quant.tflite
├── [ 16M]  mobilenet_v1_1.0_224.tflite
└── [2.6K]  README.md

  42M used in 0 directories, 9 files

```


## Run a model

Run on coral dev board,

1. Run on coral dev board using Edge TPU.

Note: the model that's compiled for the Edge TPU

```sh
python3 label_image.py \
  --model_file ./mobilenet_v1_1.0_224_quant_edgetpu.tflite \
  --label_file ./labels.txt \
  --image ./grace_hopper.bmp

INFO: Initialized TensorFlow Lite runtime.
----INFERENCE TIME----
Note: The first inference on Edge TPU is slow because it includes loading the model into Edge TPU memory.
14.4ms
2.7ms
3.2ms
2.7ms
2.4ms
0.674510: 653:military uniform
0.129412: 907:Windsor tie
0.039216: 458:bow tie, bow-tie, bowtie
0.027451: 668:mortarboard
0.019608: 466:bulletproof vest

```

2. Run on coral dev board using CPU.

Note: the model that's *not* compiled for the Edge TPU

- quantized tflite model
```sh
python3 label_image.py \
  --model_file ./mobilenet_v1_1.0_224_quant.tflite \
  --label_file ./labels.txt \
  --image ./grace_hopper.bmp

INFO: Initialized TensorFlow Lite runtime.
----INFERENCE TIME----
Note: The first inference on CPU is slow because it includes loading the model into CPU memory.
183.7ms
182.3ms
182.1ms
182.0ms
182.5ms
0.658824: 653:military uniform
0.149020: 907:Windsor tie
0.039216: 458:bow tie, bow-tie, bowtie
0.027451: 668:mortarboard
0.019608: 466:bulletproof vest

```

- normal tflite model
```sh
python3 label_image.py \
  --model_file ./mobilenet_v1_1.0_224.tflite \
  --label_file ./labels.txt \
  --image ./grace_hopper.bmp

INFO: Initialized TensorFlow Lite runtime.
----INFERENCE TIME----
Note: The first inference on CPU is slow because it includes loading the model into CPU memory.
304.7ms
180.9ms
187.8ms
166.0ms
177.1ms
0.792127: 653:military uniform
0.084584: 907:Windsor tie
0.021034: 458:bow tie, bow-tie, bowtie
0.009951: 668:mortarboard
0.007782: 514:cornet, horn, trumpet, trump

```

3. Run on desktop using CPU.(Intel(R) Core(TM) i5-6400 CPU @ 2.70GHz)

- quantized tflite model
```sh
python3 label_image_lite.py \
  --model_file ./mobilenet_v1_1.0_224_quant.tflite \
  --label_file ./labels.txt \
  --image ./grace_hopper.bmp

----INFERENCE TIME----
Note: The first inference on Edge TPU is slow because it includes loading the model into Edge TPU memory.
71.5ms
67.6ms
68.2ms
67.8ms
67.5ms
0.874510: 653:military uniform
0.031373: 907:Windsor tie
0.015686: 668:mortarboard
0.011765: 466:bulletproof vest
0.007843: 458:bow tie, bow-tie, bowtie
```

- normal tflite model
```sh
python3 label_image_lite.py \
  --model_file ./mobilenet_v1_1.0_224.tflite \
  --label_file ./labels.txt \
  --image ./grace_hopper.bmp

----INFERENCE TIME----
Note: The first inference on Edge TPU is slow because it includes loading the model into Edge TPU memory.
105.5ms
18.4ms
19.7ms
16.9ms
18.7ms
0.919720: 653:military uniform
0.017762: 907:Windsor tie
0.007507: 668:mortarboard
0.005419: 466:bulletproof vest
0.003828: 458:bow tie, bow-tie, bowtie
```


## Create a Model

Run on host machine(ubuntu)

1. Convert `SavedModel directories` for quantized inference

...

2. Compile TensorFlow Lite file

```sh
edgetpu_compiler mobilenet_v1_1.0_224_quant.tflite
```

test to run mobilenet_v1_1.0_224_quant_edgetpu.tflite on coral dev board.

