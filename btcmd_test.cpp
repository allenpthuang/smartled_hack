// g++ -std=c++20 -o btcmd_test btcmd_test.cpp
// BT packet size: 20

#include <iostream>
#include "btcmd.h"

int main() {
  std::cout << "BT packet size: "
            << sizeof(BTCmd) << std::endl;
  return 0;
}
