#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 上午10:24
# @Author  : Chen Yuelong
# @Mail    : yuelong_chen@yahoo.com
# @File    : plot_models.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals
import os, sys
import argparse
import matplotlib

matplotlib.use('Agg')
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from plotlib.pipeline import density_pipeline, cdf_pipeline, pairplot_pipeline, scatter_pipeline


def main():
    parser = argparse.ArgumentParser(description='Some plots for some different Format file')
    parser_sub = parser.add_subparsers(dest='subparser_name', help='Sub-commands (use with -h for more info)')

    density_parser = parser_sub.add_parser('density', help='plot one column data density')
    density_parser.add_argument('--data', required=True, action='store',
                                help='data, .csv .txt .gz,<required>')
    density_parser.add_argument('--column', required=True, action='store',
                                help='column name wants to plot or col number')
    density_parser.add_argument('--sep', default='\t', action='store',
                                help='sep ,defalut "tab"')
    density_parser.add_argument('--title', default='density', action='store',
                                help='title ,defalut "density"')
    density_parser.add_argument('--output', required=True, action='store',
                                help='the suffix is .png or .pdf,<required>')
    density_parser.add_argument('--header', action='store_true',
                                help='with header? if it is "yes",the column need to be column name')
    density_parser.set_defaults(func=density_pipeline)

    cdf_parser = parser_sub.add_parser('cdf', help='plot one column data cdf')
    cdf_parser.add_argument('--data', required=True, action='store',
                            help='data, .csv .txt .gz,<required>')
    cdf_parser.add_argument('--type-column', required=False, action='store',
                            help='type column name or col number', default='')
    cdf_parser.add_argument('--value-column', required=True, action='store',
                            help='value column name or col number,<required>')
    cdf_parser.add_argument('--sep', default='\t', action='store',
                            help='sep ,defalut "tab"')
    cdf_parser.add_argument('--title', default='cdf', action='store',
                            help='title ,defalut "cdf"')
    cdf_parser.add_argument('--output', required=True, action='store',
                            help='the suffix is .png or .pdf,<required>')
    cdf_parser.add_argument('--header', action='store_true',
                            help='with header? if it is "yes",the column need to be column name')
    cdf_parser.set_defaults(func=cdf_pipeline)

    pairplot_parser = parser_sub.add_parser('pairplot', help='compare pairplot')
    pairplot_parser.add_argument('--data', required=True, action='store',
                                 help='data, .csv .txt .gz,<required>')
    pairplot_parser.add_argument('--column', required=True, action='store', nargs='+',
                                 help='hue column name or col number,<required>')
    pairplot_parser.add_argument('--sep', default='\t', action='store',
                                 help='sep ,defalut "tab"')
    pairplot_parser.add_argument('--title', default='pairpolt', action='store',
                                 help='title ,defalut "pairplot"')
    pairplot_parser.add_argument('--prefix', required=True, action='store',
                                 help='output prefix,<required>')
    pairplot_parser.add_argument('--header', action='store_true',
                                 help='with header? if it is "yes",the column need to be column name')
    pairplot_parser.set_defaults(func=pairplot_pipeline)

    scatter_parser = parser_sub.add_parser('scatter', help='scatter plot')
    scatter_parser.add_argument('--data', required=True, action='store',
                                help='data, .csv .txt .gz')
    scatter_parser.add_argument('--x', required=True, action='store',
                                help='column name wants to plot')
    scatter_parser.add_argument('--y', required=True, action='store',
                                help='column name wants to plot')
    scatter_parser.add_argument('--sep', default='\t', action='store',
                                help='sep ,defalut "tab"')
    scatter_parser.add_argument('--title', default='Scatter', action='store',
                                help='title ,defalut "Scatter"')
    scatter_parser.add_argument('--x-label', default=None,
                                help='x label to show in figure, default is --x name')
    scatter_parser.add_argument('--y-label', default=None,
                                help='y label to show in figure, default is --y name')
    scatter_parser.add_argument('--hue', default=None,
                                help='HUE classification label in the data, which distinguish '
                                     'scatters in different colors')
    scatter_parser.add_argument('--style', default=None,
                                help='STYLE classification label in the data, which distinguish '
                                     'scatters in different shapes')
    scatter_parser.add_argument('--legend', choices=['full', 'brief'], default='full',
                                help='legend type, full for full name, brief for number')
    scatter_parser.add_argument('--alpha', default=0.3, type=float,
                                help='scatter points alpha')
    scatter_parser.add_argument('--width', default=25, type=int,
                                help='figure width')
    scatter_parser.add_argument('--height', default=25, type=int,
                                help='figure height')
    scatter_parser.add_argument('--output', required=True, action='store',
                                help='the suffix is .png or .pdf,<required>')
    scatter_parser.add_argument('--header', action='store_true',
                                help='with header? if it is "yes",the column need to be column name')
    scatter_parser.set_defaults(func=scatter_pipeline)

    # bam_template_gc_parser = parser_sub.add_parser('Bam_GC', help='统计DNA模版GC含量')
    # '''align,fasta,outdir,sample_n=10000'''
    # bam_template_gc_parser.add_argument('--align', dest='align', action='store', required=True,
    #                                     help='bamfile,<required>')
    # bam_template_gc_parser.add_argument('--fasta', dest='fasta', action='store', required=True,
    #                                     help='fasta,need fasta.fai in same direction,<required>')
    # bam_template_gc_parser.add_argument('--outdir', dest='outdir', action='store', required=True,
    #                                     help='outdir,<required>')
    # bam_template_gc_parser.add_argument('--sample', dest='sample_n', action='store', type=int,
    #                                     help='每个contig抽取的模版数（default=100000）', default=100000)
    # bam_template_gc_parser.set_defaults(func=template_gc_length_pipeline)
    #
    # divide_parser = parser_sub.add_parser('Check', help='根据数据获得样本的可分性')
    #
    # divide_parser.add_argument('--file', dest='file', action='store', required=True,
    #                            help='csv file,<required>')
    # divide_parser.add_argument('--method', dest='method', choices=['tsne'], action='store', required=True,
    #                            help='区分的方法，目前只有T-SNE(pca等后续会加入),<required>')
    # divide_parser.add_argument('--outdir', dest='outdir', action='store', required=True,
    #                            help='outdir,<required>')
    # divide_parser.set_defaults(func=divide_pipeline)
    #
    # plot_parser = parser_sub.add_parser('plot3Dscatter', help='画3D scatter图')
    #
    # plot_parser.add_argument('--file', dest='file', action='store', required=True,
    #                          help='csv file（label,c1,c2,c3）,<required>')
    # plot_parser.add_argument('--output', dest='output', action='store', required=True,
    #                          help='output,结尾需要是.html,<required>')
    # plot_parser.set_defaults(func=pyecharts_3d_scatter_pipeline)
    #
    # calgc_parser = parser_sub.add_parser('Bed_GC', help='统计bed区域GC含量')
    #
    # calgc_parser.add_argument('--bed', dest='bed', action='store', required=True,
    #                           help='bed file,<required>')
    # calgc_parser.add_argument('--fasta', dest='fasta', action='store', required=True,
    #                           help='参考基因组，需要有samtools构建的index在同级目录,<required>')
    # calgc_parser.add_argument('--output', dest='output', action='store', required=True,
    #                           help='output,结尾需要.csv,<required>')
    # calgc_parser.set_defaults(func=cal_bed_gc)

    args = parser.parse_args()
    args.func(args)
    # try:
    #     args.func(args)
    # except Exception as e:
    #     print(e.args)
    #     parser.print_help()


if __name__ == '__main__':
    main()
