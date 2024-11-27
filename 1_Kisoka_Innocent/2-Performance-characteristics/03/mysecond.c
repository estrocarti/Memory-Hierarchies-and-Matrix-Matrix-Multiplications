#include <stdio.h>
#include <sys/time.h>

double get_current_time_in_seconds() {
    struct timeval tp;
   
    int i;

    //current time
    i = gettimeofday(&tp, NULL);
    
    // Error check for gettimeofday()
    if (i != 0) {
        printf("Error: gettimeofday failed\n");
        return -1.0;
    }

    // Return time in seconds (tv_sec) and microseconds (tv_usec) 
    return (double)tp.tv_sec + (double)tp.tv_usec * 1e-6;
}

int main() {
    double current_time = get_current_time_in_seconds();
    printf("Current time: %f seconds\n", current_time);
    return 0;
}


