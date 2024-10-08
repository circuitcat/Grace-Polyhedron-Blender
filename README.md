# Grace's Largest 8-Vertex Polyhedron Blender Project
<p align="center">
  <img src="./0010.png" alt="Grace's Polyhedron" width=30%>
  <img src="./0001-0099_2.gif" alt="Grace's Polyhedron" width=30%>
  <img src="./0012.png" alt="Grace's Polyhedron" width=30%>
</p>

This repository contains a Blender project and script for generating Donald W. Grace's 'Largest 8-Vertex Polyhedron', discovered in 1962 using a Burroughs 220 computer, which maximizes the volume for a polyhedron with eight vertices inscribed in a unit sphere.

## Files Included
- [`Graces_Polyhedron.blend`](./Graces_Polyhedron.blend): The Blender project file. (Contains the script below.)
- [`graces_polyhedron_script.py`](./graces_polyhedron_script.py): The script to generate the polyhedron. (In case you want to view it here.)
- [`Graces_Polyhedron.stl`](./Graces_Polyhedron.stl): 3D model file to print or view

## Compatibility
This project was created using **Blender 3.3.1**. The script and project file should work with Blender 3.x versions, but you might need to make minor adjustments if using a different version. If you encounter any issues, consider checking for the following:
- **Script Compatibility**: Some Blender Python API functions might differ slightly between versions, so ensure that the functions used are supported in your version.
- **User Interface**: The location of certain tools or settings in Blender may change between versions, so refer to the Blender documentation for the version you are using.

## Screenshot
Here’s a screenshot of the polyhedron generated in Blender:

![Grace's Polyhedron Screenshot](./graces_polyhedron_screenshot.png)

## How to Use (Overview)
1. Open [`Graces_Polyhedron.blend`](./Graces_Polyhedron.blend) in Blender.
2. The script has been run before the file was saved, so the results are already visible.
3. In case you want to check out the script, you can Run the script in the Scripting tab to regenerate the polyhedron.

## How to Run the Script in Blender (Details)
To generate Grace's Polyhedron using the provided Blender file, follow these steps:

1. **Open the Blender Project**:
   - Download and open the [`Graces_Polyhedron.blend`](./Graces_Polyhedron.blend) file in Blender.

2. **Access the Script**:
   - Once the file is open, go to the **Scripting** workspace at the top of the Blender window.

3. **Run the Script**:
   - The script is already included in the Blender file. In the Text Editor panel, ensure the script is loaded (it should be visible by default). Click the **Run Script** button at the top of the Text Editor. This will execute the script and generate the polyhedron in the 3D Viewport.

4. **Inspect the Generated Polyhedron**:
   - After running the script, the polyhedron should appear in the 3D Viewport. You can use Blender’s tools to inspect, rotate, or modify the polyhedron.

## References
- [Grace's Polyhedron Discovery](https://www.ams.org/journals/mcom/1963-17-082/S0025-5718-63-99183-X/S0025-5718-63-99183-X.pdf)
- [Stand-up Maths' YouTube Video Explanation](https://www.youtube.com/watch?v=XZy3rXr2yeM&t=387s)
- [Convex Hull in Geometry](https://en.wikipedia.org/wiki/Convex_hull)
- [Platonic and Archimedean Solids](https://mathworld.wolfram.com/PlatonicSolid.html)
