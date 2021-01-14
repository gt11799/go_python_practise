package main

import (
	"fmt"
	"math/rand"
	"strings"
)

type Node struct {
	Val int
	Next *Node
}


func genRandom() int{
	// -98 ~ 97
	return int(rand.Int63n(195)) - 98
}

func genList(nodeRoot *Node) {
	idx := 99
	for {
		if idx <= 0 {
			break
		}
		node := Node{Val: genRandom()}
		nodeRoot.Next = &node
		nodeRoot = &node
		idx--
	}
	return
}

func printList(node *Node) {
	str := "["
	for {
		str = str + fmt.Sprintf("%d,", node.Val)
		if node.Next == nil {
			break
		}
		node = node.Next
	}
	str = strings.TrimRight(str, ",")
	str = str + "]"
	fmt.Println(str)
}

func removeNagetive(node *Node) *Node {
	nodeRoot := node
	for {
		if nodeRoot.Val > 0 {
			break
		}
		nodeRoot = nodeRoot.Next
	}
	if nodeRoot.Next == nil {
		return nodeRoot
	}
	nodeLast := nodeRoot
	nodeNext := nodeRoot.Next
	for {
		if nodeNext.Next == nil {
			nodeLast.Next = nil
			break
		}
		if nodeNext.Val > 0 {
			nodeLast.Next = nodeNext
			nodeLast = nodeNext
		}
		nodeNext = nodeNext.Next
	}
	return nodeRoot
}

func main() {
	val := genRandom()
	node := Node{Val: val}
	fmt.Println("---start----")
	genList(&node)
	printList(&node)
	fmt.Println("---start remove----")
	newNode := removeNagetive(&node)
	printList(newNode)
	fmt.Println("---end----")
}
