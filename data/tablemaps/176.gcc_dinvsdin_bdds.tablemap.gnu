set terminal png nocrop enhanced size 640,480
set output 'figures/176gcc_dinvsdin_bddstablemap.png'
set title "176.gcc DINxDIN Unique Table with BDDs After GC"
set xlabel "Variable Index"
set xlabel  offset character -2, -2, 0
set ylabel "Instruction Count (Millions)"
set ylabel  offset character 3, -3, 0
set zlabel "Node Count"
set zlabel  offset character 1, 0, 0
set contour both
set view 78,347
set style data lines
set hidden3d
set logscale z

splot 'data/tablemaps/176.gcc_dinvsdin_bdds.tablemap.data' matrix
