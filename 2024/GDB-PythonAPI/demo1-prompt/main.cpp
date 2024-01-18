#include <iostream>

void MyFunction(int x, float y) {
    std::cout << "Inside MyFunction. x: " << x << ", y: " << y << std::endl;
}

int main() {
    int a = 42;
    float b = 3.14;

    std::cout << "Hello, CppIndians /n This is prompt Demo!" << std::endl;

    MyFunction(a, b);

    return 0;
}
