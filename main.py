# coding:utf-8

# @author 枫儿

import json
import base64
import argparse

import aircv as ac
import pypuzzle


def findImg(big, small):
    imsrc = ac.imread(big)
    imsch = ac.imread(small)
    return ac.find_all_sift(imsrc, imsch)
    pass


def ImgCVEC(path):
    puzzle = pypuzzle.Puzzle();
    vec = puzzle.get_cvec_from_file(path);
    cmp_vec = puzzle.compress_cvec(vec)
    return ':'.join(map(str, cmp_vec))
    pass


def matchImg(eva, evb):
    puzzle = pypuzzle.Puzzle();
    eva_vec = puzzle.uncompress_cvec(tuple(map(int, eva.split(":"))))
    evb_vec = puzzle.uncompress_cvec(tuple(map(int, evb.split(":"))))
    return puzzle.get_distance_from_cvec(eva_vec, evb_vec)
    pass



ap = argparse.ArgumentParser()

ap.add_argument("-a", "--action", required=True, help="要执行的操作：bfs=图中找图、cvev=获取图片指纹、match=比对两个指纹")

ap.add_argument("-big", "--bigImgPath", required=False, help="要用于查找的大图路径")
ap.add_argument("-small", "--smallImgPath", required=False, help="要用于查找的小图路径")

ap.add_argument("-evimg", "--cvevImgPath", required=False, help="要获取指纹的图片路径")

ap.add_argument("-eva", "--cvevA", required=False, help="比对两个指纹，第一个指纹字符串")
ap.add_argument("-evb", "--cvevB", required=False, help="比对两个指纹，第二个指纹字符串")

ap.add_argument("-demoA", "--demoA", required=False, help="示例\t图中找图:python main.py -a bfs -big /user/big.png -small /user/small.png")
ap.add_argument("-demoB", "--demoB", required=False, help="示例\t获取图片指纹:python main.py -a cvev -evimg /user/big.png")
ap.add_argument("-demoC", "--demoC", required=False, help="示例\t比对两个指纹:python main.py -a match -eva xxx -evb xxx")



var = vars(ap.parse_args())


if(var['action'] == "bfs"):
    ret = findImg(var['bigImgPath'], var['smallImgPath'])
    print json.dumps(ret)
elif(var['action'] == "cvev"):
    ret = ImgCVEC(var['cvevImgPath'])
    print ret
elif (var['action'] == "match"):
    ret = matchImg(var['cvevA'], var['cvevB'])
    print ret
    pass