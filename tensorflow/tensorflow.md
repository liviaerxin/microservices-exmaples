# TensorFlow

[TensorFlow Guide](https://www.tensorflow.org/guide)

[9 Things You Should Know About TensorFlow](https://hackernoon.com/9-things-you-should-know-about-tensorflow-9cf0a05e4995)

[What is TensorFlow? The machine learning library explained](https://www.infoworld.com/article/3278008/what-is-tensorflow-the-machine-learning-library-explained.html)

[TensorFlow Tutorial For Beginners](https://www.datacamp.com/community/tutorials/tensorflow-tutorial)(*)

[TensorFlow Tutorial](https://www.tutorialspoint.com/tensorflow/index.htm)(*)

[[TensorFlow] Ch4: Support Vector Machines](https://medium.com/cs-note/tensorflow-ch4-support-vector-machines-c9ad18878c76)

TensorFlow is the `ML(machine learning)` framework that Google created for numerical computation and large-scale machine learning, and mainly used to design, build and train deep learning models. TensorFlow bundles together a slew of machine learning and deep learning (aka neural networking) models and algorithms and makes them useful by way of a common metaphor.

## Keras

Keras is a high-level API to build and train `deep learning` models which is a subfield of `ML(machine learning)`. It's used for fast prototyping, advanced research, and production, with three key advantages:

- User friendly
Keras has a simple, consistent interface optimized for common use cases. It provides clear and actionable feedback for user errors.

- Modular and composable
Keras models are made by connecting configurable building blocks together, with few restrictions.

- Easy to extend
Write custom building blocks to express new ideas for research. Create new layers, loss functions, and develop state-of-the-art models.

## TensorRT

`TensorRT(TF-RT)` is supposed to accelerate inference in TensorFlow. It includes a deep learning inference optimizer and runtime that delivers low latency and high-throughput for deep learning inference applications.

[Speed up TensorFlow Inference on GPUs with TensorRT](https://medium.com/tensorflow/speed-up-tensorflow-inference-on-gpus-with-tensorrt-13b49f3db3fa)

[TensorFlow/TensorRT Models on Jetson TX2](https://jkjung-avt.github.io/tf-trt-models/)

![TensorRT Optimize Neural Network Model](./trt-info.png "TensorRT Optimize Neural Network Model")

### TensorRT Inference Server

[NVIDIA TensorRT Inference Server](https://docs.nvidia.com/deeplearning/sdk/tensorrt-inference-server-guide/docs/index.html)

[NVIDIA TensorRT Inference Server Boosts Deep Learning Inference](https://devblogs.nvidia.com/nvidia-serves-deep-learning-inference/)


the `model repository` lives in a directory on the file system.

```
/tmp/models             --- directory for model repository
   mymodel/             --- subdirectory for each model
      config.pbtxt      --- configuration file 
      3/                --- subdirectory holding a version of the model
         model.plan      
```

### TensorRT Inference Client





## TensorFlow Lite

[TensorFlow Lite guide](https://www.tensorflow.org/lite/guide)

[Hosted models](https://www.tensorflow.org/lite/guide/hosted_models)


## Basic Methods

- List host gpu

```sh
$ nvidia-smi
```

- List devices

```python
from tensorflow.python.client import device_lib

#local_device_protos = device_lib.list_local_devices()

def get_available_cpus():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos if x.device_type == 'CPU']

def get_available_gpus():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos if x.device_type == 'GPU']
```

