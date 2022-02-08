#!/usr/bin/env python

import cv2
import click
from lib.preprocessing_image import remove_edge_of_farm_from_tif, transparent_pixel, red_pixel


@click.command()
@click.argument('src')
@click.argument('dest')
@click.option('--pixel_width', default=10, help='remove pixel width')
@click.option('--debug', default=False, help='debug mode')
def reduce_tif(src, dest, pixel_width=10, debug=False):
    if debug != False:
        debug_pixel = red_pixel
    else:
        debug_pixel = transparent_pixel
    final_image = remove_edge_of_farm_from_tif(src, remove_pixel_width=pixel_width, remove_as_pixel = debug_pixel)
    cv2.imwrite(dest, final_image)
    click.echo(f"{dest} saved")
    return True


if __name__ == '__main__':
    reduce_tif()
