<?php

# Author: Cj
# Depth First Search Binary Tree
# preorder/inordr/postorder


# Binary Node
class Node {
    public $left;
    public $right;
    public $data;

    public function __construct($data) {
        $this->data = $data;
    }
}

/*
#  Depth First Search Binary Tree
*/
class dfs {
    
    public $data;
    public $root;

    public function __construct(Node $root) {
        $this->root = $root;
    }

    /**
     * preorder: depth first search
     * @param $data
     */
    public function preorder($node) {
        static $data;

        if (!$node)
            return;

        $data[] = $node->data;
        if ($node->left)
             $this->preorder($node->left);

        if ($node->right)
            $this->preorder($node->right);
        
        return $data;
    }

    public function inorder($node) {
        static $data;

        if (!$node)
            return $data;

        if ($node->left)
            $this->inorder($node->left);

        $data[] =  $node->data;

        if ($node->right)
            $this->inorder($node->right);

        return $data;
    }

    public function postorder($node) {
        static $data;

        if (!$node)
            return $data;

        if ($node->left)
            $this->postorder($node->left);
        
        if ($node->right)
            $this->postorder($node->right);

        $data[] = $node->data;

        return $data;
    }
}

$root = new Node(21);
$root->left = new Node(15);
$root->left->left = new Node(5);
$root->left->right = new Node(9);
$root->right = new Node(29);
$root->right->left = new Node(30);
$root->right->right = new Node(40);

$dfs = new dfs($root);

print_r($dfs->preorder($root));
echo "\n";
print_r($dfs->inorder($root));
echo "\n";
print_r($dfs->postorder($root));
echo "\n";
