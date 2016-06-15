import data.stack;
int LEFT = 0;
int RIGHT = 1;
int UP = 2;
int DOWN = 3;
class Program : Stack!int
{
  public void Add()
  {
    int b = this.pop();
    int a = this.pop();
    this.push(a+b);
  }
}
