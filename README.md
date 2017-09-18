# Introduction

The Network Topology Zoo is an ongoing project to collect data network topologies from around the world. The networks are manually traced from operator provided network maps. This project gives a rough idea of what the Internet looks like.
The 3D Internet Zoo is a simple python script (50 lines) that uses the Internet
Topology Zoo dataset to merge all topologies into a single Google Earth visualization of the Internet.

<p align="center"> 
<img src="https://github.com/afourmy/3D-internet-zoo/blob/master/readme/3D_internet_zoo.gif">
</p>


## The internet network per region

# USA

# Europe

# China

# Japan

# Contact

You can contact me at my personal email address:
```
''.join(map(chr, (97, 110, 116, 111, 105, 110, 101, 46, 102, 111, 
117, 114, 109, 121, 64, 103, 109, 97, 105, 108, 46, 99, 111, 109)))
```

or on the [Network to Code slack](http://networktocode.herokuapp.com "Network to Code slack"). (@minto, #pynms)

# 3D Internet Zoo dependencies

3D Internet Zoo relies on three Python libraries:
* simplekml, used for creating KML files for Google Earth.
* networkx, used for parsing a GML graph

You must make sure all these libraries are properly installed:
```
pip install networkx
pip install simplekml
```

# Credits


