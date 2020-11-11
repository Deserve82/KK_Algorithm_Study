import java.util.*;

// Name :
// Student ID :

@SuppressWarnings("unchecked")
class BST <T extends KeyValue> {
	class TreeNode <U extends KeyValue> {
		U data;	// storage for data : in HW 3, T will be Item
		TreeNode<U> leftChild;	// link to the left Child
		TreeNode<U> rightChild;	// link to the right Child

		// constructors come here
		TreeNode() {
			leftChild = rightChild = null;
		}
		TreeNode(U d) {
			// data is given
			data = d;
			// the leftChild and rightChild field are null
			leftChild = rightChild = null;
		}
	};

	TreeNode <T> root;
	BST() { 
		// BST constructor. 
		root = null;
	}

	void Show() {
		System.out.print( "PRE  Order : ");
		PreOrder(root);
		System.out.println("");
		System.out.print("IN   Order : ");
		InOrder(root);
		System.out.println("");
		System.out.print("POST Order : ");
		PostOrder(root);
		System.out.println("");
		System.out.print("Number of Nodes : ");
		System.out.println( Count(root));
		System.out.print("HEIGHT : ");
		System.out.println( Height(root));
		System.out.println("");
	}

	boolean  Insert(T item)  {
		// first search the key

		int value = item.GetValue();
		int key = item.GetKey();
		TreeNode<T> ptr, parent;
		parent = root;
		ptr = new TreeNode<T>(item);

		if(root == null) {
			root = ptr;
			return true;
		}

		if (Get(item) != null){
			return false;
		}


		while (true) {
			if (parent.data.GetKey() > key) {
				if (parent.leftChild == null) {
					parent.leftChild = ptr;
					break;
				}
				else {
					parent = parent.leftChild;
					continue;
				}
			}

			else {
				if (parent.rightChild == null){
					parent.rightChild = ptr;
					break;
				}
				else {
					parent = parent.rightChild;
					continue;
				}
			}
		}

		return true;
	}

	T Get(T item)  {
		// use the key field of item and find the node
		// do not use val field of item

		int key = item.GetKey();

		TreeNode<T> ptr;
		ptr = root;
		while (ptr.data.GetKey() != key){
			if (ptr.data.GetKey() > key && ptr.leftChild == null) return null;
			else if (ptr.data.GetKey() < key && ptr.rightChild == null) return null;
			else {
				if (ptr.data.GetKey() < key) ptr = ptr.rightChild;
				else if(ptr.data.GetKey() > key) ptr = ptr.leftChild;
			}
		}
		return ptr.data;
	} 


	boolean Delete(T item)  {
		int key = item.GetKey();

		if (root == null || Get(item) == null)
			return false;// non existing key

		char leftOrRight = 'n';
		TreeNode<T> prev, curr;
		prev = root;
		curr = root;
		while (true) {
			if (curr.data.GetKey() == key){
				if (curr.leftChild != null && curr.rightChild != null){
					TreeNode<T> leftPivot = curr.leftChild;
					TreeNode<T> leftPivotParent = curr;
					while (leftPivot.rightChild != null) {
						leftPivotParent = leftPivot;
						leftPivot = leftPivot.rightChild;
					}
					if (leftPivot.leftChild != null) {
						leftPivotParent.rightChild = leftPivot.leftChild;
					}else {
					leftPivotParent.rightChild = null;}
					if (leftOrRight == 'n') {
						leftPivot.leftChild = root.leftChild;
						leftPivot.rightChild = root.rightChild;
						root = leftPivot;
					} else if (leftOrRight == 'r'){
						leftPivot.leftChild = curr.leftChild;
						leftPivot.rightChild = curr.rightChild;
						prev.rightChild = leftPivot;
					} else {
						leftPivot.leftChild = curr.leftChild;
						leftPivot.rightChild = curr.rightChild;
						prev.leftChild = leftPivot;
					}
				}
				else if (curr.leftChild == null && curr.rightChild == null){
					if (leftOrRight == 'n') {
						root = null;
					} else if (leftOrRight == 'r') {
						prev.rightChild = null;
					} else {
						prev.leftChild = null;
					}
				}
				else {
					if (curr.leftChild == null) {
						if (leftOrRight == 'n') {
							root = curr.rightChild;
						}
						else if (leftOrRight == 'r') {
							prev.rightChild = curr.rightChild;
						} else {
							prev.leftChild = curr.rightChild;
						}
					} else {
						if (leftOrRight == 'n'){
							root = curr.leftChild;
						} else if (leftOrRight == 'r'){
							prev.rightChild = curr.leftChild;
						} else {
							prev.leftChild = curr.leftChild;
						}
					}
				}
				break;
			} else if(curr.data.GetKey() > key){
				prev = curr;
				curr = curr.leftChild;
				leftOrRight = 'l';
			} else {
				prev = curr;
				curr = curr.rightChild;
				leftOrRight = 'r';
			}

		}

		return true;
	}

	void  PreOrder(TreeNode<T> t)  {
		if (t!=null){
			System.out.print("["+t.data.GetKey()+"("+t.data.GetValue()+")]");
			PreOrder(t.leftChild);
			PreOrder(t.rightChild);
		}
	}

	void  InOrder(TreeNode<T> t)  {
		if (t!=null){
			InOrder(t.leftChild);
			System.out.print("["+t.data.GetKey()+"("+t.data.GetValue()+")]");
			InOrder(t.rightChild);
		}
	}

	void  PostOrder(TreeNode<T> t)  {
		if (t!=null){
			PostOrder(t.leftChild);
			PostOrder(t.rightChild);
			System.out.print("["+t.data.GetKey()+"("+t.data.GetValue()+")]");
		}
	}

	int  Count(TreeNode<T> t)  {
		if (t!=null){
			return 1 + Count(t.leftChild) + Count(t.rightChild);
		}
		return 0;
	}

	int  Height(TreeNode<T> t)  {
		if (t!=null){
			return 1 + Math.max(Height(t.leftChild), Height(t.rightChild));
		}
		return 0;
	}
}
