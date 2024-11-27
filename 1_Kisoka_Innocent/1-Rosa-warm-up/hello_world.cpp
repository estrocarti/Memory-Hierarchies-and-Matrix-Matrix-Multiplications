#include <iostream>
#include <unistd.h> // getting hostname

int main() {
    char hostname[1024];
    gethostname(hostname, 1024);
    
    std::cout << "Hello World! is running on host: " << hostname << std::endl;
    return 0;
}