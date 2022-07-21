import tensorflow as tf
import numpy as np
import cv2, io, urllib
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

from base64 import b64decode, b64encode

model = tf.keras.models.load_model('C:\projects\mysite2\epoch_28')
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

def base64_to_img(base64_str):
    encoded_img = base64_str.split(',', 1)[1]
    np_img = np.fromstring(b64decode(encoded_img), np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_GRAYSCALE)
    return img


def guess_img(base64_str):
    global probability_model

    input_img = base64_to_img(base64_str)
    resized_img = cv2.resize(input_img, (28, 28), interpolation=cv2.INTER_LINEAR)
    reversed_img = cv2.bitwise_not(resized_img)
    img = np.expand_dims(reversed_img, -1)
    img = np.expand_dims(img, 0)
    img = img.astype(np.float32) / 255.
    predictions_single = probability_model.predict(img)
    return np.argmax(predictions_single[0]), predictions_single[0]


def make_plot(predictions):
    percents = predictions*100
    nums = np.arange(0, 10)
    bool_p = np.where(percents == max(percents), 1, 0)
    colors = []
    for i in bool_p:
        if i:
            colors.append('#FF8B8B')
        else:
            colors.append('#ABC9FF')
    
    fig, ax = plt.subplots()
    bar = ax.barh(nums, percents, color=colors)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)
    ax.set_xlim(0, 100)
    ax.set_xlabel("percentage(%)")
    ax.set_yticks(nums, nums)
    ax.grid(b=True, color='gray',
            linestyle='-.', linewidth=0.5,
            alpha=0.2)
    ax.invert_yaxis()

    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    ax.bar_label(bar, padding=3, color='gray', fmt='%.2f')

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = b64encode(buf.read())
    url = urllib.parse.quote(string)
    plt.close()
    return url