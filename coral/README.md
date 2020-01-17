# Coral

[Get started with the Dev Board](https://coral.ai/docs/dev-board/get-started/)


## Edge TPU

The Edge TPU is compatible with optimized TensorFlow Lite models only. So you must,

1. train a TensorFlow model.
2. convert it to TensorFlow Lite.(fully 8-bit quantized, quantization)
3. compile it for the Edge TPU.




### Running a model(inference)

However, TensorFlow Lite's default behavior is to execute each model on the `CPU`, so you must instruct the interpreter to run your model on the `Edge TPU`, using Python.

checkout [code examples](./examples/)

1. detect_image

- TPU

```sh
python3 detect_image.py \
   --model models/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite \
   --labels models/coco_labels.txt \
   --input images/grace_hopper.bmp \
   --output images/grace_hopper_processed.bmp

INFO: Initialized TensorFlow Lite runtime.
----INFERENCE TIME----
Note: The first inference is slow because it includes loading the model into Edge TPU memory.
43.14 ms
19.62 ms
16.83 ms
16.27 ms
17.33 ms
-------RESULTS--------
person
  id:     0
  score:  0.83984375
  bbox:   BBox(xmin=1, ymin=2, xmax=516, ymax=599)
tie
  id:     31
  score:  0.83984375
  bbox:   BBox(xmin=228, ymin=421, xmax=293, ymax=545)
```

- CPU

```sh
python3 detect_image.py \
   --model models/mobilenet_ssd_v2_coco_quant_postprocess.tflite \
   --labels models/coco_labels.txt \
   --input images/grace_hopper.bmp

INFO: Initialized TensorFlow Lite runtime.
----INFERENCE TIME----
Note: The first inference is slow because it includes loading the model into Edge TPU memory.
324.27 ms
322.40 ms
322.18 ms
321.95 ms
321.84 ms
-------RESULTS--------
person
  id:     0
  score:  0.83984375
  bbox:   BBox(xmin=2, ymin=5, xmax=513, ymax=596)
tie
  id:     31
  score:  0.83984375
  bbox:   BBox(xmin=228, ymin=418, xmax=293, ymax=544)
```

1. classify_image

- TPU

```sh
python3 classify_image.py \
   --model models/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite \
   --labels models/inat_bird_labels.txt \
   --input images/parrot.jpg

INFO: Initialized TensorFlow Lite runtime.
----INFERENCE TIME----
Note: The first inference on Edge TPU is slow because it includes loading the model into Edge TPU memory.
13.0ms
2.6ms
2.7ms
2.8ms
2.8ms
-------RESULTS--------
Ara macao (Scarlet Macaw): 0.76562
```

- CPU

```sh
python3 classify_image.py \
   --model models/mobilenet_v2_1.0_224_inat_bird_quant.tflite \
   --labels models/inat_bird_labels.txt \
   --input images/parrot.jpg

INFO: Initialized TensorFlow Lite runtime.
----INFERENCE TIME----
Note: The first inference on Edge TPU is slow because it includes loading the model into Edge TPU memory.
150.7ms
149.4ms
149.3ms
149.9ms
149.4ms
-------RESULTS--------
Ara macao (Scarlet Macaw): 0.77344
```

3. lable_image

- TPU

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

- CPU

```sh
python3 label_image.py \
  --model_file ./mobilenet_v1_1.0_224_quant.tflite \
  --label_file ./labels.txt \
  --image ./grace_hopper.bmp

INFO: Initialized TensorFlow Lite runtime.
----INFERENCE TIME----
Note: The first inference on Edge TPU is slow because it includes loading the model into Edge TPU memory.
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

- CPU(non-quantized tflite model)

```sh
python3 label_image.py \
  --model_file ./mobilenet_v1_1.0_224.tflite \
  --label_file ./labels.txt \
  --image ./grace_hopper.bmp

INFO: Initialized TensorFlow Lite runtime.
----INFERENCE TIME----
Note: The first inference on Edge TPU is slow because it includes loading the model into Edge TPU memory.
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

### Creating a model(training)

[TensorFlow models on the Edge TPU](https://coral.ai/docs/edgetpu/models-intro/#compatibility-overview)


***quantization***
  Quantizing a model essentially means converting all the 32-bit floating-point numbers (such as weights and activation outputs) to the nearest 8-bit fixed-point numbers. [Quantization-aware training](https://github.com/tensorflow/tensorflow/tree/r1.13/tensorflow/contrib/quantize#quantization-aware-training)


TensorFlow model => TensorFlow Lite quantized model file(.tflite)
[TensorFlow Lite converter](https://www.tensorflow.org/lite/convert)

TensorFlow Lite (with quantization) => compatible TensorFlow Lite file
[Edge TPU Compiler](https://coral.ai/docs/edgetpu/compiler/)

