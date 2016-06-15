import data.stack;
int LEFT = 0;
int RIGHT = 1;
int UP = 2;
int DOWN = 3;
class Program : Stack!int
{
  public void PushZero()
  {
    this.push(0);
  }
  public void PushOne()
  {
    this.push(1);
  }
  public void PushTwo()
  {
    this.push(2);
  }
  public void PushThree()
  {
    this.push(3);
  }
  public void PushFour()
  {
    this.push(4);
  }
  public void PushFive()
  {
    this.push(5);
  }
  public void PushSix()
  {
    this.push(6);
  }
  public void PushSeven()
  {
    this.push(7);
  }
  public void PushEight()
  {
    this.push(8);
  }
  public void PushNine()
  {
    this.push(9);
  }
  public void Add()
  {
    int b = this.pop();
    int a = this.pop();
    this.push(a+b);
  }
}
