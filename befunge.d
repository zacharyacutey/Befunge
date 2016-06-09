import std.stdio;
class Stack
{
  this()
  {
    this.val=[];
  }
  private int[] val;
  public int pop()
  {
    if(this.val.length==0)
    {
      return 0;
    }
    else
    {
      int tmp = val[val.length - 1];
      this.val.length -= 1;
      return tmp;
    }
  }
  public void push(int arg)
  {
    this.val~=arg;
  }
}
