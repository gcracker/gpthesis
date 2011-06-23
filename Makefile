.SUFFIXES: .fig .eps .pdf .dot .data

OTHERFILES = thesis.bib\
	     Makefile\

GNUPLOT=gnuplot
GENLINESCACHE=python ./gen_cache_lines.py
GENLINES=python ./gen_lines.py
GENLINESDEAD=python ./gen_lines_deadcode.py
GENSPLITBARS=python gen_splitbars.py
GENBARS=python ${PAPER_SCRIPTS}/gen_bars.py
GENBARSD=pdb ${PAPER_SCRIPTS}/gen_bars.py
GENBARS2=python ${PAPER_SCRIPTS}/gen_bars2.py
GEOMEAN=perl ${PAPER_SCRIPTS}/compute_geomean.pl
STACKIFY=perl ${PAPER_SCRIPTS}/stackify.p

TEXFILES=thesis.tex \
	 variable_orders.tex\
	 401sincode.tex\
	 sinfuncs/400sinFuncsRawO0.tex\
	 sinfuncs/400sinFuncsRawO2.tex\
	 sinfuncs/401sinFuncsRawO0.tex\
	 sinfuncs/401sinFuncsRawO2.tex\
	 sinfuncs/403sinFuncsRawO0.tex\
	 sinfuncs/403sinFuncsRawO2.tex\
	 sinfuncs/429sinFuncsRawO0.tex\
	 sinfuncs/429sinFuncsRawO2.tex\
	 sinfuncs/445sinFuncsRawO0.tex\
	 sinfuncs/445sinFuncsRawO2.tex\
	 sinfuncs/458sinFuncsRawO0.tex\
	 sinfuncs/458sinFuncsRawO2.tex\
	 sinfuncs/462sinFuncsRawO0.tex\
	 sinfuncs/462sinFuncsRawO2.tex\
	 sinfuncs/471sinFuncsRawO2.tex\
	 sinfuncs/473sinFuncsRawO0.tex\
	 sinfuncs/473sinFuncsRawO2.tex\
	 sinfuncs/483sinFuncsRawO0.tex\
	 sinfuncs/483sinFuncsRawO2.tex

FIGFILES=

DOTFILES=

DATAFILES=

TABLEMAPFILES=	figures/164gzip_dinvsdin_bddstablemap.png \
		figures/164gzip_dinvsdin_zddstablemap.png \
		figures/164gzip_dinvsdin_bdds_noGCCtablemap.png\
		figures/164gzip_dinvsdin_zdds_noGCCtablemap.png

NOGENPNGFILES=images/regions/400perlbench_test0_1000mil_syscalls_O0_regions.png\
	      images/175vpr_dinvsrdy_250mil_cleanDDCs.png\
	      images/175vpr_dinvsrdy_250mil_blobs2.png\
	      images/choppic.png\
	      images/464h264ref_O0_regions.png\
	      images/464h264ref_O2_regions.png

NOGENEPSFILES=figures/quickdead.eps\
	      figures/robdd.eps\
	      figures/bdtree.eps\
	      figures/zdd.eps\
	      figures/selectionClusters.eps\
	      figures/selectionClustersZoom.eps

NOGENPDFFILES=figures/ia64_254_gap_gcc_inf_bw_din_crop.pdf\
	      figures/175vpr01_mod2.pdf \
	      figures/btree_interlaced.pdf\
	      figures/btree_xfirst.pdf\
	      figures/btree_yfirst.pdf\
	      figures/btree_interlaced_alltrav.pdf\
	      figures/btree_interlaced_range.pdf \
	      figures/ex_dinxrdy_1.pdf \
	      figures/ex_dinxrdy_2.pdf \
	      figures/samplequadtreeds.pdf \
	      figures/bddasquadtree.pdf \
	      figures/dinID.pdf \
	      figures/basecase3.pdf \
	      figures/basecase2.pdf \
	      figures/basecase1.pdf \
	      figures/samplequadtreeds.pdf \
              figures/bdtree.pdf \
              figures/robdd.pdf \
              figures/rozdd.pdf \
              figures/reorderbdd.pdf\
	      figures/zddgraphEx1.pdf\
	      figures/bddgraphEx1.pdf\
	      figures/zddtrace01.pdf	\
	      figures/zddtrace02.pdf	\
	      figures/zddtrace03.pdf	\
              figures/zddtrace04.pdf	\
	      figures/bddtrace01.pdf	\
	      figures/bddtrace02.pdf	\
	      figures/bddtrace03.pdf	\
	      figures/bddtrace04.pdf

GENFIGFILES=

GENEPSFILES=$(FIGFILES:.fig=.eps) \
            $(GENFIGFILES:.fig=.eps)\
	    figures/tlpInterferParallelO0.eps\
	    figures/tlpInterferPerfO0.eps\
	    figures/tlpNaiveParallelO0.eps\
	    figures/tlpNaivePerfO0.eps\
	    figures/tlpPerfO0.eps\
	    figures/tlpParallelO0.eps\
	    figures/tlpInterferParallelO2.eps\
	    figures/tlpInterferPerfO2.eps\
	    figures/tlpNaiveParallelO2.eps\
	    figures/tlpNaivePerfO2.eps\
	    figures/tlpPerfO2.eps\
            figures/slice10.eps\
	    figures/slice100.eps\
	    figures/slice1000.eps\
	    figures/slice10000.eps\
	    figures/memory_bound.eps\
	    figures/visualizationTime.eps	\
	    figures/dindinTime.eps	\
	    figures/dinsinTime.eps	\
	    figures/dinrdyTime.eps  \
	    figures/dindinBDDTime.eps	\
	    figures/dinsinBDDTime.eps	\
	    figures/dinrdyBDDTime.eps  \
	    figures/dindinSize.eps  \
	    figures/dinsinSize.eps	\
	    figures/dinrdySize.eps  \
	    figures/dindinGC.eps	\
	    figures/dinsinGC.eps	\
	    figures/dinrdyGC.eps	\
	    figures/dindinGCTime.eps	\
	    figures/dinsinGCTime.eps	\
	    figures/dinrdyGCTime.eps	\
	    figures/164gzip_dinvsdin_bdds_linechart.eps	\
	    figures/164gzip_dinvsdin_zdds_linechart.eps \
		figures/403gccDeadCodeDiffRemoved.eps\
		figures/400perlbenchDeadCodeDiffRemoved.eps\
		figures/401bzip2DeadCodeDiffRemoved.eps\
		figures/429mcfDeadCodeDiffRemoved.eps\
		figures/445gobmkDeadCodeDiffRemoved.eps\
		figures/456hmmerDeadCodeDiffRemoved.eps\
		figures/458sjengDeadCodeDiffRemoved.eps\
		figures/464h264refDeadCodeDiffRemoved.eps\
		figures/471omnetppDeadCodeDiffRemoved.eps\
		figures/473astarDeadCodeDiffRemoved.eps\
		figures/483xalancbmkDeadCodeDiffRemoved.eps\
		figures/deadCodeDiffTotal.eps\
		figures/deadCodeDiffTotalPercent.eps\
		figures/403gccDeadCodeRemoved.eps\
		figures/400perlbenchDeadCodeRemoved.eps\
		figures/401bzip2DeadCodeRemoved.eps\
		figures/429mcfDeadCodeRemoved.eps\
		figures/445gobmkDeadCodeRemoved.eps\
		figures/456hmmerDeadCodeRemoved.eps\
		figures/458sjengDeadCodeRemoved.eps\
		figures/464h264refDeadCodeRemoved.eps\
		figures/471omnetppDeadCodeRemoved.eps\
		figures/473astarDeadCodeRemoved.eps\
		figures/483xalancbmkDeadCodeRemoved.eps\
		figures/deadCodeTotalO0.eps\
		figures/deadCodeTotalO2.eps\
		figures/deadCodeBothTotal.eps\
		figures/deadCodeTotalPercentO0.eps\
		figures/deadCodeTotalPercentO2.eps\
		figures/deadCodeBothTotalPercent.eps\
		figures/tlpPerfTLS.eps

EPSFILES=$(GENEPSFILES)

PDFFILES=$(EPSFILES:.eps=.pdf)

OTHERFILES =

.fig.eps:
	fig2dev -L eps $< $@

.dot.fig:
	dot -Gsize="12,4" -Tfig -o $@ $<

.eps.pdf:
	epstopdf $<

pdf: thesis.pdf

ps: thesis.ps

print: thesis.pdf
	lpr thesis.pdf

thesis.ps: thesis.dvi
	dvips -e 0 -P cmz -t letter -o thesis.ps thesis.dvi

thesis.pdf: $(TEXFILES) $(EPSFILES) $(PDFFILES) $(OTHERFILES)
	pdflatex thesis.tex
	bibtex thesis || echo 'BiBTeX failed; continuing anyway'
	pdflatex thesis.tex
	pdflatex thesis.tex

thesis.dvi:$(TEXFILES) $(EPSFILES) $(PDFFILES) $(OTHERFILES)
	latex thesis
	bibtex thesis || echo 'BiBTeX failed; continuing anyway'
	latex thesis
	latex thesis

clean:
	rm -f $(PDFFILES) $(GENEPSFILES) thesis.dvi thesis.aux thesis.bbl thesis.blg thesis.log thesis.ps thesis.pdf

thesis.bib:
	if [ ! -e thesis.bib ]; then ln -s ../../bib/thesis.bib; fi

spellcheck:
	for i in $(TEXFILES); do if [ $$i == thesis.tex ]; then continue; fi; aspell --personal=./personal.wl -c $$i; done

figures/quickdead.eps: figures/%.eps: data/%.data
	${GENBARS} --xtitle "Benchmark" --ytitle "Tuple Count" --fillpatterns "color.grey.black,color.grey.white" --yend 1200000000 --legenddist +0.1 --legendxshift +1.0 --legendpos "-t-r" --legendyshift +0.15 --width 13 --delim ',' --subnamesize .5 --output  $@ $<;

figures/tlpPerfO0.eps: figures/%.eps: data/%.data
	${GENBARS} --xtitle "Benchmark" --ytitle "Parallelized Instructions \%" --fillpatterns "color.grey.black,color.grey.white" --legenddist +0.1 --legendxshift +1.0 --legendpos "-t-r" --legendyshift +0.15 --width 10 --delim ',' --ysplitauto 2 --subnamesize .5 --output  $@ $<;

figures/tlpNaivePerfO0.eps: figures/%.eps: data/%.data
	${GENBARS} --xtitle "Benchmark" --ytitle "Parallelized Instructions \%" --fillpatterns "color.grey.black,color.grey.white"  --nolegend --legenddist +0.1 --legendxshift +1.0 --legendpos "-t-r" --legendyshift +0.15 --width 10 --ysplitauto 2 --delim ',' --subnamesize .5 --output  $@ $<;

figures/tlpInterferPerfO0.eps: figures/%.eps: data/%.data
	${GENBARS} --xtitle "Benchmark" --ytitle "Parallelized Instructions \%" --fillpatterns "color.grey.black,color.grey.white" --nolegend --legenddist +0.1 --legendxshift +1.0 --legendpos "-t-r" --legendyshift +0.15 --width 10 --delim ',' --subnamesize .5 --output  $@ $<;

figures/tlpNaiveParallelO0.eps: figures/%.eps: data/%.data
	${GENBARS} --xtitle "Benchmark" --ytitle "Maximum Thread Count" --fillpatterns "color.grey.black,color.grey.white" --nolegend --legenddist +0.1 --legendxshift +1.0 --legendpos "-t-r" --legendyshift +0.15 --width 10 --delim ',' --subnamesize .5 --output  $@ $<;

figures/tlpInterferParallelO0.eps: figures/%.eps: data/%.data
	${GENBARS} --xtitle "Benchmark" --ytitle "Maximum Thread Count" --fillpatterns "color.grey.black,color.grey.white" --nolegend --legenddist +0.1 --legendxshift +1.0 --legendpos "-t-r" --legendyshift +0.15 --width 10 --delim ',' --subnamesize .5 --output  $@ $<;

figures/tlpPerfO2.eps: figures/%.eps: data/%.data
	${GENBARS} --xtitle "Benchmark" --ytitle "Parallelized Instructions \%" --fillpatterns "color.grey.black,color.grey.white" --legenddist +0.1 --legendxshift +0.5 --legendpos "-t-r" --legendyshift +0.15 --width 10 --delim ',' --ysplitauto 3 --subnamesize .5 --output  $@ $<;

figures/tlpNaivePerfO2.eps: figures/%.eps: data/%.data
	${GENBARS} --xtitle "Benchmark" --ytitle "Parallelized Instructions \%" --fillpatterns "color.grey.black,color.grey.white" --nolegend --legenddist +0.1 --legendxshift +1.0 --legendpos "-t-r" --legendyshift +0.15 --width 10 --ysplitauto 3 --delim ',' --subnamesize .5 --output  $@ $<;

figures/tlpInterferPerfO2.eps: figures/%.eps: data/%.data
	${GENBARS} --xtitle "Benchmark" --ytitle "Parallelized Instructions \%" --fillpatterns "color.grey.black,color.grey.white" --nolegend --legenddist +0.1 --legendxshift +1.0 --legendpos "-t-r" --legendyshift +0.15 --width 10 --delim ',' --subnamesize .5 --output  $@ $<;

figures/tlpNaiveParallelO2.eps: figures/%.eps: data/%.data
	${GENBARS} --xtitle "Benchmark" --ytitle "Maximum Thread Count" --fillpatterns "color.grey.black,color.grey.white" --nolegend --legenddist +0.1 --legendxshift +1.0 --legendpos "-t-r" --legendyshift +0.15 --width 10 --ysplitauto 2 --delim ',' --subnamesize .5 --output  $@ $<;

figures/tlpInterferParallelO2.eps: figures/%.eps: data/%.data
	${GENBARS} --xtitle "Benchmark" --ytitle "Maximum Thread Count" --fillpatterns "color.grey.black,color.grey.white" --nolegend --legenddist +0.1 --legendxshift +1.0 --legendpos "-t-r" --legendyshift +0.15 --width 10 --delim ',' --subnamesize .5 --output  $@ $<;

figures/tlpPerfTLS.eps: figures/%.eps: data/%.data
	${GENBARS} --xtitle "Benchmark" --ytitle "Parallelized Instructions \%" --legenddist +0.1 --legendxshift +3.5 --legendpos "-t-r" --legendyshift +0.15 --width 13 --delim ',' --subnamesize .5 --output  $@ $<;

figures/tlpParallelO0.eps: figures/%.eps: data/%.data
	${GENBARS} --xtitle "Benchmark" --ytitle "Maximum Thread Count" --fillpatterns "color.grey.black,color.grey.white" --legenddist +0.08 --legendxshift +1.0 --legendpos "-t-r" --legendyshift +0.08 --width 10 --delim ',' --subnamesize .5 --output  $@ $<;

# Begin Unate slicing Methods graphs

figures/slice10.eps: figures/%.eps: data/%.dat
	${GENBARS} --xtitle "Benchmark" --ytitle "Seconds" --fillpatterns "color.grey.black,color.grey.white" --ysplit [[0,9],[23,54]] --ylabels "4" --legenddist +0.1 --legendxshift +0.1 --legendpos "-t-r" --legendyshift +0.15 --width 13 --delim ',' --subnamesize .5 --output  $@ $<;

figures/slice100.eps: figures/%.eps: data/%.dat
	${GENBARS} --xtitle "Benchmark" --ytitle "Seconds" --ysplitauto 2 --fillpatterns "color.grey.black,color.grey.white" --legenddist +0.1 --legendxshift +1.0 --legendpos "-t-r" --legendyshift +0.15 --width 13 --delim ',' --subnamesize .5 --output  $@ $<;

figures/slice1000.eps: figures/%.eps: data/%.dat
	${GENBARS} --xtitle "Benchmark" --ytitle "Seconds" --fillpatterns "color.grey.black,color.grey.white" --legenddist +0.1 --legendxshift +1.0 --legendpos "-t-r" --legendyshift +0.15 --width 13 --delim ',' --subnamesize .5 --output  $@ $<;

figures/slice10000.eps: figures/%.eps: data/%.dat
	${GENBARS} --xtitle "Benchmark" --ytitle "Seconds" --fillpatterns "color.grey.black,color.grey.white" --legenddist +0.1 --legendxshift +0.5 --legendpos "-t-r" --legendyshift +0.15 --width 13 --delim ',' --subnamesize .5 --output  $@ $<;

# BEGIN CGO 10 paper figures

figures/164gzip_dinvsdin_zdds_linechart.eps: figures/%.eps: data/%.data
	${GENLINES} figures/164gzip_dinvsdin_zdds_linechart.eps data/164gzip_dinvsdin_zdds_linechart.data

figures/164gzip_dinvsdin_bdds_linechart.eps: figures/%.eps: data/%.data
	${GENLINES} figures/164gzip_dinvsdin_bdds_linechart.eps data/164gzip_dinvsdin_bdds_linechart.data

figures/dindinGCTime.eps: figures/%.eps: data/%.csv
	${GENBARS} --xtitle "Benchmark" --ytitle "Time (Minutes)" --yend 8000 --legenddist 0.1 --legendxshift -1.5 --legendpos "-t-r" --legendyshift -0.9 --width 13 --delim ',' --subnamesize .5  --stack 2 --fillpatterns "color.grey.black,color.grey.white" --output  $@ $<;

figures/dinsinGCTime.eps: figures/%.eps: data/%.csv
	${GENBARS} --xtitle "Benchmark" --nolegend --ytitle "Time (Minutes)" --yend 2000 --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-r" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --stack 2 --fillpatterns "color.grey.black,color.grey.white" --output  $@ $<;

figures/dinrdyGCTime.eps: figures/%.eps: data/%.csv
	${GENBARS} --xtitle "Benchmark" --ytitle "Time (Minutes)" --yend 2000 --nolegend --legenddist 0.1 --legendxshift +0.7 --legendpos "-t-r" --legendyshift -0.8 --width 13 --delim ',' --subnamesize .5  --stack 2 --fillpatterns "color.grey.black,color.grey.white" --output  $@ $<;

figures/memory_bound.eps: figures/%.eps: data/%.data
	${GENBARS} --xtitle "Benchmark" --ytitle "Tuple Count" --yend 4000000000 --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-r" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/300.twolf_dinvsdin_bddstablemap.png: data/tablemaps/300.twolf_dinvsdin_bdds.tablemap.gnu data/tablemaps/300.twolf_dinvsdin_bdds.tablemap.data
	${GNUPLOT} data/tablemaps/300.twolf_dinvsdin_bdds.tablemap.gnu

figures/256bzip2_dinvsdin_bddstablemap.png: data/tablemaps/256.bzip2_dinvsdin_bdds.tablemap.gnu data/tablemaps/256.bzip2_dinvsdin_bdds.tablemap.data
	${GNUPLOT} data/tablemaps/256.bzip2_dinvsdin_bdds.tablemap.gnu

figures/254gap_dinvsdin_bddstablemap.png: data/tablemaps/254.gap_dinvsdin_bdds.tablemap.gnu data/tablemaps/254.gap_dinvsdin_bdds.tablemap.data
	${GNUPLOT} data/tablemaps/254.gap_dinvsdin_bdds.tablemap.gnu

figures/253perlbmk_dinvsdin_bddstablemap.png: data/tablemaps/253.perlbmk_dinvsdin_bdds.tablemap.gnu data/tablemaps/253.perlbmk_dinvsdin_bdds.tablemap.data
	${GNUPLOT} data/tablemaps/253.perlbmk_dinvsdin_bdds.tablemap.gnu

figures/252eon_dinvsdin_bddstablemap.png: data/tablemaps/252.eon_dinvsdin_bdds.tablemap.gnu data/tablemaps/252.eon_dinvsdin_bdds.tablemap.data
	${GNUPLOT} data/tablemaps/252.eon_dinvsdin_bdds.tablemap.gnu

figures/186crafty_dinvsdin_bddstablemap.png: data/tablemaps/186crafty_dinvsdin_bdds.tablemap.gnu data/tablemaps/186.crafty_dinvsdin_bdds.tablemap.data
	${GNUPLOT} data/tablemaps/186.crafty_dinvsdin_bdds.tablemap.gnu

figures/181mcf_dinvsdin_bddstablemap.png: data/tablemaps/181.mcf_dinvsdin_bdds.tablemap.gnu data/tablemaps/181.mcf_dinvsdin_bdds.tablemap.data
	${GNUPLOT} data/tablemaps/181.mcf_dinvsdin_bdds.tablemap.gnu

figures/176gcc_dinvsdin_bdds_noGCCtablemap.png: data/tablemaps/176gcc_dinvsdin_bdds_noGCC.tablemap.gnu data/tablemaps/176gcc_dinvsdin_bdds_noGCC.tablemap.data
	${GNUPLOT} data/tablemaps/176gcc_dinvsdin_bdds_noGCC.tablemap.gnu 

figures/176gcc_dinvsdin_bddstablemap.png: data/tablemaps/176gcc_dinvsdin_bdds.tablemap.gnu data/tablemaps/176.gcc_dinvsdin_bdds.tablemap.data
	${GNUPLOT} data/tablemaps/176gcc_dinvsdin_bdds.tablemap.gnu

figures/175vpr_dinvsdin_bddstablemap.png: data/tablemaps/175.vpr_dinvsdin_bdds.tablemap.gnu data/tablemaps/175.vpr_dinvsdin_bdds.tablemap.data
	${GNUPLOT} data/tablemaps/175.vpr_dinvsdin_bdds.tablemap.gnu 

figures/175vpr_dinvsdin_zddstablemap.png: data/tablemaps/175.vpr_dinvsdin_zdds.tablemap.gnu  data/tablemaps/175.vpr_dinvsdin_zdds.tablemap.data
	${GNUPLOT} data/tablemaps/175.vpr_dinvsdin_zdds.tablemap.gnu 

figures/175vpr_dinvsdin_zdds_noGCCtablemap.png: data/tablemaps/175.vpr_dinvsdin_zdds_noGCC.tablemap.gnu data/tablemaps/175.vpr_dinvsdin_zdds_noGCC.tablemap.data
	${GNUPLOT} data/tablemaps/175.vpr_dinvsdin_zdds_noGCC.tablemap.gnu 

figures/175vpr_dinvsdin_bdds_noGCCtablemap.png: data/tablemaps/175.vpr_dinvsdin_bdds_noGCC.tablemap.gnu data/tablemaps/175.vpr_dinvsdin_bdds_noGCC.tablemap.data
	${GNUPLOT} data/tablemaps/175.vpr_dinvsdin_bdds_noGCC.tablemap.gnu 

figures/164gzip_dinvsdin_bddstablemap.png: data/tablemaps/164.gzip_dinvsdin_bdds.tablemap.gnu data/tablemaps/164.gzip_dinvsdin_bdds.tablemap.data
	${GNUPLOT} data/tablemaps/164.gzip_dinvsdin_bdds.tablemap.gnu 

figures/164gzip_dinvsdin_zddstablemap.png: data/tablemaps/164.gzip_dinvsdin_zdds.tablemap.gnu  data/tablemaps/164.gzip_dinvsdin_zdds.tablemap.data
	${GNUPLOT} data/tablemaps/164.gzip_dinvsdin_zdds.tablemap.gnu 

figures/164gzip_dinvsdin_bdds_noGCCtablemap.png: data/tablemaps/164.gzip_dinvsdin_bdds_noGCC.tablemap.gnu data/tablemaps/164.gzip_dinvsdin_bdds_noGCC.tablemap.data
	${GNUPLOT} data/tablemaps/164.gzip_dinvsdin_bdds_noGCC.tablemap.gnu 

figures/164gzip_dinvsdin_zdds_noGCCtablemap.png: data/tablemaps/164.gzip_dinvsdin_zdds_noGCC.tablemap.gnu data/tablemaps/164.gzip_dinvsdin_zdds_noGCC.tablemap.data
	${GNUPLOT} data/tablemaps/164.gzip_dinvsdin_zdds_noGCC.tablemap.gnu 

figures/visualizationTime.eps: figures/%.eps: data/%.data
	${GENBARS} --xtitle "Benchmark" --height 5 --ytitle "Seconds" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-r" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/dinrdySize.eps: figures/%.eps: data/%.data
	${GENBARS}  --nolegend --xtitle "Benchmark" --height 5 --ytitle "Nodes" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/dinsinSize.eps: figures/%.eps: data/%.data
	${GENBARS} --nolegend  --xtitle "Benchmark" --height 5 --ytitle "Nodes" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/dindinSize.eps: figures/%.eps: data/%.data
	${GENBARS}  --xtitle "Benchmark" --height 5 --ytitle "Nodes" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-r" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/dinrdyGC.eps: figures/%.eps: data/%.data
	${GENBARS} --nolegend --xtitle "Benchmark" --height 5 --ytitle "Seconds" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/dinsinGC.eps: figures/%.eps: data/%.data
	${GENBARS} --nolegend  --xtitle "Benchmark" --height 5 --ytitle "Seconds" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/dindinGC.eps: figures/%.eps: data/%.data
	${GENBARS}  --xtitle "Benchmark" --height 5 --ytitle "Seconds" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/dindinTime.eps: figures/%.eps: data/%.data
	${GENBARS}  --xtitle "Benchmark" --height 5 --ytitle "Seconds" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/dinsinTime.eps: figures/%.eps: data/%.data
	${GENBARS}  --nolegend  --xtitle "Benchmark" --height 5 --ytitle "Seconds" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/dinrdyTime.eps: figures/%.eps: data/%.data
	${GENBARS} --nolegend --xtitle "Benchmark" --height 5 --ytitle "Seconds" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/dindinBDDTime.eps: figures/%.eps: data/%.data
	${GENBARS}  --xtitle "Benchmark" --height 5 --ytitle "Minutes" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/dinsinBDDTime.eps: figures/%.eps: data/%.data
	${GENBARS}  --nolegend  --xtitle "Benchmark" --height 5 --ytitle "Minutes" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/dinrdyBDDTime.eps: figures/%.eps: data/%.data
	${GENBARS} --nolegend --xtitle "Benchmark" --height 5 --ytitle "Minutes" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/graph_bar_time.eps: figures/%.eps: data/%.data
	${GENBARS}  --xtitle "Benchmark" --height 5 --ytitle "Performance Improvement" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/175vpr_cache_conflictssec.eps: figures/%.eps: data/bddcon/%.csv
	python ./comma2space.py data/bddcon/175vpr_cache_conflictssec.csv temp.data
	${GENLINESCACHE} figures/175vpr_cache_conflictssec.eps temp.data
	rm temp.data

# Dead Code Removal Line Graphs
figures/403gccDeadCodeRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/400perlbenchDeadCodeRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/401bzip2DeadCodeRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/429mcfDeadCodeRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/445gobmkDeadCodeRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/456hmmerDeadCodeRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/458sjengDeadCodeRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/464h264refDeadCodeRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/471omnetppDeadCodeRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/473astarDeadCodeRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/483xalancbmkDeadCodeRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;

# Dead Code Removal Line Graphs with O0 O2 diff
figures/403gccDeadCodeDiffRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/400perlbenchDeadCodeDiffRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/401bzip2DeadCodeDiffRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/429mcfDeadCodeDiffRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/445gobmkDeadCodeDiffRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/456hmmerDeadCodeDiffRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/458sjengDeadCodeDiffRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/464h264refDeadCodeDiffRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/471omnetppDeadCodeDiffRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/473astarDeadCodeDiffRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;
figures/483xalancbmkDeadCodeDiffRemoved.eps: figures/%.eps: data/%.data
	${GENLINESDEAD}  $@ $<;

figures/deadCodeTotalO0.eps: figures/%.eps: data/%.data
	${GENBARS}  --xtitle "Benchmark" --height 5 --ytitle "Irrelevant Instruction Count" --legenddist 0.1 --legendxshift +0.2 --nolegend --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/deadCodeBothTotal.eps: figures/%.eps: data/%.data
	${GENBARS}  --xtitle "Benchmark" --height 5 --ytitle "Irrelevant Dependence Count" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/deadCodeTotalO2.eps: figures/%.eps: data/%.data
	${GENBARS}  --xtitle "Benchmark" --height 5 --ytitle "Irrelevant Dependence Count" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --nolegend --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/deadCodeDiffTotal.eps: figures/%.eps: data/%.data
	${GENBARS2}  --xtitle "Benchmark" --height 5 --ytitle "Irrelevant Dependence Count Diff" --nolegend --width 13 --barrelative 0 --delim "," --output  $@ $<;

figures/deadCodeTotalPercentO0.eps: figures/%.eps: data/%.data
	${GENBARS}  --xtitle "Benchmark" --height 5 --ytitle "Irrelevant Dependence Percent" --legenddist 0.1 --legendxshift +0.2 --nolegend --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/deadCodeBothTotalPercent.eps: figures/%.eps: data/%.data
	${GENBARS}  --xtitle "Benchmark" --height 5 --ytitle "Irrelevant Dependence Percent" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/deadCodeTotalPercentO2.eps: figures/%.eps: data/%.data
	${GENBARS}  --xtitle "Benchmark" --height 5 --ytitle "Irrelevant  Dependence Count" --legenddist 0.1 --legendxshift +0.2 --legendpos "-t-l" --legendyshift +0.2 --width 13 --delim ',' --nolegend --subnamesize .5  --fillpatterns "color.grey.black,color.grey.white,color.grey(.6)" --output  $@ $<;

figures/deadCodeDiffTotalPercent.eps: figures/%.eps: data/%.data
	${GENBARS2}  --xtitle "Benchmark" --height 5 --ytitle "Irrelevant  Dependence Count Diff" --nolegend --width 13 --barrelative 0 --delim "," --output  $@ $<;