#!/usr/bin/env python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("directory", type=str, help="List a directory to analyze.")
parser.add_argument("--type", type=str, required=True, help="fluid or particle")
parser.add_argument("--output", type=str, help="output file name")
args = parser.parse_args()

import yt

ytfield = ''
if args.type == 'particle':
	ytfield = 'all_cic'
elif args.type == 'fluid':
	ytfield = 'density'

ds = yt.load(args.directory+'/'+args.directory)
output_dir = '/work/03330/tg826294/projectionplots/'

yt.ProjectionPlot(ds, 'x', ytfield).save(output_dir+args.output+'_x.png')
yt.ProjectionPlot(ds, 'y', ytfield).save(output_dir+args.output+'_y.png')
yt.ProjectionPlot(ds, 'z', ytfield).save(output_dir+args.output+'_z.png')