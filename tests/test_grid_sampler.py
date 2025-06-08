import os
import sys
import numpy as np
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from grid_sampler import create_resized_grid


def test_large_one_pixel_size():
    img = np.zeros((5, 5, 3), dtype=np.uint8)
    # one_pixel_size larger than image dimensions should still return 1x1 image
    out = create_resized_grid(img, 10)
    assert out.shape[:2] == (1, 1)


def test_invalid_one_pixel_size():
    img = np.zeros((5, 5, 3), dtype=np.uint8)
    with pytest.raises(ValueError):
        create_resized_grid(img, 0)


def test_alpha_channel_preserved():
    img = np.zeros((4, 4, 4), dtype=np.uint8)
    img[:, :, 3] = 128
    out = create_resized_grid(img, 2)
    assert out.shape[2] == 4
    assert np.all(out[:, :, 3] == 128)
