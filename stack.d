module stack;
class Stack
{

  private int[] val;
  this()
  {
    this.val = [];
    
  }
  public bool empty()
  {
    return this.val.length==0;
  }
  public int pop()
  {
    if(this.empty())
    {
      return 0;
    }
    int temp = this.val[this.val.length - 1];
    this.val.length = this.val.length - 1;
    return temp;
  }
  public void push(int value)
  {
    this.val ~= value;
  }
}
