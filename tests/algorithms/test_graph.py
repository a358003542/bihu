#!/usr/bin/env python
# -*-coding:utf-8-*-


from bihu.algorithms.graph.graph import UndirectedGraph, Graph, DirectedGraph




def test_ug():

    ug = UndirectedGraph()


    ug.add_edge({"a","d"})

    ug.add_edge({"d","c"})

    ug.add_edge({"c","b"})

    ug.add_edge({"c","e"})

    ug.add_edge({"c","c"})

    assert ug.has_edge({'c','e'})

def test_dg():

    dg = DirectedGraph()

    dg.add_edge(("a", "d"))

    dg.add_edge(("d", "c"))

    dg.add_edge(("c", "b"))

    dg.add_edge(("c", "e"))

    dg.add_edge(("c", "c"))

    dg.add_edge(('b','f'))

    dg.del_node('c')

    assert not dg.has_node('c')

