from django.test import TestCase

# Create your tests here.
# [[0.08973935 0.13152401 0.09046402 0.09021951 0.09784464 0.1116109 0.09013975 0.09215745 0.09065654 0.11564389]]
# import numpy as np
# import matplotlib.pyplot as plt

# p = np.array([[0.08973935, 0.13152401, 0.09046402, 0.09021951, 0.09784464, 0.1116109, 0.09013975, 0.09215745, 0.09065654, 0.11564389]])
# p = p[0]*100
# nums = np.arange(0, 10)

# bool_p = np.where(p==max(p), 1, 0)
# colors = []
# for i in bool_p:
#     if i:
#         colors.append('#FF8B8B')
#     else:
#         colors.append('#ABC9FF')

# fig, ax = plt.subplots(figsize=(5, 6))
# bar = ax.barh(nums, p, color=colors)
# ax.xaxis.set_ticks_position('none')
# ax.yaxis.set_ticks_position('none')
# ax.xaxis.set_tick_params(pad=5)
# ax.yaxis.set_tick_params(pad=10)
# ax.set_xlim(0, 100)
# ax.set_xlabel("percentage(%)")
# ax.set_yticks(nums, nums)
# ax.grid(b=True, color='gray',
#         linestyle='-.', linewidth=0.5,
#         alpha=0.2)
# ax.invert_yaxis()

# for s in ['top', 'bottom', 'left', 'right']:
#     ax.spines[s].set_visible(False)
# ax.bar_label(bar, padding=3, color='gray', fmt='%.2f')
# plt.show()