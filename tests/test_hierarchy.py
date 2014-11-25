import json

from ppp_questionparsing_grammatical import Word, DependenciesTree, computeTree, simplify
import data

from unittest import TestCase

class HierarchyTests(TestCase):

    def testQuestion(self):
        tree=computeTree(data.give_president_of_USA()['sentences'][0])
        self.assertEqual(simplify(tree),'who')

    def testQuestion2(self):
        tree=computeTree(data.give_how_hold()['sentences'][0])
        self.assertEqual(simplify(tree),'how old')

    def testHierarchySimplification(self):
        tree=computeTree(data.give_president_of_USA()['sentences'][0])
        simplify(tree)
        root=tree
        # Root
        self.assertEqual(root.wordList,[Word("ROOT",0)])
        self.assertEqual(root.namedEntityTag,'undef')
        self.assertEqual(root.dependency,'t0')
        self.assertEqual(root.parent,None)
        self.assertEqual(len(root.child),1)
        self.assertEqual(root.subtreeType,'PERSON')
        self.assertEqual(root.dfsTag,0)
        # Is
        is_=root.child[0]
        self.assertEqual(is_.wordList,[Word("identity",2,'VBZ')])
        self.assertEqual(is_.namedEntityTag,'undef')
        self.assertEqual(is_.dependency,'t0')
        self.assertEqual(is_.parent,root)
        self.assertEqual(len(is_.child),1)
        self.assertEqual(is_.subtreeType,'PERSON')
        self.assertEqual(is_.dfsTag,0)
        # President
        president=is_.child[0]
        self.assertEqual(president.wordList,[Word("president",4,'NN')])
        self.assertEqual(president.namedEntityTag,'undef')
        self.assertEqual(president.dependency,'t1')
        self.assertEqual(president.parent,is_)
        self.assertEqual(len(president.child),1)
        self.assertEqual(president.subtreeType,'PERSON')
        self.assertEqual(president.dfsTag,0)
        # United States
        us=president.child[0]
        self.assertEqual(us.wordList,[Word("United",7,'NNP'),Word("States",8,'NNPS')])
        self.assertEqual(us.namedEntityTag,'LOCATION')
        self.assertEqual(us.dependency,'t4')
        self.assertEqual(us.parent,president)
        self.assertEqual(len(us.child),0)
        self.assertEqual(us.subtreeType,'undef')
        self.assertEqual(us.dfsTag,0)
        
    def testIgnore(self):
        tree=computeTree(data.give_how_hold()['sentences'][0])
        simplify(tree)
        root=tree
        # Root
        self.assertEqual(root.wordList,[Word("ROOT",0)])
        self.assertEqual(root.namedEntityTag,'undef')
        self.assertEqual(root.dependency,'t0')
        self.assertEqual(root.parent,None)
        self.assertEqual(len(root.child),1)
        self.assertEqual(root.subtreeType,'NUMBER')
        self.assertEqual(root.dfsTag,0)
        # Are
        are=root.child[0]
        self.assertEqual(are.wordList,[Word("age",3,'VBP')])
        self.assertEqual(are.namedEntityTag,'undef')
        self.assertEqual(are.dependency,'t0')
        self.assertEqual(are.parent,root)
        self.assertEqual(len(are.child),0)
        self.assertEqual(are.subtreeType,'NUMBER')
        self.assertEqual(are.dfsTag,0)
        
    def testHierarchySimplification2(self):
        tree=computeTree(data.give_USA_president()['sentences'][0])
        simplify(tree)
        root=tree
        # Root
        self.assertEqual(root.wordList,[Word("ROOT",0)])
        self.assertEqual(root.namedEntityTag,'undef')
        self.assertEqual(root.dependency,'t0')
        self.assertEqual(root.parent,None)
        self.assertEqual(len(root.child),1)
        self.assertEqual(root.subtreeType,'PERSON')
        self.assertEqual(root.dfsTag,0)
        # Is
        is_=root.child[0]
        self.assertEqual(is_.wordList,[Word("identity",2,'VBZ')])
        self.assertEqual(is_.namedEntityTag,'undef')
        self.assertEqual(is_.dependency,'t0')
        self.assertEqual(is_.parent,root)
        self.assertEqual(len(is_.child),1)
        self.assertEqual(is_.subtreeType,'PERSON')
        self.assertEqual(is_.dfsTag,0)
        # President
        president=is_.child[0]
        self.assertEqual(president.wordList,[Word("United",4,'NNP'),Word("States",5,'NNPS'),Word("president",6,'NN')])
        self.assertEqual(president.namedEntityTag,'undef')
        self.assertEqual(president.dependency,'t1')
        self.assertEqual(president.parent,is_)
        self.assertEqual(len(president.child),0)
        self.assertEqual(president.subtreeType,'PERSON')
        self.assertEqual(president.dfsTag,0)
        
    def testHierarchyConnectors1(self):
        tree=computeTree(data.give_opera()['sentences'][0])
        simplify(tree)
        root=tree
        # Root
        self.assertEqual(root.wordList,[Word("ROOT",0)])
        self.assertEqual(root.namedEntityTag,'undef')
        self.assertEqual(root.dependency,'t0')
        self.assertEqual(root.parent,None)
        self.assertEqual(len(root.child),1)
        self.assertEqual(root.subtreeType,'undef')
        self.assertEqual(root.dfsTag,0)
        # identity
        identity=root.child[0]
        self.assertEqual(identity.wordList,[Word("definition",2,'VBD')])
        self.assertEqual(identity.namedEntityTag,'undef')
        self.assertEqual(identity.dependency,'t0')
        self.assertEqual(identity.parent,root)
        self.assertEqual(len(identity.child),1)
        self.assertEqual(identity.subtreeType,'undef')
        self.assertEqual(identity.dfsTag,0)
        # and
        andw=identity.child[0]
        self.assertEqual(andw.wordList,[Word("and",1000,None)])
        self.assertEqual(andw.namedEntityTag,'undef')
        self.assertEqual(andw.dependency,'t1')
        self.assertEqual(andw.parent,identity)
        self.assertEqual(len(andw.child),2)
        self.assertEqual(andw.subtreeType,'undef')
        self.assertEqual(andw.dfsTag,0)
        # first1
        first1=andw.child[0]
        self.assertEqual(first1.wordList,[Word("first",4,'JJ')])
        self.assertEqual(first1.namedEntityTag,'ORDINAL')
        self.assertEqual(first1.dependency,'connector')
        self.assertEqual(first1.parent,andw)
        self.assertEqual(len(first1.child),1)
        self.assertEqual(first1.subtreeType,'undef')
        self.assertEqual(first1.dfsTag,0)
        # first2
        first2=andw.child[1]
        self.assertEqual(first2.wordList,[Word("first",4,'JJ')])
        self.assertEqual(first2.namedEntityTag,'ORDINAL')
        self.assertEqual(first2.dependency,'connector')
        self.assertEqual(first2.parent,andw)
        self.assertEqual(len(first2.child),1)
        self.assertEqual(first2.subtreeType,'undef')
        self.assertEqual(first2.dfsTag,0)
        # gilbert
        gilbert=first1.child[0]
        self.assertEqual(gilbert.wordList,[Word("Gilbert",5,'NNP')])
        self.assertEqual(gilbert.namedEntityTag,'PERSON')
        self.assertEqual(gilbert.dependency,'connector')
        self.assertEqual(gilbert.parent,first1)
        self.assertEqual(len(gilbert.child),0)
        self.assertEqual(gilbert.subtreeType,'undef')
        self.assertEqual(gilbert.dfsTag,0)
        # sullivan
        sullivan=first2.child[0]
        self.assertEqual(sullivan.wordList,[Word("Sullivan",7,'NNP'),Word("opera",8,'NN')])
        self.assertEqual(sullivan.namedEntityTag,'undef')
        self.assertEqual(sullivan.dependency,'connector')
        self.assertEqual(sullivan.parent,first2)
        self.assertEqual(len(sullivan.child),0)
        self.assertEqual(sullivan.subtreeType,'undef')
        self.assertEqual(sullivan.dfsTag,0)        

    def testHierarchyConnectors2(self):
        tree=computeTree(data.give_chief()['sentences'][0])
        simplify(tree)
        root=tree
        # Root
        self.assertEqual(root.wordList,[Word("ROOT",0)])
        self.assertEqual(root.namedEntityTag,'undef')
        self.assertEqual(root.dependency,'t0')
        self.assertEqual(root.parent,None)
        self.assertEqual(len(root.child),1)
        self.assertEqual(root.subtreeType,'PERSON')
        self.assertEqual(root.dfsTag,0)
        # and
        andw=root.child[0]
        self.assertEqual(andw.wordList,[Word("and",1000,None)])
        self.assertEqual(andw.namedEntityTag,'undef')
        self.assertEqual(andw.dependency,'t0')
        self.assertEqual(andw.parent,root)
        self.assertEqual(len(andw.child),2)
        self.assertEqual(andw.subtreeType,'PERSON')
        self.assertEqual(andw.dfsTag,0)
        # identity
        identity1=andw.child[0]
        self.assertEqual(identity1.wordList,[Word("identity",2,'VBZ')])
        self.assertEqual(identity1.namedEntityTag,'undef')
        self.assertEqual(identity1.dependency,'connector')
        self.assertEqual(identity1.parent,andw)
        self.assertEqual(len(identity1.child),1)
        self.assertEqual(identity1.subtreeType,'PERSON')
        self.assertEqual(identity1.dfsTag,0)
        # identity
        identity2=andw.child[1]
        self.assertEqual(identity2.wordList,[Word("identity",2,'VBZ')])
        self.assertEqual(identity2.namedEntityTag,'undef')
        self.assertEqual(identity2.dependency,'connector')
        self.assertEqual(identity2.parent,andw)
        self.assertEqual(len(identity2.child),1)
        self.assertEqual(identity2.subtreeType,'PERSON')
        self.assertEqual(identity2.dfsTag,0)
        # chief
        chief=identity1.child[0]
        self.assertEqual(chief.wordList,[Word("chief",4,'NN')])
        self.assertEqual(chief.namedEntityTag,'undef')
        self.assertEqual(chief.dependency,'t1')
        self.assertEqual(chief.parent,identity1)
        self.assertEqual(len(chief.child),0)
        self.assertEqual(chief.subtreeType,'PERSON')
        self.assertEqual(chief.dfsTag,0)
        # prime minister
        prime=identity2.child[0]
        self.assertEqual(prime.wordList,[Word("prime",6,'JJ'),Word("minister",7,'NN')])
        self.assertEqual(prime.namedEntityTag,'undef')
        self.assertEqual(prime.dependency,'t1')
        self.assertEqual(prime.parent,identity2)
        self.assertEqual(len(prime.child),0)
        self.assertEqual(prime.subtreeType,'PERSON')
        self.assertEqual(prime.dfsTag,0)        
