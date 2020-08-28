# -*- coding: utf-8 -*-
# @Author: frankchen
# @Date:   2020-01-07 16:27:23
# @Last Modified by:   frankchen
# @Last Modified time: 2020-01-07 16:42:04
import tensorflow as tf

saved_model_dir = "./mobilenet_v1_1.0_224"


# Convert the model.
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()
