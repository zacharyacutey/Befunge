module data.stack;
class Stack(T)
{
  private T[] value;
  this()
  {
  }
  public T pop()
  {
    if(this.value.length==0)
    {
      return T.init;
    }
    else
    {
      T tmp = this.value[this.value.length - 1];
      this.value.length = this.value.length-1;
      return tmp;
    }
  }
  public void push(T val)
  {
    this.value~=val;
  }
}
