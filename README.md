pyemd
=====

A Python wrapper around FastEMD by Ofir Pele.

Please cite these papers if you use this code:

     A Linear Time Histogram Metric for Improved SIFT Matching
     Ofir Pele, Michael Werman
     ECCV 2008
    bibTex:
    @INPROCEEDINGS{Pele-eccv2008,
    author = {Ofir Pele and Michael Werman},
    title = {A Linear Time Histogram Metric for Improved SIFT Matching},
    booktitle = {ECCV},
    year = {2008}
    }
     Fast and Robust Earth Mover's Distances
     Ofir Pele, Michael Werman
     ICCV 2009
    @INPROCEEDINGS{Pele-iccv2009,
    author = {Ofir Pele and Michael Werman},
    title = {Fast and Robust Earth Mover's Distances},
    booktitle = {ICCV},
    year = {2009}
    }

The code in the subdirectory, FastEMD, is taken from the website,
http://www.cs.huji.ac.il/~ofirpele/FastEMD/

I've successfully compiled on Windows Python 2.7 AMD64,
Cython 0.20.1 and numpy 1.7.0 and the Windows SDK. Pull requests
that correct build problems on other platforms would be appreciated.
