from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from modes import hex_to_rgb, plot_constellation, build_modes

kwargs = {}

#bgcolor = hex_to_rgb('00070E')
bgcolor = hex_to_rgb('FFFFFF')

# Written in base 1. Converted to base 0
ionian = np.array([1, 3, 5, 6, 8, 10, 12]) - 1
greek_mode_dict, greek_mode_names = build_modes(ionian, [
    'Ionian', 'Dorian', 'Phyrgian', 'Lydian', 'Mixolydian', 'Aeolian',
    'Locrian'])


def plot_modes_one_at_a_time(mode_dict, mode_names):
    for scale_num, scale_name in enumerate(mode_names):
        scale = mode_dict[scale_name]
        fig = plt.figure(100 + scale_num, figsize=(6, 6))
        ax = plt.subplot(111)
        ax.set_aspect('equal')
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)
        plot_constellation(scale, pos_xy=(0., 0.), scale_name=scale_name)
        plt.axis('off')
        fig.savefig(scale_name + '.png', format='png')


def plot_modes(mode_dict, mode_names, fignum=0):
    num_modes = len(mode_names)
    fig_width = 30

    num_levels = int((num_modes - 1) / 7) + 1
    num_steps = min(7, num_modes)

    fig_height = 6 * num_levels

    fig = plt.figure(fignum, figsize=(fig_width, fig_height))
    fig.clf()

    step_size_y = 6
    step_size_x = 4.32  # 11*tau/16

    start_x = -step_size_x * (num_steps - 1) / 2
    start_y = +step_size_y * (num_levels - 1) / 2

    cur_x = start_x
    cur_y = start_y

    ax = fig.add_subplot(111)
    # ax.set_axis_bgcolor(bgcolor)
    ax.set_facecolor(bgcolor)
    y_shift = 0
    ax.set_xlim(-fig_width / 2.0, fig_width / 2.0)
    ax.set_ylim((-fig_height / 2.0) - y_shift, fig_height / 2.0 - y_shift)
    ax.set_aspect('equal')

    for count, scale_name in enumerate(mode_names):
        pos_xy = (cur_x, cur_y)
        scale = mode_dict[scale_name]

        if scale_name.find('or') > -1:
            scale_name = scale_name.replace('or ', 'or\n')
        else:
            scale_name = scale_name.replace(' ', '\n')

        plot_constellation(scale, pos_xy=pos_xy, scale_name=scale_name)
        cur_x += step_size_x
        if np.mod(count, 7) == 6:
            cur_y -= step_size_y
            cur_x = start_x
    plt.axis('off')
    fig.savefig('modes' + str(num_modes) + '.png', format='png')
    fig.show()


def main():
    # Plot greek modes
    mode_dict, mode_names = (greek_mode_dict, greek_mode_names)
    plot_modes(mode_dict, mode_names, fignum=0)
    plot_modes_one_at_a_time(greek_mode_dict, greek_mode_names)

    # Plots the ones from wikipedia
    try:
        from wiki_scale_list import get_wiki_modes
        from wiki_scale_list import get_wiki_mode_names
        wiki_mode_dict = get_wiki_modes()
        wiki_mode_names = get_wiki_mode_names()
        plot_modes(wiki_mode_dict, wiki_mode_names, fignum=1)
        plot_modes_one_at_a_time(wiki_mode_dict, wiki_mode_names)
    except Exception as ex:
        print('ex = {!r}'.format(ex))

    plt.show()
    plt.draw()

if __name__ == '__main__':
    """
    CommandLine:
        python ~/code/pitch_constellations/scales.py
    """
    main()
