from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import os

def get_version():
    """Get version from git or file system.

    If this is a git repository, try to get the version number by
    running ``git describe``, then store it in
    javabridge/_version.py. Otherwise, try to load the version number
    from that file. If both methods fail, quietly return None.

    """
    git_version = None
    if os.path.exists(os.path.join(os.path.dirname(__file__), '.git')):
        import subprocess
        try:
            git_version = subprocess.Popen(['git', 'describe'], 
                                           stdout=subprocess.PIPE).communicate()[0].strip()
        except:
            pass

    version_file = os.path.join(os.path.dirname(__file__), 'pyemd', 
                                '_version.py')
    if os.path.exists(version_file):
        with open(version_file) as f:
            cached_version_line = f.read().strip()
        try:
            # From http://stackoverflow.com/a/3619714/17498
            cached_version = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", 
                                       cached_version_line, re.M).group(1)
        except:
            raise RuntimeError("Unable to find version in %s" % version_file)
    else:
        cached_version = None

    if git_version and git_version != cached_version:
        with open(version_file, 'w') as f:
            print >>f, '__version__ = "%s"' % git_version

    return git_version or cached_version

def get_ext_modules():
    from numpy import get_include
    fast_emd_path = os.path.join(os.path.dirname(__file__), "FastEMD")
    include_path = os.path.join(os.path.dirname(__file__), "pyemd", "include")
    return cythonize([
        Extension(
            "_pyemd",
            ["pyemd/_pyemd.pyx"],
            language = "c++",
            include_dirs = [get_include(), fast_emd_path, include_path])])

setup(name="pyemd",
      version=get_version(),
      description="Python wrapper for FastEMD",
      long_description="""PyEMD is a Python wrapper for the fast earth mover's
distance algorithm described in Pele, "Fast and Robust Earth Mover's Distances",
ICCV2009, doi: 10.1109/ICCV.2009.5459199""",
      license='BSD License',
      ext_modules=get_ext_modules())
      

      
        