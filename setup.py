import os
import subprocess
from pathlib import Path

from setuptools import setup
from setuptools.command.build_py import build_py as _build_py


class build_py(_build_py):
    def run(self):
        super().run()

        subprocess.run(["make"], cwd=Path("pnextract"), check=True)

        pnextract_name = "pnextract" + (".exe" if os.name == "nt" else "")
        (Path("pnextract", "bin", pnextract_name)).rename(
            Path("src", "pnextract", pnextract_name)
        )

        voxel_image_process_name = "voxelImageProcess" + (
            ".exe" if os.name == "nt" else ""
        )
        (Path("pnextract", "bin", voxel_image_process_name)).rename(
            Path("src", "pnextract", voxel_image_process_name)
        )


setup(
    cmdclass={"build_py": build_py},
    package_dir={"": "src"},
    package_data={"pnextract": ["pnextract*", "voxelImageProcess*"]},
)
