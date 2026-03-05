import os
import sys

from pathlib import Path


PNEXTRACT_PATH = Path(__file__).parent / (
    "pnextract" + (".exe" if os.name == "nt" else "")
)
VOXEL_IMAGE_PROCESS_PATH = Path(__file__).parent / (
    "voxelImageProcess" + (".exe" if os.name == "nt" else "")
)


def pnextract() -> None:
    os.execv(PNEXTRACT_PATH, sys.argv)


def voxel_image_process() -> None:
    os.execv(VOXEL_IMAGE_PROCESS_PATH, sys.argv)


if __name__ == "__main__":
    pnextract()
