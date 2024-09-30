struct Node{
    int val;
    Node*next;
    Node* prev;
    Node(int x):val(x),next(nullptr),prev(nullptr){}
};
class CustomStack {
private:
    Node* head;
    Node* tail;
    int size,maxcapacity;
public:
    CustomStack(int maxSize): head(nullptr) , tail(nullptr) , size(0) ,  maxcapacity(maxSize) {}

    void push(int x) {
        if(size==maxcapacity){
            return ;
        }
        Node*newNode=new Node(x);
        if (head==nullptr){
            head=tail=newNode;
        }
        else{
            newNode->next=head;
            head->prev=newNode;
            head=newNode;
        }
        size++;
    }

    int pop() {
        if (head==nullptr){
            return -1;
        }
        int ans=head->val;
        Node*temp=head;
        if(head==tail){
            head=tail=nullptr;
        }
        else{
            head=head->next;
            head->prev=nullptr;
        }
        delete temp;
        size--;
        return ans;
    }

    void increment(int k, int val) {
        Node * temp=tail;
        int limit=min(k,size);
        while(limit-->0 && temp!=nullptr){
            temp->val+=val;
            temp=temp->prev;
        }
    }
};