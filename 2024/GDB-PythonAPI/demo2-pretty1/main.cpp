/**
 * @brief This is a sample program to demo GDB Pretty function
 * @ref: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/developer_guide/debuggingprettyprinters
 * 
 */

enum Fruits {Orange, Apple, Banana};

class Fruit
{
  int fruit;

 public:
  Fruit (int f)
    {
      fruit = f;
    }
};

int main()
{
  Fruit myFruit(Apple);
  Fruit myFruit1(Orange);
  Fruit myFruit2(Banana);
  return 0;                                           
}
