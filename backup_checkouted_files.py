#! /usr/bin/python

#TODO: nazwa modulu bledna bo nie tylko checkouted ale tez private.
__author__="amousa_68"
__date__ ="$Dec 9, 2016 7:48:54 AM$"

import os
import os.path
from common import make_path


def rmgen(view):
    cmd = "rm -rf /view/" + view + "/vobs/porta/sw/develop/gen/*"
    print cmd
    os.system(cmd)

def backup(view, lscmd, backup_dir):
    make_path(backup_dir)
    out = os.popen("cd /view/" + view +" ; " + lscmd)
    line = out.readline().strip()
    while len(line) > 0:
        outpath = os.path.join(backup_dir, line.strip("\"/"))
        (outdir, outfile) = os.path.split(outpath)
        os.makepath(outdir)
        cmd = "cp " + line + " \"" + outdir + "\""
        print cmd
        os.system(cmd)
        line = out.readline().strip()
    out.close()


if __name__ == "__main__":
    VIEWS = [
        "amousa_EMPTY",
        "amousa_PORTA_052_011_310_MAINT_DEV",
        "amousa_PORTA_052_011_310_MAINT_INT",
        "amousa_PORTA_BAS_052_MAINT_DEV",
        "amousa_PORTA_BAS_052_MAINT_PREINT",
        "amousa_PORTA_FRONTIER_DEV",
        "amousa_PORTA_FRONTIER_PREINT",
        "amousa_PORTA_KERNEL_2_4_31-SHC",
        "amousa_PORTA_WEBCOMMON_BAS_022_MAINT_DEV",
        "amousa_PORTA_WEBCOMMON_BAS_022_MAINT_PREINT",
        "amousa_TOOLING_PIB",
        "PORTA_TO_GIT",
    ]

    BACKUP_DIR_LSCO = "/home/amousa/backup_porta_lsco/"
    BACKUP_DIR_LSPRIVATE = "/home/amousa/backup_porta_lsprivate/"

    for view in VIEWS:
        print "VIEW:", view
        #rmgen(view)
        backup(view, "/build/vct lsco", BACKUP_DIR_LSCO)
        #backup(view, "/build/vct lsprivate", BACKUP_DIR_LSPRIVATE)



