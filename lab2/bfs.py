import sys
import os.path
import argparse

from collections import deque

def bfs(graph, start, end):
    queue = deque([(start, [start])])
    visited = set([])
    while queue:
        (node, path) = queue.popleft()
        if node == end:
            return path
        for neigbour in graph[node]:
            if not neigbour in visited:
                queue.append((neigbour, path + [neigbour]))
                visited.add(neigbour)
    return None

def distance(graph, start, end):
    path = bfs(graph, start, end)
    if path:
        return len(path) - 1
    return -1

def have_edge(word1, word2):
    n = 0
    for c in word1[1:]:
        if c in word2:
            n += 1
            i = word2.index(c)
            word2 = word2[:i] + word2[i + 1:]
    return n == (len(word1) - 1)

def build_graph_without_bucket(f):
    words = {word.strip(): set([]) for word in f}
    for word1 in words:
        for word2 in words:
            if word1 != word2 and have_edge(word1, word2):
                words[word1].add(word2)
    return words

def build_graph(f):
    words = dict()
    buckets = dict()
    for line in f:
        word = line.strip()
        words[word] = set([])
        for i in range(len(word)):
            bucket = ''.join(sorted(word[:i] + word[i + 1:]))
            if bucket in buckets:
                buckets[bucket].append(word)
            else:
                buckets[bucket] = [word]
    for bucket in buckets.keys():
        for word1 in buckets[bucket]:
            for word2 in buckets[bucket]:
                if word1 != word2 and have_edge(word1, word2):
                    words[word1].add(word2)
    return words

if __name__ == '__main__':
    def get_valid_file(parser, arg):
        if not os.path.exists(arg):
            parser.error('The file %s does not exist!' % arg)
        else:
            return open(arg, 'r')
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data', dest='datafile', required=True,
            type=lambda f: get_valid_file(parser, f), help='data file')
    parser.add_argument('-t', '--test', dest='testfile', required=True,
            type=lambda f: get_valid_file(parser, f), help='test file')
    args = parser.parse_args()

    #graph = build_graph_without_bucket(args.datafile)
    graph = build_graph(args.datafile)

    for line in args.testfile:
        s, t = line.strip().split(' ')
        print distance(graph, s, t)
