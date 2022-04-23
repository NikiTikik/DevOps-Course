#!/usr/bin/python3

import argparse
import shutil
import os
import sys
import csv
from datetime import datetime

LOG_FILE = '/home/niki/dz11/journal.csv'


def backup(source_dir, backup_dir, compralg):
    """Создание резервной копии всего содержимого директории source"""

    # Проверить, что обе директории существуют
    if not (os.path.isabs(source_dir) and os.path.isdir(source_dir)):
        print('Directory %s doesn\'t exitst' % (source_dir))
        return
    if not (os.path.isabs(backup_dir) and os.path.isdir(backup_dir)):
        print('Directory %s doesn\'t exitst' % (backup_dir))
        return

    # Взять название исходной папки
    if source_dir[-1] == '/':
        src_folder = source_dir.split('/')[-2]
    else:
        src_folder = source_dir.split('/')[-1]
    
    # Определить название архива-бэкапа
    name = src_folder + '_' + str(datetime.utcnow())
    archive_name = os.path.expanduser(os.path.join(backup_dir, name))

    shutil.make_archive(archive_name, compralg, backup_dir)

    print('The backup was created in ' + os.path.dirname(backup_dir))


def logger(journal):
    """Логирование событий"""
    file_exists = os.path.isfile(journal)
    with open(journal, 'a', newline='') as csvfile:
        fieldnames = ['Directory', 'Path_to_backup', 'Time_of_creating', 'Result']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({'Directory': source_dir, 'Path_to_backup': backup_dir, 'Time_of_creating': str(datetime.utcnow()), 'Result': result})


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Save backup of directory')
    parser.add_argument('-d', '--directory',
                        dest='source_dir',
                        type=str,
                        required=True,
                        help='It\'s a directory for backupping')
    parser.add_argument('-o', '--output',
                        dest='backup_dir',
                        type=str,
                        required=True,
                        help='It\'s a directory with backups')
    parser.add_argument('-a', '--compralg',
                        dest='compralg',
                        type=str,
                        default='gztar',
                        required=False,
                        help='Сompression algorithm, please enter \'zip\' for using zip or \'targz\' for using targz \n'
                        r'You can also use "tar", "bztar" or "xztar"')
    parser.add_argument('-j', '--log_journal',
                        dest='journal',
                        default=LOG_FILE,
                        required=False,
                        help='It\'s a journal with logs')
    args = parser.parse_args()

    source_dir = args.source_dir
    backup_dir = args.backup_dir
    journal = args.journal
    compralg = args.compralg
    result = 'success'

    try:
        backup(source_dir, backup_dir, compralg)
    except Exception as e:  
        print(e, file=sys.stderr)
        result = 'fail'
    finally:
        logger(journal)
