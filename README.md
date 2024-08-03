# rangoli-maker
 A tool to create and save lattice-based rangoli art

Controls:
 1) There are three drawing modes: dots, lines, and colors. Press `d`, `l`, and `c` to toggle these, respectively. Only one of these modes can be activate at a given time.
 2) Press `g` to toggle the grid. It toggles between none, a square grid, and a hexagon grid. Use the mouse wheel or up-down cursor keys to adjust magnification. The grids serve to aid in placing dots.
 3) When either a square grid or a hexagon grid is active, press a number will introduce a regular polygon of that length (see caveats below).
 4) Note that pressing `1` will lead to a regular polygon of length 11. Pressing `5` will lead to a regular polygon of length 15, but pressing `6` will construct a regular polygon of length 6.
 5) Press `s` to toggle the symmetry in the system. It toggles between none, C3 (120 degrees), C4 (90 degrees), and C6 (symmetry). The virtual mirrors will convey symmetry.
 6) Symmetry mode affects the construction/destruction of lines and insertion of points only. It doesn't affect the deletion of points and the insertion/deletion of colors.
 7) In dot mode, press the left mouse button to insert a dot and the right mouse button to delete a dot
 8) In line mode, use the left mouse button to select two dots to introduce a line between them. Use the right mouse button to select two dots and delete a line between them.
 9) In color mode, select a color from the palette below and use the left mouse button to introduce the color. Use the right mouse button to remove color
 10) Press `.` to toggle display of dots and `/` to toggle display of lines
 11) Once the rangoli is done, press either left shift or right left to save the rangoli in the `saves` folder as a PNG.

Notes:
 1) Various display parameters can be adjusted in the settings script
 2) Additional colors can be added to the color palette in the `init_color_palette()` function
